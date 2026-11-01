# BSI Calculation Formula — Hybrid v3x
**نسخه:** v3.2
**همگام با:** BIO v1.0 (سند مرجع رسمی)
**بر اساس:** SOP v3.4.2 + CORE_BEHMANESH v1.0
**تاریخ به‌روزرسانی:** ۲۶ ژوئن ۲۰۲۶
**تغییر نسبت به v3.1:**
- همگام‌سازی نام ۷ معیار با BIO v1.0
- همگام‌سازی وزن‌های ۷ معیار با BIO v1.0
- حفظ کامل زیرمعیارهای اصلی (بدون حذف)
- اصلاح D4: زیرمعیارها مطابق BIO (Combinatorial/EGT/Generative)
- اصلاح D6: بازگشت به ترتیب وزنی اصلی

> **قانون مرجع:** در هر تعارض بین این سند و BIO v1.0،
> BIO v1.0 مرجع است. این سند فقط Operationalization BIO است.

---

## ۱. سازه اصلی (Core Construct)

BSI یک معیار **Epistemic Robustness** است — نه حقیقت، نه اجماع، نه اقتدار.

```
Epistemic Robustness = درجه‌ای که یک Knowledge Artifact
انسجام ساختاری، پایه‌گذاری شواهدی، عمق مکانیسمی،
یکپارچگی تبیینی، سازگاری علّی و پایداری طولانی‌مدت
را تحت تحلیل معرفتی چندلایه حفظ می‌کند.
```

---

## ۲. معیارها و وزن‌های رسمی (مطابق BIO v1.0)

| # | نام رسمی (BIO v1.0) | وزن | لایه اصلی |
|---|---|---|---|
| D1 | ConditionalDepth | **0.22** | Manifest + Latent |
| D2 | LongitudinalCoherence | **0.18** | Meta + Temporal |
| D3 | AuthenticEthicalLayer | **0.18** | Latent + Meta |
| D4 | CreativeValueAdd | **0.17** | Latent + Meta |
| D5 | StrategicDepth | **0.12** | Manifest + Latent |
| D6 | InterdisciplinaryBreadth | **0.08** | Manifest |
| D7 | AntiPerformativeDrift | **0.05** | Meta |
| | **مجموع** | **1.00** | |

---

## ۳. فرمول محاسبه BSI

### فرمول خطی (استاندارد):
```
BSI_linear = Σ(i=1→7) [ w_i × D_i ] × (1 - EIG_penalty)
```

### فرمول غیرخطی (تنبیه ضعف بنیادین):
```
BSI_nonlinear = 100 × Π(i=1→7) [ (D_i / 100)^w_i ] × (1 - EIG_penalty)
```

**نکته انتخاب فرمول:**
- فرمول خطی: تحلیل‌های عمومی و مقایسه‌ای
- فرمول غیرخطی: وقتی یک معیار بحرانی (D1 یا D2) بسیار پایین است

### محاسبه EIG_penalty:
```
EIG_penalty = EIG_avg / 20
```
`EIG_avg` میانگین وزن‌دار چهار فاصله EIG است (مقیاس ۰ تا ۱۰). طبق تصمیم تأییدشدهٔ مالک پروژه در ۳۱ اکتبر ۲۰۲۶، ضریب جریمه `/20` است؛ بنابراین حداکثر جریمه ۰٫۵ خواهد بود.

---

## ۴. فرمول تفصیلی هر معیار (زیرشاخص‌ها)

### D1 — ConditionalDepth (وزن: 0.22)
**تعریف BIO:** عمق استدلال شرطی و پیش‌بینی‌کننده — آیا محتوا روابط «اگر...آنگاه» مکانیسمی می‌سازد؟

```
D1 = 0.35 × Causal_Link_Density
   + 0.25 × Testable_Predictions
   + 0.25 × Counterfactual_Resilience
   + 0.15 × Longitudinal_Accuracy
```

| زیرشاخص | وزن | تعریف |
|---|---|---|
| Causal_Link_Density | 0.35 | تراکم روابط علت-معلولی مستند در متن |
| Testable_Predictions | 0.25 | آیا پیش‌بینی‌های قابل آزمون وجود دارد؟ |
| Counterfactual_Resilience | 0.25 | پایداری استدلال در برابر سناریوهای خلاف واقع |
| Longitudinal_Accuracy | 0.15 | دقت پیش‌بینی در طول زمان |

---

### D2 — LongitudinalCoherence (وزن: 0.18)
**تعریف BIO:** تداوم و انسجام استدلال در طول زمان، متن‌ها و زمینه‌ها

```
D2 = 0.40 × Trajectory_Stability
   + 0.30 × Contradiction_Resolution_Rate
   + 0.20 × Stable_Nodes_Consistency
   + 0.10 × Theme_Evolution
```

| زیرشاخص | وزن | تعریف |
|---|---|---|
| Trajectory_Stability | 0.40 | ثبات مسیر فکری در طول زمان |
| Contradiction_Resolution_Rate | 0.30 | نرخ حل تناقضات داخلی |
| Stable_Nodes_Consistency | 0.20 | انسجام گره‌های مفهومی پایدار |
| Theme_Evolution | 0.10 | تکامل آگاهانه تم‌ها (Evolution نه Rupture) |

**DEPRECATED — Legacy Longitudinal Weight Rule**

قاعدهٔ «وزن Longitudinal حداقل ۶۰٪» متعلق به معماری‌های پیش از BIO v1.0 است و در معماری canonical فعلی BSI اعمال نمی‌شود.

این قاعده نباید به‌عنوان وزن اضافی، override، constraint یا لایهٔ مستقل بر محاسبهٔ D2 یا امتیاز کلی BSI اعمال شود.

مرجع فعلی:
- D2 LongitudinalCoherence = 0.18
- تفکیک داخلی D2 طبق operationalization رسمی این سند باقی می‌ماند.
- نقش longitudinal evidence در خود سازهٔ D2 حفظ می‌شود، نه به‌صورت یک وزن مستقل ۶۰٪.
**تفکیک اجباری EIG:** Evolution (آگاهانه) از Rupture (ناآگاهانه).

---



### D2-SI — Single-Input Scoring Operationalization (Proposed v0.2)

**Status:** Proposed single-input operationalization. The canonical longitudinal D2 formula and D2's official BSI weight of 0.18 remain unchanged.

When only one content item is available, temporal trajectory cannot be validly inferred. For a numeric single-input result, use the four dimensions below. This operationalization is not prescribed as an internal weighting by BIO v1.0.

| D2-SI subcriterion | Weight | Operational definition and checks |
|---|---:|---|
| Internal Structural Coherence | 0.40 | Assess logical and functional fit among the problem, premises, claims, concepts, evidence, reasoning, conclusions, and limitations. Do conclusions follow from their stated support? Are inferential steps defensible and certainty proportionate? Are material contradictions unresolved? A difference or change is not automatically a contradiction. |
| Developmental Consistency | 0.30 | Assess continuity and development of concepts and arguments within the same content: do successive stages build on, refine, or justifiably revise earlier stages? Are intermediate conclusions connected, and does development deepen the argument rather than add disconnected claims? This is not historical development across time; repetition is neither automatically a strength nor a weakness. |
| Cross-Context Transfer | 0.20 | Assess whether concepts or principles are validly transferred across contexts, domains, or analytical levels. Check the basis for transfer, relevant similarities and differences, preservation of meaning and boundary conditions, and whether analogy or generalization exceeds the evidence. The number of domains is not itself merit. If no meaningful transfer opportunity exists, distinguish N/A from an invalid transfer. |
| Reflective Integration | 0.10 | Assess whether limitations, hidden assumptions, counterevidence, and revisions are integrated into the reasoning and conclusions. Merely stating “I may be wrong” or listing a limitation is insufficient if the analysis then ignores it. Counterevidence is not itself a weakness; its treatment is what matters. |

```
D2-SI = 0.40 × Internal_Structural_Coherence
      + 0.30 × Developmental_Consistency
      + 0.20 × Cross_Context_Transfer
      + 0.10 × Reflective_Integration
```

Score each applicable dimension from 0 to 4. With all four applicable, the weighted sum is already on the 0–4 scale; do not divide by 4. If a dimension is genuinely not applicable, state the reason and renormalize over applicable dimensions only:

```
D2-SI = Σ(weight_i × score_i) / Σ(weight_i for applicable dimensions)
```

Do not use N/A to hide weak performance. Report raw scores, applicability, any renormalization, and the rationale for every N/A. If no defensible dimension can be scored, report D2-SI as not scorable rather than inventing a number.

**Overlap control:** Assign an observed problem to the dimension that most directly captures it. For example, a conclusion unsupported by its premises primarily affects Internal Structural Coherence; disconnected stages or unexplained conceptual shifts affect Developmental Consistency; invalid generalization across contexts affects Cross-Context Transfer; and limitations or counterevidence acknowledged but ignored in the conclusion affect Reflective Integration. Do not penalize the same underlying error in multiple dimensions unless distinct evidence supports each penalty.

### D2-SI Behavioral Scoring Anchors (0–4)

Apply the following observable anchors independently to each D2-SI dimension. Scores must be supported by identifiable evidence in the analyzed content; writing polish, topic importance, and agreement with the author are not substitutes for structural evidence.

#### Shared scale semantics

| Score | Behavioral anchor | Interpretation |
|---:|---|---|
| 0 | Demonstrable fundamental failure in the applicable dimension; the expected structure is absent or materially invalidated. | Use only when sufficient evidence establishes failure; never use for missing information. |
| 1 | Very weak performance; limited positive evidence is outweighed by major, pervasive, or unresolved defects. | Major deficiencies dominate. |
| 2 | Partial/basic performance; the dimension is recognizably present, but material gaps or discontinuities remain. | A genuine intermediate level, not a default score. |
| 3 | Strong performance; the dimension is substantially coherent and defensible, with limited non-fundamental deficiencies. | Remaining defects do not materially undermine the dimension. |
| 4 | Very strong and integrated performance throughout the relevant content; no material unresolved defect in this dimension is evidenced. | Requires positive evidence of strong performance; absence of detected errors alone is insufficient. |

A score of 0 is not equivalent to insufficient evidence. If the dimension is applicable but cannot be assessed defensibly, use INSUFFICIENT_EVIDENCE rather than 0. A score of 4 does not claim absolute perfection; it describes performance within the scope and evidence of the assessed content.

#### Dimension-specific anchors

**Internal Structural Coherence (I) — weight 0.40**

| Score | Anchor |
|---:|---|
| 0 | A fundamental break among the problem, claims, reasoning, and conclusion, or an unresolved central contradiction invalidates the conclusion. |
| 1 | Inferential links are predominantly weak; multiple major unsupported claims or inferential jumps occur. |
| 2 | The overall argument is identifiable, but important links are incomplete and some conclusions exceed their support. |
| 3 | Problem, premises, evidence, reasoning, and conclusions are largely aligned; inferential gaps are limited and material contradictions are absent or resolved. |
| 4 | The reasoning chain is explicit and continuous; central claims have proportionate support, transitions are defensible, and conclusions remain within the evidence. |

**Developmental Consistency (D) — weight 0.30**

| Score | Anchor |
|---:|---|
| 0 | The content is fundamentally fragmented; central conceptual shifts occur without a connecting rationale. |
| 1 | Stages are mostly juxtaposed rather than developed from one another; major discontinuities are frequent. |
| 2 | Some stages connect and develop, but important parts of the argument stall or remain discontinuous. |
| 3 | Stages generally build on one another; refinements and revisions are traceable, with only limited unexplained gaps. |
| 4 | The internal progression is clear; each stage extends, sharpens, or justifiably revises prior reasoning, producing coherent argumentative development. |

This dimension concerns development within the single content item, not historical change across time.

**Cross-Context Transfer (C) — weight 0.20**

| Score | Anchor |
|---:|---|
| 0 | A central transfer is demonstrably invalid; decisive contextual differences are ignored and the main conclusion depends on it. |
| 1 | Transfers rely mainly on superficial similarities; important differences or validity conditions are not examined. |
| 2 | Some transfers have a defensible basis, but comparison, contextual differences, or limits of generalization are incompletely handled. |
| 3 | Transfers are generally valid; relevant similarities and differences are considered and generalizations mostly remain within defensible bounds. |
| 4 | Transfers have an explicit and rigorous basis; relevant equivalences and decisive differences are identified, boundary conditions are preserved, and validity limits are clear. |

The number of domains or examples is not itself evidence of transfer quality. If no meaningful transfer opportunity exists, mark N/A with a rationale; do not use N/A when an attempted transfer is weak or invalid.

**Reflective Integration (R) — weight 0.10**

| Score | Anchor |
|---:|---|
| 0 | Decisive counterevidence or limitations are ignored or distorted, while the conclusion is maintained despite the unresolved conflict. |
| 1 | Reflection is absent or largely performative; acknowledged limitations or counterevidence have no meaningful effect on the reasoning. |
| 2 | Some assumptions or limitations are identified, but their integration into reasoning and conclusions is incomplete or uneven. |
| 3 | Important limitations and counterevidence are examined and meaningfully inform qualification of some claims or conclusions; omissions are limited. |
| 4 | Assumptions, limitations, and counterevidence are actively evaluated; their effects on claim scope, confidence, and conclusions are explicit, and justified revisions are integrated. |

#### Non-score assessment states

| State | Meaning | Required handling |
|---|---|---|
| N/A | The dimension is genuinely inapplicable or no relevant assessment opportunity exists in the content. | Exclude its weight from the denominator, explain why, and renormalize across applicable dimensions. |
| INSUFFICIENT_EVIDENCE | The dimension is applicable, but available evidence is insufficient for a defensible score. | Do not assign a numeric score; identify what evidence is missing. |
| NOT_ASSESSED | The dimension has not been evaluated. | Do not treat as N/A or as zero. |
| NOT_SCORABLE | No dimension can be defensibly scored. | Do not report a numeric D2-SI. |
| 0 | Sufficient evidence demonstrates fundamental failure in that dimension. | Provide the specific supporting evidence. |

#### Evidence record and adjudication

For each dimension, record: raw score (or non-score state), applicability, specific textual evidence or location, rationale for the selected anchor, material counterevidence or defect, and evaluator confidence. When evaluators disagree, resolve the disagreement by comparing evidence and anchor interpretation; do not automatically average their scores. The final adjudicated score and its rationale must be recorded.

#### Boundary and overlap controls

A change of position is not automatically a contradiction; a reasoned revision may support Developmental Consistency. Cross-context quality is not measured by domain count. A statement of humility alone does not establish Reflective Integration. Assign each defect to the dimension that most directly captures it; apply multiple penalties only where distinct evidence establishes distinct failures. Missing information must not be converted into a score of 0.


**Scope and provenance:** This is a proposed single-input operationalization, not BIO v1.0’s canonical longitudinal subcriterion formula. It does not change D2’s official weight of 0.18. Label the result `D2-SI`; never present it as proof of longitudinal continuity, stability, persistence, or historical development. A single input can support analysis of structure and development within that content only. Missing longitudinal evidence is not itself a defect. If expressing its contribution in a 0–100 total, use `(D2-SI / 4) × 18` only if the canonical aggregate uses normalized criterion scores; this does not redefine overall BSI aggregation.

### D3 — AuthenticEthicalLayer (وزن: 0.18)

**تعریف:** D3 در معنای ریشه‌ای v3.3، اصالت لایه اخلاقی انسانی را همراه با قدرت راستی‌آزمایی، صداقت معرفتی و تعهد به حقیقت می‌سنجد. بنابراین D3 صرفاً شاخص «اخلاق‌گرایی» یا «غیراخلاقی‌نبودن» نیست و صرفاً معادل Anti-Performative نیز نیست.

D3 باید این زنجیره را بررسی کند:

**ارزش‌های اصیل و انسانی → صداقت فکری → مقاومت در برابر خودفریبی → شفافیت محدودیت‌ها → آزمون‌پذیری و امکان ابطال → راستی‌آزمایی → پذیرش نقد و اصلاح → تعهد به حقیقت**

D3 = 0.20 × Authentic_Value_Hierarchy + 0.20 × Intellectual_Honesty_Truth_Commitment + 0.15 × Anti_Self_Deception_Criticality + 0.15 × Limitation_Transparency + 0.15 × Falsifiability_Testability + 0.15 × Verification_Openness_to_Critique

| زیرشاخص | وزن | تعریف |
|---|---:|---|
| Authentic_Value_Hierarchy | 0.20 | اصالت انسانی و غیرایدئولوژیک لایه ارزش‌ها، انسجام سلسله‌مراتب ارزش‌ها و provenance آن‌ها در گفتار و عمل |
| Intellectual_Honesty_Truth_Commitment | 0.20 | صداقت فکری، ترجیح حقیقت بر حفظ موضع، و تعهد به حقیقت حتی هنگامی که برای فرد پرهزینه است |
| Anti_Self_Deception_Criticality | 0.15 | مقاومت در برابر خودفریبی، rationalization، نادیده‌گرفتن شواهد ناسازگار و توانایی نقد موضع خود |
| Limitation_Transparency | 0.15 | شفافیت درباره محدودیت‌ها، عدم‌قطعیت‌ها، نقاط کور، دامنه اعتبار و موارد ندانستن |
| Falsifiability_Testability | 0.15 | آزمون‌پذیری، امکان ابطال، مشخص‌بودن شرایط نقض و پرهیز از ادعاهای مصون از آزمون |
| Verification_Openness_to_Critique | 0.15 | راستی‌آزمایی داخلی و خارجی، dogfooding در موارد مرتبط، استفاده از شواهد مستقل، دعوت به نقد و آمادگی برای اصلاح |

**اصل مهم در محاسبه D3:** نبودِ بیان اخلاقی صریح در یک متن علمی، فنی یا تحلیلی نباید به‌تنهایی موجب امتیاز پایین D3 شود. شواهد D3 می‌تواند در رفتار معرفتی فرد، نحوه بیان عدم‌قطعیت، پذیرش محدودیت‌ها، طراحی آزمون، راستی‌آزمایی و واکنش به شواهد مخالف ظاهر شود.

در مقابل، استفاده از زبان اخلاقی، ادعای صداقت یا نمایش موضع انسان‌دوستانه بدون شواهد متناظر نباید امتیاز بالا ایجاد کند.

**مرزبندی با D7:** D3 اصالت اخلاقی، صداقت معرفتی، ضدخودفریبی، آزمون‌پذیری و راستی‌آزمایی را می‌سنجد؛ D7 مقاومت در برابر performative drift، attention optimization، engagement-driven production و audience-pleasing را می‌سنجد. هم‌پوشانی جزئی ممکن است وجود داشته باشد، اما D3 و D7 یک سازه واحد نیستند.

---

### D4 — CreativeValueAdd (وزن: 0.17)
**تعریف BIO:** آیا محتوا یک شکاف معرفتی واقعی را شناسایی کرده، با ترکیب حوزه‌ای هدفمند پر کرده، و خروجی‌ای با Generative Capacity تولید کرده است؟

```
D4 = 0.40 × Combinatorial_Synthesis
   + 0.35 × Epistemic_Gap_Targeting
   + 0.25 × Generative_Capacity
```

| زیرشاخص | وزن | لایه | سوال کلیدی |
|---|---|---|---|
| Combinatorial_Synthesis | 0.40 | Latent | آیا ترکیب ساختاری حوزه‌ها به سنتز جدید رسیده؟ |
| Epistemic_Gap_Targeting | 0.35 | Latent | آیا شکاف معرفتی واقعی و مهم هدف گرفته شده؟ |
| Generative_Capacity | 0.25 | Meta | آیا خروجی ابزار یا چارچوبی می‌سازد که دیگران با آن فکر جدید تولید کنند؟ |

**نکته BIO:** بیان هنری و استعاره‌سازی فقط در صورتی امتیاز دارد که در خدمت Generative Capacity باشد.

---

### D5 — StrategicDepth (وزن: 0.12)
**تعریف BIO:** کیفیت عمق تحلیل نسبت به حجم — کمتر اما عمیق‌تر

```
D5 = 0.30 × Mechanistic_Depth
   + 0.25 × Evidence_Quality_Density
   + 0.20 × Conditional_Reasoning_Strength
   + 0.15 × Insight_Compression_Ratio
   + 0.10 × Layered_Analysis_Quality
```

| زیرشاخص | وزن | تعریف |
|---|---|---|
| Mechanistic_Depth | 0.30 | عمق توضیح مکانیسم‌های زیرین |
| Evidence_Quality_Density | 0.25 | کیفیت و تراکم شواهد در واحد متن |
| Conditional_Reasoning_Strength | 0.20 | قدرت و انسجام استدلال شرطی |
| Insight_Compression_Ratio | 0.15 | نسبت بینش به حجم (کمتر اما عمیق‌تر) |
| Layered_Analysis_Quality | 0.10 | کیفیت تحلیل لایه‌ای |

**تمایز از D1:** D1 وجود روابط علّی را می‌سنجد؛ D5 کیفیت و تراکم تحلیل را می‌سنجد.

---

### D6 — InterdisciplinaryBreadth (وزن: 0.08)
**تعریف BIO:** گستردگی چندحوزه‌ای بدون از دست دادن دقت

```
D6 = 0.45 × BIO_Ontology_Coverage
   + 0.30 × Concept_Graph_Density
   + 0.15 × Cross_Field_Integration
   + 0.10 × Method_Diversity
```

| زیرشاخص | وزن | تعریف |
|---|---|---|
| BIO_Ontology_Coverage | 0.45 | پوشش مفاهیم در هستی‌شناسی BIO |
| Concept_Graph_Density | 0.30 | تراکم شبکه مفهومی بین حوزه‌ها |
| Cross_Field_Integration | 0.15 | ادغام واقعی (نه سطحی) بین رشته‌ها |
| Method_Diversity | 0.10 | تنوع روش‌شناختی |

**هشدار:** وزن این معیار ۸٪ است — breadth بدون depth امتیاز بالا نمی‌گیرد.

---

### D7 — AntiPerformativeDrift (وزن: 0.05)
**تعریف BIO:** اجتناب از تولید محتوای نمایشی، engagement-driven یا attention-optimized

```
D7 = 0.50 × Claim_Classification_Purity
   + 0.30 × Implicit_Assumption_Exposure
   + 0.20 × Audience_Pleasing_Detection
```

| زیرشاخص | وزن | تعریف |
|---|---|---|
| Claim_Classification_Purity | 0.50 | دقت برچسب‌گذاری FACT/INFERENCE/HYPOTHESIS/SPECULATION |
| Implicit_Assumption_Exposure | 0.30 | افشای صریح پیش‌فرض‌های پنهان |
| Audience_Pleasing_Detection | 0.20 | تشخیص و اجتناب از محتوای مخاطب‌پسند بدون عمق |

**نکته:** وزن ۵٪ عمدی است — Anti-drift یک شرط پایه است، نه مزیت رقابتی.

---

## ۵. تأیید مجموع وزن‌های زیرمعیارها

| معیار | Σ زیرمعیارها |
|---|---|
| D1 ConditionalDepth | 0.35+0.25+0.25+0.15 = **1.00** ✓ |
| D2 LongitudinalCoherence | 0.40+0.30+0.20+0.10 = **1.00** ✓ |
| D3 AuthenticEthicalLayer | 0.20+0.20+0.15+0.15+0.15+0.15 = **1.00** ✓ |
| D4 CreativeValueAdd | 0.40+0.35+0.25 = **1.00** ✓ |
| D5 StrategicDepth | 0.30+0.25+0.20+0.15+0.10 = **1.00** ✓ |
| D6 InterdisciplinaryBreadth | 0.45+0.30+0.15+0.10 = **1.00** ✓ |
| D7 AntiPerformativeDrift | 0.50+0.30+0.20 = **1.00** ✓ |
| **Σ وزن‌های اصلی** | 0.22+0.18+0.18+0.17+0.12+0.08+0.05 = **1.00** ✓ |

---

## ۶. جدول تغییرات نسبت به v3.1

| # | معیار قدیم (v3.1) | معیار جدید (BIO v1.0) | وزن قدیم | وزن جدید | تغییر |
|---|---|---|---|---|---|
| D1 | Predictive Depth | ConditionalDepth | 0.23 | **0.22** | نام + وزن |
| D2 | Longitudinal Coherence | LongitudinalCoherence | 0.19 | **0.18** | وزن |
| D3 | Ethical Verifiability | AuthenticEthicalLayer | 0.14 | **0.18↑** | نام + وزن |
| D4 | Depth Over Volume | CreativeValueAdd | 0.18 | **0.17** | نام + وزن + زیرمعیارها |
| D5 | Creative Value Add | StrategicDepth | 0.09 | **0.12↑** | نام + وزن + زیرمعیارها |
| D6 | Multidisciplinary Rigor | InterdisciplinaryBreadth | 0.10 | **0.08↓** | نام + وزن |
| D7 | Anti-Performative Resistance | AntiPerformativeDrift | 0.07 | **0.05↓** | نام + وزن |

---

## ۷. مقیاس تفسیر امتیاز نهایی

| امتیاز BSI | سطح | تفسیر |
|---|---|---|
| ۸۵–۱۰۰ | HIGH_INTEGRITY | انسجام معرفتی استثنایی |
| ۷۰–۸۴ | MODERATE_HIGH | انسجام قوی با شکاف‌های جزئی |
| ۵۵–۶۹ | MODERATE_INTEGRITY | کیفیت متوسط؛ نیاز به تقویت |
| ۴۰–۵۴ | LOW_INTEGRITY | شکاف‌های قابل توجه |
| زیر ۴۰ | CRITICAL_GAPS | ضعف ساختاری بنیادین |

---

## ۸. یادداشت پیاده‌سازی

پیاده‌سازی کد (`bsi_engine.py`) باید با این سند و BIO v1.0 هماهنگ باشد:
- نام متغیرها → نام‌های BIO
- وزن‌های `BSI_WEIGHTS` → جدول بخش ۲
- Schema خروجی API → نام‌های BIO

---

*در هر تعارض: BIO v1.0 مرجع است.*
