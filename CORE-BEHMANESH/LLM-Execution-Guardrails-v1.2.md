# LLM Execution Guardrails v1.3

**Compatibility note:** The repository path retains the historical `v1.2` filename for backward references; the document content is version 1.3.

**راهنمای اجرای ایمن، دقیق و پایدار شاخص بهمنش توسط مدل‌های زبانی**

**نسخه:** 1.3
**تاریخ:** ۴ ژوئن ۲۰۲۶
**سازگار با:** CORE_BEHMANESH v1.0 + BIO v1.0 + BSI v3.5 Development Release
**تغییرات نسبت به v1.2:**
- سازگاری صریح با BSI v3.5 و Prompt-First execution
- ارجاع ساختار خروجی به قرارداد canonical لایه C
- تفکیک خروجی تحلیلی از workflow و audit trace

**تغییرات تاریخی نسبت به v1.0:**
- اضافه شدن Rule#0 — Core Claim First
- ارجاع به EIG Module و Assumption Excavation Protocol
- به‌روزرسانی چک‌لیست پیش از تحلیل
- اضافه شدن Correction Prompt برای EIG Drift

---

## مقدمه

مدل‌های زبانی هنگام اجرای شاخص بهمنش مستعد چهار نوع انحراف هستند:

**Methodological Drift** — منحرف شدن از SOP به تحلیل آزاد
**Manifest Bias** — ماندن در لایه ظاهری و ندیدن لایه پنهان
**Partial Repository Reading** — اجرای تحلیل بدون خواندن کامل مخزن
**Overconfidence** — ارائه INFERENCE به‌عنوان FACT

این سند مجموعه‌ای از قوانین، چک‌لیست‌ها و مکانیسم‌های پیشگیرانه است
تا کیفیت اجرا نزدیک به سطح حرفه‌ای باقی بماند.

---

## ۱. اصول اساسی Guardrails (غیرقابل نقض)

### Rule #0 — Core Claim First (updated in v1.3)
**هیچ تحلیلی بدون استخراج Core Claim شروع نمی‌شود.**

قبل از هر اقدام دیگری، ادعای مرکزی نویسنده/متن را در یک جمله
واحد استخراج و ثبت کن. تمام بخش‌های بعدی تحلیل باید به این
Core Claim مرتبط باشند.

```
Core Claim: [یک جمله — بدون بند]
```

اگر Core Claim قابل استخراج نیست، این خودش یک یافته است:
«متن/حساب فاقد ادعای مرکزی مشخص است» — و باید گزارش شود.

---

### Rule #1 — Canonical Source Awareness
مدل باید پیش از تحلیل، منابع مرجع مرتبط با دامنه و نوع تحلیل را شناسایی و در حد لازم بررسی کند؛ از جمله CORE_BEHMANESH v1.0، BIO v1.0، Master Prompt و قرارداد خروجی Layer C.

وجود دسترسی به کل مخزن پیش‌شرط اجرای مستقل Prompt-First نیست. اگر Master Prompt کامل و خودبسنده در اختیار است، نبود checkout یا دسترسی مخزن به‌خودی‌خود مانع اجرا نیست. هیچ مطالعه‌ای که واقعاً انجام نشده نباید ادعا شود.

---

### Rule #2 — Strict Ontology Adherence
تمام خروجی‌ها باید مطابق ساختار **BIO v1.0** باشند.

---

### Rule #3 — Claim Classification Discipline
استفاده اجباری از برچسب‌های:
`[FACT]` / `[INFERENCE]` / `[HYPOTHESIS]` / `[SPECULATION]`

برای تعیین برچسب از پروتکل سه‌تستی EIG Module استفاده کن.
هیچ گزاره مهمی بدون برچسب مجاز نیست.

---

### Rule #4 — Longitudinal Priority — DEPRECATED
**Deprecated:** The former minimum-60% longitudinal weighting rule is no longer part of the canonical BSI scoring architecture.

It MUST NOT be used as an additional weighting layer, override, or constraint on D2 or the overall BSI score.

Longitudinal evidence remains intrinsic to D2 and must be evaluated according to the current canonical D2 construct and subcriteria.

---

### Rule #5 — Anti-Drift Protocol
هرگاه احتمال Manifest Bias یا Methodological Drift تشخیص داده شد،
مدل موظف است:
- صریحاً گزارش دهد که drift شناسایی شده
- به SOP و Guardrails بازگردد
- تحلیل را از نقطه آخر صحیح ادامه دهد

---

### Rule #6 — EIG و Assumption Excavation اجباری در سطح ۲ و ۳
در تمام تحلیل‌های سطح ۲ و ۳:

**ابتدا:** `Assumption_Excavation_Protocol_v1.1.md` اجرا شود
→ پیش‌فرض‌های پنهان استخراج شوند

**سپس:** `Epistemic_Integrity_Gap_Analyzer_v1.0.md` اجرا شود
→ فاصله‌های معرفتی سنجیده شوند

این ترتیب اجباری است. معکوس کردن آن مجاز نیست.

---### Rule #7 — REIG Object Discipline
REIG فقط روی Draft Analysis اجرا می‌شود.
اگر REIG چک‌لیست خود را روی متن هدف اجرا کند،
این نقض مستقیم Pipeline است — به عنوان 
Methodological Drift ثبت و اصلاح شود.

## ۲. چک‌لیست اجباری پیش از تحلیل

- [ ] **Rule #0:** Core Claim استخراج شده (یک جمله واحد)
- [ ] تمام فایل‌های کلیدی مخزن خوانده شده
- [ ] CORE_BEHMANESH v1.0 و BIO v1.0 مطالعه شده
- [ ] دامنه و سطح تحلیل (۱/۲/۳) مشخص شده
- [ ] Manifest Bias Gate فعال شده
- [ ] در سطح ۲ و ۳: Assumption Excavation Protocol آماده اجراست
- [ ] در سطح ۲ و ۳: EIG Module آماده اجراست

---

## ۳. پرامپت‌های ضد انحراف

**Initialization Prompt (اجباری):**
 > «شاخص بهمنش را طبق Master Prompt BSI v3.5، قرارداد خروجی Layer C، CORE_BEHMANESH v1.0، BIO v1.0 و Guardrails v1.3 اجرا کن.
> Rule #0: ابتدا Core Claim را استخراج کن.
> سپس تمام الزامات را لیست کن و گام‌به‌گام پیش برو.»

**Correction Prompt — Methodological Drift:**
> «در اجرای قبلی دچار Methodological Drift شدی.
> دوباره Master Prompt BSI v3.5، قرارداد خروجی Layer C، CORE_BEHMANESH v1.0 و Guardrails v1.3 را اعمال کن و خروجی را اصلاح کن.»

**Correction Prompt — Manifest Bias:**
> «تحلیل در لایه Manifest متوقف شده.
> Assumption Excavation Protocol را اجرا کن
> و به لایه Latent برو.»

**Correction Prompt — EIG Drift (جدید در v1.2):**
> «فاصله‌های معرفتی بدون اجرای Assumption Excavation Protocol
> سنجیده شده‌اند. ابتدا پیش‌فرض‌ها را کشف کن، سپس EIG را اجرا کن.»

**Correction Prompt — Missing Core Claim:**
> «Rule #0 نقض شده. قبل از ادامه، Core Claim را در یک جمله
> استخراج و ثبت کن.»

---

## ۴. قرارداد خروجی

ترتیب و اجزای خروجی نهایی تابع سند canonical زیر است:

`docs/specification/ANALYTICAL_OUTPUT_CONTRACT_LAYERC_v3.5.md`

ترتیب الزامی:
1. Analysis Title and Source Identification
2. Executive Summary (شامل Core Claim)
3. Seven Main BSI Criteria (D1–D7)
4. CreativeValueAdd
5. Deep Structural Analysis (Manifest / Latent / Meta)
6. Final Synthesis
7. D2 Temporal Evidence Presentation، در صورت applicability
8. Final BSI Score

EIG، ECC و REIG گزارش‌های مستقل و شماره‌دار در خروجی Layer C نیستند؛ اثر substantive آن‌ها باید در تحلیل ساختاری، synthesis، confidence و limitations ادغام شود. Draft Analysis، REIG correction loop، Completion Gate و machine/audit trace داخلی باقی می‌مانند. جزئیات و مرزهای کامل در Layer C و Master Prompt تعیین شده‌اند.

## ۵. جدول ارجاع سریع ماژول‌ها

| ماژول | جایگاه | اجرا در |
|-------|--------|---------|
| Assumption Excavation Protocol v1.1 | `Shared_Components/` | سطح ۲ و ۳ — قبل از EIG |
| EIG Module v1.0 | `Shared_Components/` | سطح ۲ و ۳ — بعد از Assumption Excavation |
| Claim Classification | `Shared_Components/` | همه سطوح |
| Confidence Scale | `Shared_Components/` | همه سطوح |
| Fallacy & Bias Detection | `Shared_Components/` | همه سطوح |
| Scientific Modules | `Scientific_Modules/` | فقط حوزه‌های علمی |

---

**این سند بخشی از راهنمای اجرای BSI v3.5 Development Release است.**

*نسخه بعدی (v1.4) در صورت نیاز بر اساس Case Studyهای واقعی به‌روزرسانی خواهد شد.*
