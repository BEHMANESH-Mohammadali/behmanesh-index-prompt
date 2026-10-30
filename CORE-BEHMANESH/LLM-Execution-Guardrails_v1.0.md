# LLM Execution Guardrails v1.0

**راهنمای اجرای ایمن، دقیق و پایدار شاخص بهمنش توسط مدل‌های زبانی**

**نسخه:** 1.0
**تاریخ:** ۳ ژوئن ۲۰۲۶
**سازگار با:** CORE_BEHMANESH v1.0 + BIO v1.0 + Behmanesh Index v3.4

---

### مقدمه

مدل‌های زبانی هنگام اجرای شاخص بهمنش مستعد **Methodological Drift**، **Manifest Bias**، **Partial Repository Reading** و **Overconfidence** هستند. این سند مجموعه‌ای از قوانین، چک‌لیست‌ها و مکانیسم‌های پیشگیرانه است تا کیفیت اجرا نزدیک به سطح حرفه‌ای باقی بماند.

---

### ۱. اصول اساسی Guardrails (غیرقابل نقض)

1. **Full Repository Awareness**
   مدل باید قبل از هر تحلیل، تمام فایل‌های کلیدی را خوانده باشد (README, SOP, CORE-BEHMANESH v1.0, BIO v1.0, Methodology).

2. **Strict Ontology Adherence**
   تمام خروجی‌ها باید مطابق ساختار **BIO v1.0** باشند.

3. **Claim Classification Discipline**
   استفاده اجباری از برچسب‌های `[FACT]`, `[INFERENCE]`, `[HYPOTHESIS]`, `[SPECULATION]`.

4. **Longitudinal Priority — DEPRECATED**
   **Deprecated:** The former minimum-60% longitudinal weighting rule is no longer part of the canonical BSI scoring architecture.

   It MUST NOT be used as an additional weighting layer, override, or constraint on D2 or the overall BSI score.

   Longitudinal evidence remains intrinsic to D2 and must be evaluated according to the current canonical D2 construct and subcriteria.

5. **Anti-Drift Protocol**
   هرگاه احتمال Manifest Bias یا Drift تشخیص داده شد، مدل موظف به گزارش صریح و اصلاح است.

---

### ۲. چک‌لیست اجباری پیش از تحلیل

- [ ] تمام فایل‌های کلیدی مخزن خوانده شده
- [ ] CORE_BEHMANESH v1.0 و BIO v1.0 مطالعه شده
- [ ] دامنه و لایه تحلیل شناسایی شده
- [ ] Manifest Bias Gate فعال شده

---

### ۳. پرامپت‌های ضد انحراف

**Initialization Prompt (اجباری):**
> "شاخص بهمنش را دقیقاً طبق SOP v3.4 + CORE_BEHMANESH v1.0 + BIO v1.0 اجرا کن. ابتدا تمام الزامات را لیست کن، سپس گام‌به‌گام پیش برو."

**Correction Prompt:**
> "در اجرای قبلی دچار Methodological Drift شدی. دوباره به SOP، CORE-BEHMANESH v1.0 و BIO v1.0 مراجعه کن و خروجی را اصلاح کن."

---

### ۴. ساختار خروجی استاندارد

هر تحلیل باید شامل:
- Domain & Context Detection
- Layered Analysis (Manifest / Latent / Meta)
- Theme & Core Node
- Weighted Score Table
- Uncertainty Report
- Final Synthesis

---

**این سند بخشی جدایی‌ناپذیر از اجرای حرفه‌ای شاخص بهمنش نسخه Hybrid v4 است.**
