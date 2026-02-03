import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta, datetime
import os

# Initialize Faker
fake = Faker()
Faker.seed(42)
np.random.seed(42)
random.seed(42)

def generate_dataset(num_rows=100000):
    print(f"Generating {num_rows} synthetic project records...")
    
    data = []
    
    project_types = ['Software', 'Construction', 'Research', 'Marketing', 'Consulting']
    domains = ['IT', 'Finance', 'Healthcare', 'Education', 'Manufacturing', 'Retail']
    schedule_types = ['Agile', 'Waterfall', 'Hybrid']
    statuses = ['On Track', 'Delayed', 'Completed', 'Cancelled']
    roles_list = ['Dev', 'QA', 'PM', 'Designer', 'Ba', 'Architect']
    tools_list = ['Jira', 'Trello', 'Asana', 'MS Project', 'Excel', 'ClickUp']
    
    for _ in range(num_rows):
        # Basic Info
        proj_id = fake.uuid4()[:8]
        proj_name = fake.bs().title()
        proj_type = random.choice(project_types)
        domain = random.choice(domains)
        org = fake.company()
        
        # Scopes & Text
        scope_desc = fake.sentence(nb_words=10)
        out_scope = fake.sentence(nb_words=5)
        goal = fake.sentence(nb_words=8)
        deliverables = ", ".join(fake.words(nb=3))
        
        # Dates & Duration
        start_date = fake.date_between(start_date='-2y', end_date='today')
        # Simulate planned duration (30 to 730 days)
        duration_days = random.randint(30, 730)
        planned_end_date = start_date + timedelta(days=duration_days)
        
        # Budget
        budget = round(random.uniform(5000, 5000000), 2)
        currency = 'USD'
        
        # Team & Process
        schedule = random.choice(schedule_types)
        team_size = random.randint(3, 50)
        start_roles = random.sample(roles_list, k=random.randint(2, len(roles_list)))
        team_roles = ", ".join(start_roles)
        avg_exp = round(random.uniform(1, 15), 1)
        pm_name = fake.name()
        stakeholders = random.randint(1, 20)
        
        # Performance Metrics (Earned Value Management checks)
        # Planned Value (PV) is usually budget * expected_progress
        # But for simplicity, let's treat PV as a fraction of Budget based on time elapsed?
        # Let's just randomise reasonably.
        
        # Simulate if the project is actually problematic or not
        is_risky = random.random() < 0.3  # 30% chance of being inherently risky/delayed
        
        # Progress Percent
        # If today is after planned end date, it should be near 100% or delayed context.
        # Let's keep it simple: progress 0-100%
        progress = round(random.uniform(0, 100), 2)
        
        # PV: roughly budget * (progress/100) +/- noise
        pv = budget * (progress / 100) * random.uniform(0.9, 1.1)
        
        # EV (Earned Value): If risky, EV is lower than PV
        if is_risky:
            ev = pv * random.uniform(0.6, 0.95)
        else:
            ev = pv * random.uniform(0.95, 1.05)
            
        # Actual Cost (AC): If risky, AC is higher than EV
        if is_risky:
            ac = ev * random.uniform(1.1, 1.5)
        else:
            ac = ev * random.uniform(0.9, 1.1)
            
        # Status assignment (simplified based on risk)
        if progress == 100:
            status = 'Completed'
            actual_end_date = start_date + timedelta(days=int(duration_days * (random.uniform(0.9, 1.5))))
        else:
            status = random.choice(['On Track', 'Delayed']) if not is_risky else 'Delayed'
            actual_end_date = None # Not finished yet
            
        # Location
        country = fake.country()
        region = fake.state()
        language = 'English'
        tools = ", ".join(random.sample(tools_list, k=random.randint(1, 4)))
        
        # --- DERIVE TARGET VARIABLE: schedule_delay ---
        # Logic: 
        # 1. If Completed, did it take longer than planned?
        # 2. If In Progress, is EV < PV significantly? Or Status explicitly 'Delayed'?
        # 3. SPI (Schedule Performance Index) = EV / PV. If SPI < 0.9, likely delayed.
        
        label_delay = 0
        
        # Calculate SPI
        spi = ev / pv if pv > 0 else 1.0
        
        # Scenario 1: Completed projects
        if status == 'Completed' and actual_end_date:
            actual_duration = (actual_end_date - start_date).days
            if actual_duration > duration_days * 1.05: # 5% buffer
                label_delay = 1
        
        # Scenario 2: Ongoing projects
        else:
            if status == 'Delayed':
                label_delay = 1
            elif spi < 0.90:
                label_delay = 1
            elif ac > ev * 1.2: # Cost overrun often correlates with delay
                label_delay = 1
        
        # Add actual_end_date for completed projects (optional to keep in dataset or not, 
        # but user schema requested end_date. I'll use planned_end_date as 'end_date' field 
        # because that's usually the target. Or I can have 'planned_end_date' and 'actual_end_date'.
        # The schema asks for 'end_date', I will assume 'planned_end_date' for planning data.
        
        
        row = {
            'project_id': proj_id,
            'project_name': proj_name,
            'project_type': proj_type,
            'project_domain': domain,
            'organization_name': org,
            'scope_description': scope_desc,
            'out_of_scope': out_scope,
            'project_goal': goal,
            'key_deliverables': deliverables,
            'start_date': start_date,
            'end_date': planned_end_date, # Planned End Date
            'duration_days': duration_days,
            'budget_usd': budget,
            'currency': currency,
            'schedule_type': schedule,
            'team_size': team_size,
            'team_roles': team_roles,
            'team_experience_avg_years': avg_exp,
            'project_manager_name': pm_name,
            'stakeholder_count': stakeholders,
            'planned_value': round(pv, 2),
            'earned_value': round(ev, 2),
            'actual_cost': round(ac, 2),
            'progress_percent': progress,
            'status': status,
            'country': country,
            'region': region,
            'project_language': language,
            'tools_used': tools,
            'schedule_delay': label_delay
        }
        data.append(row)
        
    df = pd.DataFrame(data)
    
    # Save
    os.makedirs('dataset', exist_ok=True)
    output_path = 'dataset/projects_dataset.csv'
    df.to_csv(output_path, index=False)
    print(f"Dataset generated at {output_path}")
    print(df['schedule_delay'].value_counts())
    return df

if __name__ == "__main__":
    generate_dataset()
