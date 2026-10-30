# Behmanesh Index Ontology (BIO) v1.0

**هستی‌شناسی رسمی شاخص بهمنش**  
**نسخه:** 1.0  
**تاریخ:** ۲۸ می ۲۰۲۶  
**سازگار با:** CORE_BEHMANESH v1.0 + Behmanesh Index v3.4

---

## ۱. مقدمه

BIO v1.0 چارچوب مفهومی استاندارد برای تمام تحلیل‌های شاخص بهمنش است. این ontology تکرارپذیری، شفافیت، ماشین‌خوانی و گسترش آینده را تضمین می‌کند.

---
## Core Construct

BSI does not measure truth, popularity, authority,
scientific impact, persuasion power, or social acceptance.

BSI measures:

Epistemic Robustness

Definition:

The degree to which a knowledge artifact maintains
structural coherence, evidential grounding,
mechanistic depth, explanatory integrity,
causal consistency, and longitudinal stability
under multi-layer epistemic analysis.

BSI is therefore a measure of epistemic robustness,
not a predictor of external outcomes.
## ۲. کلاس ریشه
**BehmaneshEntity** — هر موجود تحلیلی (Account, Person, Thread, ScientificPaper, Idea و غیره)

---

## ۳. کلاس‌های اصلی

### AnalysisLayer
- ManifestLayer
- LatentLayer
- MetaLayer

### Theme
- DominantTheme
- SecondaryTheme
- CoreTheme
- EmergingTheme

### CoreNode
- MechanisticNode
- WorldviewNode
- StrategicNode
- ConceptNode

### Relation / Edge
- TemporalEdge (Longitudinal)
- CausalEdge
- FeedbackLoop
- LeveragePoint
- ContradictionEdge
- SelfReferenceEdge

### EvaluationCriterion (وزن‌دار)
- ConditionalDepth → ۲۲٪
- LongitudinalCoherence → ۱۸٪
- AuthenticEthicalLayer → ۱۸٪
- CreativeValueAdd → ۱۷٪
- StrategicDepth → ۱۲٪
- InterdisciplinaryBreadth → ۸٪
- AntiPerformativeDrift → ۵٪

#### AuthenticEthicalLayer (D3 — ۱۸٪)

**تعریف رسمی:**

D3 میزان اصالت لایه اخلاقی انسانی و قدرت راستی‌آزمایی معرفتی را می‌سنجد. این سازه از ریشه v3.3 شامل صداقت فکری، تعهد به حقیقت، اجتناب از خودفریبی، شفافیت محدودیت‌ها، falsification و آزمون‌پذیری، راستی‌آزمایی داخلی و خارجی، dogfooding در موارد مرتبط، دعوت به نقد و آمادگی برای اصلاح است.

D3 نباید به «اخلاق نمایشی نبودن» تقلیل یابد و نباید با D7 یکی گرفته شود.

**زیرمعیارهای رسمی D3:**

| زیرمعیار | وزن داخلی | تعریف |
|---|---:|---|
| Authentic_Value_Hierarchy | ۲۰٪ | اصالت انسانی و غیرایدئولوژیک ارزش‌ها، انسجام سلسله‌مراتب ارزش‌ها و provenance آن‌ها |
| Intellectual_Honesty_Truth_Commitment | ۲۰٪ | صداقت فکری، ترجیح حقیقت بر حفظ موضع و تعهد به حقیقت حتی در هزینه شخصی/اعتباری |
| Anti_Self_Deception_Criticality | ۱۵٪ | اجتناب از خودفریبی، rationalization و حذف شواهد ناسازگار؛ آمادگی برای نقد موضع خود |
| Limitation_Transparency | ۱۵٪ | شفافیت درباره محدودیت‌ها، عدم‌قطعیت‌ها، نقاط کور و دامنه اعتبار |
| Falsifiability_Testability | ۱۵٪ | آزمون‌پذیری، امکان ابطال و مشخص‌بودن شرایطی که ادعا را نقض می‌کنند |
| Verification_Openness_to_Critique | ۱۵٪ | راستی‌آزمایی داخلی/خارجی، dogfooding مرتبط، شواهد مستقل، دعوت به نقد و آمادگی برای اصلاح |

**اصل شواهدی:** نبودِ زبان اخلاقی صریح در متن علمی یا فنی به‌تنهایی نشانه ضعف D3 نیست؛ صداقت معرفتی، شفافیت محدودیت‌ها، آزمون‌پذیری و راستی‌آزمایی نیز شواهد مستقیم D3 هستند.

**مرزبندی D3 و D7:** D3 اصالت اخلاقی و صداقت/راستی‌آزمایی معرفتی را می‌سنجد؛ D7 مقاومت در برابر performative drift، attention optimization و audience-pleasing را می‌سنجد.

---

#### CreativeValueAdd (۱۷٪)

**تعریف:**  
آیا محتوا یا سازنده آن یک شکاف معرفتی واقعی را شناسایی کرده و با ترکیب حوزه‌ای هدفمند، خروجی‌ای تولید کرده که ظرفیت تولید فکر جدید و ابزارهای فکری در دیگران را ایجاد می‌کند؟

**لایه اصلی:** Latent + Meta

**زیرمعیارهای داخلی (برای راهنمایی تحلیل‌گر):**

| زیرمعیار | وزن داخلی | لایه | سوال کلیدی |
|----------|-----------|------|-----------|
| Epistemic Gap Targeting | ۳۵٪ | Latent | آیا شکاف معرفتی واقعی و مهم هدف گرفته شده است؟ |
| Combinatorial Synthesis | ۴۰٪ | Latent | آیا ترکیب موفق و ساختاری حوزه‌ها به سنتز جدید رسیده است؟ |
| Generative Capacity | ۲۵٪ | Meta | آیا خروجی، ابزار یا چارچوبی ایجاد می‌کند که دیگران بتوانند با آن فکر جدید تولید کنند؟ |

**نکته:** بیان هنری و استعاره‌سازی تنها در صورتی امتیاز مثبت دارد که در خدمت Generative Capacity باشد، نه به عنوان هدف مستقل.

---

## ۴. ماژول علمی (ScientificTextAnalysis Module)
- DisciplinaryDomain (PhysicsAndMath, Biomedical, Economics, AI, ...)
- MethodologicalStandards
- ScientificClaimType
- ScientificQualityCriteria
- ScientificUncertainty

---

## ۵. Claim Classification (اجباری)
- [FACT]
- [INFERENCE]
- [HYPOTHESIS]
- [SPECULATION]

---

## ۶. روابط کلیدی
- `hasTheme`
- `hasCoreNode`
- `belongsToLayer`
- `hasConfidence`
- `hasLongitudinalWeight` (حداقل ۰.۶)

---

**این ontology پایه تمام تحلیل‌های نسخه Hybrid v4 شاخص بهمنش خواهد بود.**
