# دستورالعمل اجرایی نحوه ارائه تحلیل
# Standard Operating Procedure - Output Format & Presentation

**نسخه / Version:** ۱.۱
**تاریخ / Date:** ۴ ژوئن ۲۰۲۶
**وضعیت / Status:** الزامی — همه سطوح | Mandatory — All Levels
**مرجع / Reference:** Methodology v1.1 + SOP v3.4.2 + Guardrails v1.2
**تغییرات نسبت به v1.0:**
- به‌روزرسانی ارجاع از SOP v3.2 به SOP v3.4.2
- اضافه شدن Core Claim به ابتدای ساختار خروجی
- هماهنگی وزن‌ها با BIO v1.0
- اضافه شدن EIG Score به ساختار خروجی

---

## هدف / Purpose

این سند دستورالعمل اجرایی دقیق و الزامی برای **نحوه ارائه
و ساختار خروجی** تمام تحلیل‌های شاخص بهمنش است.

**This document defines the mandatory output format and
presentation standard for all Behmanesh Index analyses.**

---

## پیش‌نیازهای الزامی قبل از هر تحلیل

1. مطالعه کامل **Methodology.md** (نسخه ۱.۱)
2. مطالعه دقیق **SOP_Intellectual_Content_Analysis_v3.4.2.md**
3. مطالعه **LLM-Execution-Guardrails_v1.2.md**
4. استفاده از **BEHMANESH_INDEX_PROMPT_v3.4.md** به‌عنوان System Prompt
5. راستی‌آزمایی محتوا با شواهد خارجی

---

## ساختار خروجی الزامی
## Mandatory Output Structure

---

### ۰. Core Claim (جدید در v1.1 — اجباری)

**شاخص بهمنش (نسخه ۳.۴.۱) — ارزیابی [نام کاربری / موضوع / صفحه]**

```
Core Claim: [یک جمله واحد — ادعای مرکزی نویسنده/متن]
```

اگر Core Claim قابل استخراج نیست:
```
Core Claim: [متن/حساب فاقد ادعای مرکزی مشخص است — دلیل: ...]
```

---

### ۱. خلاصه اجرایی / Executive Summary

- حداکثر ۱۵۰-۲۰۰ کلمه
- شامل: نمره کلی، EIG Score، نقاط قوت کلیدی، ضعف‌ها، نتیجه نهایی

---

### ۲. سطوح تحلیل (لایه‌برداری سه‌گانه)

**سطح ۱ — Manifest:**
موضوعات، فعالیت‌ها، سبک محتوا، ادعاهای صریح

**سطح ۲ — Latent:**
پیش‌فرض‌های پنهان (خروجی Assumption Excavation Protocol)،
مکانیسم‌های پنهان، Feedback Loops، Blind Spots،
تناقض‌های درونی و بیرونی

**سطح ۳ — Meta:**
EIG Score و الگوی غالب، جهان‌بینی، خودآگاهی،
جایگاه در اکوسیستم فکری، تکامل Longitudinal

---

### ۳. تم‌ها و الگوهای محوری

- لیست ۴-۷ تم اصلی با رتبه‌بندی
- مثال مستقیم از محتوا برای هر تم
- ارتباط هر تم با Core Claim

---

### ۴. EIG Analysis (جدید در v1.1 — اجباری در سطح ۲ و ۳)

| فاصله | امتیاز (۰-۱۰) | الگو |
|-------|--------------|------|
| Method-Conclusion Gap (۳۰٪) | | |
| Claim-Evidence Gap (۳۵٪) | | |
| Framing-Content Gap (۱۵٪) | | |
| Longitudinal Consistency Gap (۲۰٪) | | E/R/? |

**EIG Score:** .../۱۰۰
**الگوی غالب:** [یکی از پنج الگو]
**منشأ فاصله (اجباری اگر Score < 70):** ناتوانی / محدودیت / آگاهانه

---

### ۵. ارزیابی ۷ معیار اصلی

| معیار | وزن | امتیاز | توضیح |
|-------|-----|--------|-------|
| عمق شرطی و پیش‌بینی‌کننده واقعی | ۲۲٪ | .../۱۰۰ | |
| تداوم ارجاعی و انسجام بلندمدت | ۱۸٪ | .../۱۰۰ | |
| لایه اخلاقی اصیل + راستی‌آزمایی | ۱۸٪ | .../۱۰۰ | |
| خلاقیت + ارزش افزوده + استعاره‌سازی | ۱۷٪ | .../۱۰۰ | |
| استراتژی «کمتر اما عمیق‌تر» | ۱۲٪ | .../۱۰۰ | |
| گستردگی چندحوزه‌ای | ۸٪ | .../۱۰۰ | |
| اجتناب از performative drift | ۵٪ | .../۱۰۰ | |

**امتیاز کل:** .../۱۰۰
**نتیجه نهایی:** عالی / خیلی خوب / خوب / متوسط / ضعیف

---

### ۶. مقایسه زمانی / Temporal Comparison

- بلندمدت — Long-term
- متوسط‌مدت — Mid-term
- کوتاه‌مدت — Short-term

> **DEPRECATED:** The former 60%/25%/15% temporal weighting scheme is not part of the canonical BSI scoring architecture. These horizons are analytical views over the evidence universe and MUST NOT be treated as independent weighting layers or mutually exclusive partitions.
---

### ۷. Uncertainty Report

**نتایج با اطمینان بالا [FACT]:**
...

**نتایج با اطمینان متوسط [INFERENCE]:**
...

**سوالات بی‌پاسخ (نیازمند داده بیشتر):**
...

---

### ۸. الگوهای قابل پیش‌بینی

- روندهای آینده فکری و رفتاری
- نقاط قوت و ریسک‌های احتمالی

---

### ۹. چک‌لیست نهایی (اجباری)

- [ ] Rule #0 رعایت شد — Core Claim استخراج شده
- [ ] راستی‌آزمایی انجام شد
- [ ] بی‌طرفی و سخت‌گیری منصفانه رعایت شد
- [ ] لایه‌برداری سه‌گانه کامل است
- [ ] Assumption Excavation Protocol اجرا شد (سطح ۲ و ۳)
- [ ] EIG Module اجرا شد (سطح ۲ و ۳)
- [ ] ~~وزن زمانی رعایت شده (حداقل ۶۰٪ بلندمدت)~~ **DEPRECATED — legacy 60% rule; do not apply to current BSI scoring**
- [ ] مثال‌های مستقیم آورده شده
- [ ] رویکرد واقع‌گرایانه-مکانیسمی حفظ شده
- [ ] برچسب‌گذاری FACT/INFERENCE/HYPOTHESIS/SPECULATION کامل است

---

## نکات مهم

- زبان اصلی فارسی روان و حرفه‌ای است. انگلیسی برای دسترسی
  بین‌المللی اضافه شده است.
- از اغراق، تمجید بدون سند و جانبداری پرهیز شود.
- هر تحلیلی که این ساختار را کامل رعایت نکند، خارج از
  استاندارد رسمی شاخص بهمنش محسوب می‌شود.

**Any analysis that does not fully comply with this structure
is considered non-compliant with the official Behmanesh Index standard.**
