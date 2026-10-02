# CORE_BEHMANESH v1.0
**معماری رسمی تقویت‌کننده شاخص بهمنش**

**نسخه:** 1.0  
**تاریخ:** ۲۸ می ۲۰۲۶  
**سازگار با:** Behmanesh Index v3.4 + BIO v1.0

---

## ۰. فلسفه طراحی (Design Philosophy)

CORE_BEHMANESH v1.0 یک **پروتکل تحلیلی ساخت‌یافته**، **چارچوب استدلال چندلایه** و **معماری سنتز آگاه از شواهد** است که به‌عنوان لایه تقویت‌کننده (Meta-Layer) بر روی شاخص بهمنش قرار می‌گیرد.

این سیستم به‌طور صریح موارد زیر را تفکیک می‌کند:
- **حقایق** [FACT]
- **استنتاج‌ها** [INFERENCE]
- **فرضیه‌ها** [HYPOTHESIS]
- **گمانه‌زنی‌ها** [SPECULATION]

**الزامات اصلی:**
- توضیح‌پذیری کامل (Explainability)
- کالیبراسیون اطمینان (Confidence Calibration)
- ردیابی عدم قطعیت (Uncertainty Tracking)
- تکرارپذیری (Reproducibility)
- همخوانی کامل با BIO v1.0

---

## ۱. معماری سیستم (System Architecture)
---

## ۲. موتور دامنه و زمینه (Domain & Context Engine)

### ۲.۱. Multi-Domain Detector
- تشخیص رشته اصلی و رشته‌های فرعی
- خروجی JSON با سطح اطمینان
- فعال‌سازی خودکار ScientificTextAnalysis Module در صورت تشخیص حوزه علمی

### ۲.۲. Context Memory System
- ثبت هر آیتم حافظه با: `source`, `timestamp`, `confidence`, `decay_factor`
- جداسازی حافظه از شواهد
- تشخیص drift و تناقض

### ۲.۳. Priority & Relevance Engine
امتیازدهی بر اساس:
- Conceptual Importance
- Evidence Density
- Contradiction Intensity
- Longitudinal Weight — DEPRECATED (former minimum 60% rule; not part of canonical BSI scoring)

---

## ۳. هسته علمی (Scientific Core Modules)

### ۳.۱. Foundational Disciplines
- **Physics & Mathematics**: Falsifiability, Dimensional Consistency, Mathematical Coherence
- **Medicine & Biology**: CONSORT, PRISMA, STROBE, GRADE, Cochrane
- **Economics & Behavioral**: Econometric Robustness, Causal Inference, Endogeneity
- **Philosophy & Logic**: Formal Logic, Fallacy Detection, Conceptual Precision
- **Emerging Fields**: AI, Complexity Science, Computational Social Science

### ۳.۲. ScientificTextAnalysis Module (فعال در حوزه‌های علمی)
- ارزیابی Methodological Standards
- تشخیص نوع ادعای علمی (Empirical, Theoretical, Computational و غیره)
- ارزیابی Reproducibility و Limitation Transparency

### ۳.۳. Claim Classification (اجباری)
هر گزاره باید یکی از برچسب‌های زیر را داشته باشد:
- **[FACT]**
- **[INFERENCE]**
- **[HYPOTHESIS]**
- **[SPECULATION]**

---

## ۴. موتور تحلیل متا-ساختاری

- Coherence & Logical Consistency
- Contradiction & Paradox Detection
- Fallacy & Bias Detection (Confirmation Bias, Anchoring, Motivated Reasoning و غیره)
- Narrative & Framing Analysis
- Mechanistic Realism Assessment
- Longitudinal Pattern Recognition — DEPRECATED (former minimum 60% rule; not part of canonical BSI scoring)

---

## ۵. لایه اعتبارسنجی و Verification (الزامی)

- Cross-Check بین لایه‌ها
- Adversarial Stress Testing
- Hallucination Prevention Protocol
- Grounding متنی و شواهد

---

## ۶. لایه سنتز و خروجی

- Integrated Insight
- Weighted Score Table (مطابق معیارهای شاخص بهمنش)
- Uncertainty Report
- Recommendations with Risk Disclosure
- Final Category & Synthesis

---

## ۷. حلقه بازخورد و تکامل کنترل‌شده

- Self-Evaluation
- User Feedback Integration (با اعتبارسنجی)
- Controlled Knowledge Refinement
- Version Tracking

---

## ۸. ادغام با Ontology

این معماری کاملاً با **BIO v1.0** همخوان است و تمام خروجی‌ها باید بر اساس ontology BIO v1.0 ساختاربندی شوند.

---

## ۹. الزامات توضیح‌پذیری

هر امتیاز و نتیجه باید شامل:
- مقدار
- توضیح (Explanation)
- شواهد grounding
- سطح اطمینان

---
CORE Principle:

Evaluate robustness of knowledge architecture,
not correctness of conclusions.
## ۱۰. محدودیت‌ها

- این چارچوب جایگزین expertise حوزه‌ای نیست.
- نباید استنتاج احتمالی را به صورت قطعی ارائه دهد.
- در تحلیل‌های سریع، نسخه Lite قابل استفاده است.

---

**پایان سند CORE_BEHMANESH_v1.0**
