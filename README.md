
### **LOYIHA NOMI:**

**AI-based Early Detection Model for Project Risk Factors and Schedule Delay Probability**
*(Loyiha xavf omillari va jadvaldan kechikish ehtimolini erta aniqlovchi AI modeli)*

### **1. LOYIHANING ASOSIY MAQSADI (The Goal)**

**Mijoz tili bilan aytganda:**
Bizning maqsadimiz — loyiha menejerlari uchun shunday **“Raqamli Maslahatchi” (Digital Consultant)** yaratishki, u loyiha haqidagi oddiy matnli suhbat yoki hujjatlardan ma’lumotlarni o‘zi ajratib olsin, yashirin xavflarni ko‘ra bilsin va **“Bu loyiha 80% ehtimol bilan 20 kunga kechikadi”** degan aniq ogohlantirishni, muammoni hal qilish yo‘llari bilan birga taqdim etsin.

**Ilmiy tilda:**
Loyiha maqsadi — Tabiiy Tilni Qayta Ishlash (NLP) va Mashinaviy O‘rganish (ML) algoritmlarini integratsiya qilish orqali, kiritilgan loyiha ma’lumotlari asosida xavf omillarini (Risk Factors) tasniflovchi va muddatdan kechikish ehtimolini (Schedule Delay Probability) yuqori aniqlikda bashorat qiluvchi intellektual chat-tizimini ishlab chiqishdir.



### **2. LOYIHA O‘ZI NIMA QILADI? (What it does)**

Tasavvur qiling, siz loyiha menejerisiz va yangi loyihani boshlayapsiz. Hamma narsa joyidadek tuyuladi. Lekin tajribali ekspert bir qarashda muammolarni ko‘ra oladi. Bu AI tizimi aynan shu **“Ekspert”** rolini bajaradi.

U quyidagi **uchta asosiy ishni** bajaradi:

1. **Tinglaydi va Tushunadi:** Siz tizimga loyiha haqida xuddi hamkasbingizga gapirib bergandek (chatda yozib) ma’lumot berasiz. U matn ichidan eng muhim raqamlar va faktlarni “ilib oladi”.
2. **Kelajakni ko‘radi (Bashorat):** Tizim sizning loyihangizni avvalgi minglab loyihalar tarixi bilan solishtiradi va "Sizning jamoangiz tajribasi va byudjetga qaraganda, bu loyiha o‘z vaqtida tugamasligi mumkin" degan xulosaga keladi.
3. **Yo‘l ko‘rsatadi:** Shunchaki muammoni aytmaydi, balki "Rejani o‘zgartiring" yoki "Byudjetni optimallashtiring" kabi maslahatlarni beradi.

---

### **3. FUNKSIONALLIKLAR (A–Z)**

Loyiha qanday ishlashi va qanday imkoniyatlarga ega ekanligi to‘liq ro‘yxati:

#### **A. Interaktiv Chat Interfeysi (Input)**

* **F1. Erkin matnni qabul qilish:** Foydalanuvchi qat’iy jadvallarni to‘ldirib o‘tirishi shart emas. Loyiha haqida erkin uslubda yozishi mumkin (masalan: *"Biz yangi CRM quryapmiz, byudjet 10k, muddat 3 oy"*).
* **F2. Savol-javob rejimi:** Agar foydalanuvchi muhim ma’lumotni (masalan, jamoa sonini) yozishni unutgan bo‘lsa, AI o‘zi qayta savol berib, ma’lumotni to‘ldirib oladi.

#### **B. Ma’lumotlarni Tahlil Qilish (Processing)**

* **F3. Avtomatik Ekstraktsiya (NLP):** Chatdagi matndan *Budget, Duration, Team Size, Scope, Tools* kabi 20 dan ortiq parametrlarni avtomatik ajratib oladi va orqa fonda jadvalga joylaydi.
* **F4. Hujjatlarni O‘qish:** Foydalanuvchi matn yozish o‘rniga *"Mana Texnik Topshiriq"* deb fayl (PDF/DOC) tashlasa, tizim uni o‘qib, ichidagi risklarni tahlil qiladi.

#### **C. Xavflarni Aniqlash va Baholash (Risk Detection)**

* **F5. Yashirin Riskarni Topish:** Matn ohangi va mazmuniga qarab yashirin muammolarni topadi (masalan, *"Talablar hali aniq emas"* degan gapni ko‘rsa → **High Risk** deb belgilaydi).
* **F6. Risk Faktorlarini Tasniflash:** Aniqlangan xavflarni guruhlarga ajratadi: *Moliya, Vaqt, Inson resurslari, Texnik qiyinchiliklar*.

#### **D. Bashorat Qilish (AI Prediction)**

* **F7. Kechikish Ehtimolini Hisoblash:** Mashinaviy o‘rganish modeli (XGBoost/Random Forest) barcha ma’lumotlarni tahlil qilib, aniq raqam beradi: *"Kechikish ehtimoli: 78%"*.
* **F8. Muddatni Taxmin Qilish:** *"Loyiha rejadagi 90 kun o‘rniga, taxminan 115 kun davom etishi kutilmoqda"*.

#### **E. Izoh va Tavsiyalar (XAI & Recommendations)**

* **F9. Sababni Tushuntirish (Explainability):** Nima uchun bunday bashorat qilinganini izohlaydi. *Misol: "Chunki jamoada Senior dasturchilar yo‘q va muddat loyiha hajbiga nisbatan juda qisqa."*
* **F10. Aqlli Tavsiyalar:** Vaziyatni o‘nglash uchun yechim beradi. *Misol: "Riskni kamaytirish uchun sprint vaqtini 2 haftaga uzaytirish tavsiya etiladi."*

---

### **MIJOZ UCHUN QISQA SSENARIY (User Flow)**

1. **Mijoz:** Chatga kiradi va yozadi: *"Salom, men 50,000$ byudjet bilan yangi mobil ilova qilyapman. Jamoada 3 ta junior dasturchi bor, muddatimiz 4 oy."*
2. **AI (Tizim):** Ma'lumotni tahlil qiladi va javob beradi: *"Qabul qilindi. Jamoada Senior (tajribali) mutaxassis bormi yoki faqat Juniorlarmi?"*
3. **Mijoz:** *"Faqat Juniorlar."*
4. **AI (Natija):** *"Tahlil yakunlandi.
* **Xavf darajasi:** YUQORI 🔴
* **Kechikish ehtimoli:** 85%
* **Asosiy sabab:** Jamoa tajribasi pastligi va muddatning tig'izligi.
* **Tavsiya:** Loyiha muddatini kamida 6 oygacha uzaytirish yoki bitta tajribali Team Lead yollash kerak."*


