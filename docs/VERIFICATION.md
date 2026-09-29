# VERIFICATION.md — Z.ai Field Guide claim audit

Verification run: **2026-09-29** · Scope: all 46 content files (`content/` EN ×23, `content/zh/` ZH ×23)
· Method: page-by-page claim extraction → verification against the source-authority order
(official docs / model cards / repositories → named trade press → labeled community), fixes applied to EN+ZH,
sources re-audited (every URL opened; see appendix).

**Legend.** CONFIRMED = text left as-is with source present · CORRECTED = text fixed (and reason logged)
· UNVERIFIED = not supportable by primary or reputable sources (cut or explicitly carried as unverified)
· Attribution = vendor-only claims kept with in-text attribution.

**Summary.**

- Pages checked: **23 EN + 23 ZH** (46 files; all read in full).
- Checkable claims logged: **~270** across both editions.
- Corrections applied: **14 clusters** (dates, numbers, links, product naming) — all in EN **and** ZH.
- Verdict counts (claim level): ~250 CONFIRMED · 14 CORRECTED · 0 WRONG-left-standing · 5 UNVERIFIED/soft (listed at the end).
- Build: `make build` (73 pages, 0 warnings) and `make check` (0 errors, 0 warnings) clean after fixes.
- Out of scope by brief: `templates/`, `config.yaml`*, `assets/`, build tooling, `README.md`* — untouched.
  (*Both still carry the old "code.z.ai" phrasing in their page descriptions; flagged for the owner, not edited.)

**The single biggest find:** the site repeatedly referenced **`code.z.ai` as a product surface. No such
domain exists** (NXDOMAIN across resolvers; absent from every Z.ai document). The real surfaces are
`z.ai/subscribe` (the GLM Coding Plan page) and `zcode.z.ai` (ZCode). Fixed everywhere in content.

---

## Per-page log (EN; ZH mirrors tracked alongside and fixed identically)

### content/index.md — home
| Claim | Verdict | Source | Action |
|---|---|---|---|
| "first listed large-model company in January 2026" | CONFIRMED | STCN / BAAI / pedaily ("全球大模型第一股") | none |
| "publishing GLM models since 2022" | CONFIRMED | GLM-130B Aug 2022 | none |
| chat.z.ai + code.z.ai as the two doors | **CORRECTED** | code.z.ai NXDOMAIN; z.ai/subscribe is the plan page | "code.z.ai" → "the GLM Coding Plan" (3 spots) |
| GLM-5.3 bullets (50% gain, TB 3.0, custom license) | CONFIRMED | docs.z.ai release notes 2026-08-18; HF card | none |
| GLM-5.3-Flash bullets (320B/18B, MIT, 1/10 price) | CONFIRMED | release notes 2026-08-26; HF card | none |
| "18 USD per month… more than twenty agent harnesses" | CONFIRMED | devpack overview; tracker counts; docs tool list | none |
| History recap (2019 spin-out / GLM-130B / ChatGLM / GLM-4.5) | CONFIRMED | see history pages | none |

### content/api/index.md — developer platform
| Claim | Verdict | Source | Action |
|---|---|---|---|
| OpenAI-compatible; Python & Java SDKs; LangChain; OpenAPI | CONFIRMED | docs.z.ai llms.txt + SDK pages + /openapi.json | none |
| Streaming / tool streaming / function calling / structured output / context caching | CONFIRMED | docs nav + guides | none |
| Full price table (12 rows incl. FlashX, 4.7, 4.5-Air, 4.6V, OCR, free tiers) | CONFIRMED | docs.z.ai pricing (fetched 2026-09-29) | none |
| GLM-Image $0.015 · CogVideoX-3 $0.20 · ASR ≈$0.0024/min | CONFIRMED | pricing page | none |
| Slide/Poster agent $0.70/MTok; translation; video templates; web reader; tokenizer + rate-limit endpoints | CONFIRMED | pricing; agent docs; llms.txt | none |

### content/chat/index.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| chat.z.ai default engine GLM-5.3-Flash since Aug 2026 | CONFIRMED | z.ai homepage ("powered by GLM-5.3-Flash"); release notes | none |
| Slide agent = retrieval + structuring + layout | CONFIRMED | release notes 2025-08-08 | none |
| PPTX/PDF/DOCX/XLSX deliverables | CONFIRMED | GLM-5.3-Flash guide | none |
| Web search $0.01/use | CONFIRMED | pricing | none |
| 320B/18B, MIT, $0.15/M input | CONFIRMED | model card | none |

### content/code/index.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| code.z.ai sells coding | **CORRECTED** | domain does not exist | rewritten around the GLM Coding Plan |
| Tiers: Lite 2,000/10,000 · Pro 12,000/60,000 · Max 28,000/140,000 | CONFIRMED | devpack overview | none |
| From $18; trackers ≈$80/$168; discounts 12.60/50.40/112 | CONFIRMED as tracker-recorded (see caveat below) | zentor, techtrendery, rankllms | added live-page link `z.ai/subscribe` |
| Multipliers 24 / 8; rolling 5-hour & 7-day pools | CONFIRMED | devpack overview | none |
| Claude Code/Cline/OpenCode/Kilo Code/Clawdbot-OpenClaw named; 20+ tools per trackers | CONFIRMED | docs.z.ai llms.txt; tool page (20 cards); zentor | none |
| September campaign (Sep 3–Oct 7, 23:00–09:00, ZCode+AutoClaw unlimited, doubled elsewhere) | CONFIRMED | campaign notice | none |
| ZCode: first-party harness; 7,000+ stars; plugin marketplace | CONFIRMED | repo (created 2026-09-20; 7,149★); zcode-plugins repo | descriptor fixed: "terminal agent" → "multi-agent coding workbench" |
| Team Plan: seats, insights, budget controls | CONFIRMED | teamplan page | none |
| AutoGLM-Phone-Multilingual Dec 2025; ADB; 50+ apps | CONFIRMED | release notes 2025-12-11 | none |

### content/company/index.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Founded June 2019; KEG spin-out; Beijing | CONFIRMED | prospectus coverage; report filings | none |
| Leadership trio (Tang Jie / Zhang Peng / Liu Debing roles & backgrounds) | CONFIRMED | press; "智谱三杰" features | none |
| >8 rounds; >8.3B yuan; 87 shareholders; Meituan/Ant/Alibaba/Tencent/Xiaomi | CONFIRMED | 36kr/ebrun 2026-01-18 ("合计共87家股东"); BAAI | none |
| Listing: code 2513; HK$116.2; ≈HK$4.3B; 11 cornerstones; 1,164x | as final figure **CORRECTED** → 1,159.46x | 21jingji 2026-01-08 allotment; chiefgroup data | text fixed; source added |
| First-day mcap >HK$51B; +300%+ by mid-Feb (≈HK$485); mcap >HK$200B | CONFIRMED | STCN ("涨超300%", HK$485.0); nbd.com.cn | wording tuned ("up more than 300%") |
| STAR: Jun 1 board; Jun 17 accepted; Guotai Haitong + CICC; ≈RMB 15B | CONFIRMED (stage wording clarified) | 21jingji; sfccn; stcn | "Coaching accepted" → "Coaching acceptance" |
| 2025 loss ≈4.7B yuan | CONFIRMED | press coverage | none |
| Qingyan 25M users; revenue +100% YoY | CONFIRMED | qbitai/36kr/oeeee | none |

### content/company/open-source.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Star table (ChatGLM-6B 40.9k → GLM-4-Voice 3.2k; slime 8.6k; AgentBench 3.8k) | CONFIRMED | GitHub API 2026-09-29 | none |
| "GLM-TTS, GLM-ASR, GLM-Image … 1.0k+ each" | **CORRECTED** | GLM-ASR = 855★ | → "1.1k / 0.9k / 1.1k" |
| "P-tuning line that predates the company itself" | **CORRECTED** | P-tuning is 2021; company 2019 | clause removed |
| License arc (MIT → custom "glm-5.3"; Flash MIT) | CONFIRMED | HF license fields; LICENSE text | none |
| $10B MaaS security-review provision (community reporting) | CONFIRMED | LICENSE §2 | none |
| Community license discussion attribution | **CORRECTED** | The New Stack piece verified; "ThursdAI" could not be located | TNS linked; ThursdAI dropped |

### content/ecosystem/index.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Official tool list incl. Clawdbot/OpenClaw + ZCode | CONFIRMED | llms.txt; tool page | none |
| ZCode "first-party terminal agent" + 7k stars + marketplace | **CORRECTED** descriptor | repo/README (desktop+browser+terminal) | → "first-party coding harness" |
| MCP bundles (vision/web search/web reader/Zread) | CONFIRMED | devpack overview | none |
| Providers: Together, Novita, DeepInfra, Featherless | CONFIRMED | HF model pages (inference-provider lists) | none |
| GLM-5 trained entirely on Huawei Ascend; GLM-Image on domestic chips | CONFIRMED | multiple independent analyses; release notes | none |
| Competitive frame (Qwen3.7-Max, MiniMax M3, DeepSeek-V4-Pro, Opus 4.8, GPT-5.5, Gemini 3.1 Pro) | CONFIRMED | GLM-5.2 card | none |

### content/history/index.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Four-era structure + dates (2019→2026) | CONFIRMED | era pages | none |
| "first listed large-model company" | CONFIRMED | press | none |

### content/history/origins.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| KEG parent; ~"three decades" framing; GLM lineage | CONFIRMED | company framing via press | none |
| Tang Jie: Tsinghua professor; ACM/IEEE Fellow | CONFIRMED | tsinghua.edu.cn; Baike (also AAAI) | none |
| Tang Jie "roughly 13 percent stake in the early years" | **CORRECTED** | filings show 7.4081% direct (2025), ≈6.1% at IPO; no 13% source found | → "a direct stake of roughly seven percent ahead of the listing" |
| "Zhipu's three heroes" nickname | CONFIRMED | Caixin Weekly 2026-07; 163.com | none |
| Incorporated June 2019 as KEG spin-out | CONFIRMED | prospectus coverage | none |
| GLM-130B Aug 2022; ICLR 2023 | CONFIRMED | repo; paper | none |
| >8 rounds / 87 shareholders / "5B yuan pre-2023" phrasing | **CORRECTED** phrasing | sources support ≥8 rounds & >83亿 total; the "5B pre-2023" figure was unsupportable | → "over 8.3 billion yuan raised in total" (both editions) |
| Lao Hu Caijing link | **CORRECTED** | m.laohucaijing.com dead | → www.laohucaijing.com |

> Note on the origins fix: the same sentence has been harmonized with the company page's audited
> figures (≥8 rounds, >8.3B yuan, 87 shareholders) so the two pages no longer disagree.

### content/history/chatglm-era.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| "Six weeks after ChatGPT's launch" | **CORRECTED** | ChatGLM-6B released 2023-03-14 (GPT-4 day); ChatGPT 2022-11-30 | → "Three and a half months after ChatGPT's launch, on the day GPT-4 was announced" |
| >10M downloads; single-GPU 6B | CONFIRMED | press retrospectives; eeo/tencent cloud | none |
| 2.5B+ yuan in 2023; investors incl. Meituan/Ant/Alibaba/Tencent/Xiaomi; ~7× valuation by Oct 2023 | CONFIRMED | Wikipedia; guancha; Forbes CN | none |
| "three more rounds through 2024" | CONFIRMED (≥4 per some sources; "three" is within range) | cs.com.cn ("至少4轮"); keep as-is with sources | none |
| ≈20B-yuan "super unicorn" by Sept 2024 | CONFIRMED | 36kr; 21jingji | none |
| Qingyan 25M users; revenue +100%+ | CONFIRMED | press | none |
| GLM-4 DevDay Jan 16, 2024 | CONFIRMED | Tencent News; press | none |
| "September's KDD announcements" | **CORRECTED** | KDD 2024 ran Aug 25–29; announcements Aug 29 | → "August's KDD announcements" |
| Yemacaijing link | **CORRECTED** | a.yemacaijing.com dead | → www.yemacaijing.com |

### content/history/pivot.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| GLM-4.5/4.5-Air Jul 28, 2025; "ARC"; doubled efficiency; Claude Code compat | CONFIRMED | release notes; GLM-4.5 repo | none |
| Z.ai rebrand same week | CONFIRMED | Wikipedia; CNBC | none |
| …"and later code.z.ai" | **CORRECTED** | domain NXDOMAIN | → "and later the GLM Coding Plan" |
| GLM-4.5V Aug 11; Slide agent Aug 8; GLM-4.6 Sep 30; GLM-4.6V Dec 8; GLM-4.7 Dec 22 | CONFIRMED | release notes | none |
| "A reported three-billion-yuan round arrived in 2025" | **CORRECTED** | 30亿 round closed Dec 2024; Mar 2025 round was >10亿 | sentence corrected to both events |
| Developer platform "millions of registered users"; listing "imminent" late 2025 | CONFIRMED (prospectus: 45M developers; Dec 2025 IPO launch) | cls.cn; sina | none |

### content/history/engineering-era.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Listing Jan 8, 2026; 2513; HK$116.2; ≈HK$4.3B; 11 cornerstones; 1,164x | oversubscription **CORRECTED** → 1,159.46x | 21jingji allotment; chiefgroup | text fixed; source added |
| First-day mcap >HK$51B | CONFIRMED | BAAI; STCN | none |
| +300%+ mid-Feb; loss ≈4.7B (2025) | CONFIRMED | STCN; nbd; press | none |
| GLM-5 Feb / 5.1 Apr / 5.2 Jun; 744B; Ascend; 8-hour; 1M context | CONFIRMED | release notes; cards | none |
| STAR: Jun 1 board; "regulators had accepted the IPO coaching filing" | **CORRECTED** | status moved to 辅导验收 (Apr-incubation: filed Jun 6; acceptance Jun 17) | → "the IPO coaching status had moved to the acceptance stage" |
| ≈RMB 15B target; "A+H" | CONFIRMED | 21jingji; sina | none |

### content/la-famille/* and content/meta/about.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| la-famille repo live; build stats ("<1s", "50+ output files", 3 artworks, 2 fonts) | CONFIRMED | repo check; local build (45 ms, 73 pages); assets listing | none |
| Method notes; four myths (lineage, rebrand, license arc, open weights ≠ open source) | CONFIRMED | cross-checked against the pages above | none |
| raw-sample (render:false demo) | CONFIRMED (build output serves it) | build | none |

### content/models/index.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Flagship table (5.3 / 5.3-Flash / 5.2 / 5.1 / 5) | CONFIRMED | cards; pricing | none |
| Full chronology 2022→2026 | CONFIRMED | release notes; repos | one span fixed (below) |
| "Jun-Sep 2024" span for 9B/9B-V/4-Plus | **CORRECTED** | KDD items are August | → "Jun-Aug 2024" |
| Cadence & license-arc summaries | CONFIRMED | as logged | none |

### content/models/earlier.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| GLM-130B details (130B, bilingual, ICLR 2023) | CONFIRMED | repo; paper | none |
| ChatGLM-6B "released … weeks after ChatGPT-mania began" | **CORRECTED** (tightened) | Mar 14, 2023 | → "in March 2023, on the day GPT-4 was announced" |
| GLM-4 Jan 16, 2024; dual-track strategy | CONFIRMED | press | none |
| Jun 2024 9B opens; "September 2024: at KDD" | **CORRECTED** | KDD = Aug 2024 | → "August 2024" |
| Modality shelf (CodeGeeX 2022/KDD 2023; CogVLM 2023; CogView; CogVideo; GLM-4-Voice) | CONFIRMED | repos; press | none |
| CogVideoX "July 2024" | CONFIRMED (announced Jul 26, 2024; open-sourced Aug 6) | press | none |

### content/models/glm-4-x-era.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| GLM-4.5/4.5-Air Jul 28; 355B/32B; ARC; Claude Code | CONFIRMED | card; notes | none |
| GLM-4.5V Aug 11 (100B; video/grounding/GUI) | CONFIRMED | release notes | none |
| GLM-4.6 Sep 30; "leading coding in China"; 355B; MIT | CONFIRMED | release notes; card; independent summaries | none |
| GLM-4.6V Dec 8 (128K) | CONFIRMED | release notes | none |
| GLM-4.7 Dec 22; SWE-bench Verified 73.8; Flash Jan 19; FlashX | CONFIRMED | card; release notes; pricing | none |

### content/models/glm-5-family.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| GLM-5: 744B/40B; 28.5T tokens; DSA; vs Opus 4.5; MIT; paper title | CONFIRMED | card; arXiv 2602.15763 | none |
| HF community ranked it #1 open-weight on Artificial Analysis | CONFIRMED | HF blog (mlabonne) | none |
| GLM-5.1: Apr 7; 8-hour; Opus 4.6 alignment; SWE-bench Pro 58.4; TB2.0 63.5 | CONFIRMED | release notes; card | none |
| GLM-5.2: Jun 16; 1M; IndexShare 2.9×; MTP +20%; "Pure Open"; 62.1 / 81.0 / 82.7 | CONFIRMED | card | none |
| Huawei-training reports attribution | CONFIRMED (multiple independent analyses) | press cluster | none |

### content/models/glm-5-3.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| Post-training-only over GLM-5.2 base | CONFIRMED | notes; card; InferenceX | none |
| +50% Z.ai Code Bench; TB3.0 & ALE SOTA; CyberGym best; 2,436/1,097 | CONFIRMED | notes; guide | none |
| Spec sheet (text-only; 1M; 128K; low/high/max; prices; weights published) | CONFIRMED | guide; card; HF file list | none |
| `thinking.type: disabled` migration constraint | CONFIRMED | guide | none |
| License: custom "glm-5.3"; $10B MaaS review; Flash stayed MIT | CONFIRMED | LICENSE §2 | none |
| "matches Mythos 5 … covered critically by trade press" | CONFIRMED | AI News analysis | none |
| Sources: TNS license discussion | **CORRECTED** (linked) | thenewstack.io/zai-glm-weights-license/ | link added; "ThursdAI roundups" dropped |

### content/models/glm-5-3-flash.md
| Claim | Verdict | Source | Action |
|---|---|---|---|
| First native multimodal GLM-5; 320B/18B; hybrid attention; 3.01×/4.44×; mHC; 30T; fresh base | CONFIRMED | cards; guide | none |
| PPTX/PDF/DOCX/XLSX; Blender; BUA/CUA | CONFIRMED | guide | none |
| Beats 5.2 "at one-tenth the price"; "approaching Opus 4.8"; DeepSWE 63.4; AutomationBench 48.8 | CONFIRMED | card; guide | none |
| TB2.1 84.3 "(mini-swe-agent harness, 400K context)" | **CORRECTED** | TB2.1 evaluated in Claude Code 2.1.207; mini-swe is DeepSWE's | → "(Claude Code harness)" |
| Price $0.15/$0.03/$0.50; FlashX 200 tok/s $0.37/$1.25 | CONFIRMED | pricing | none |
| ox-alpha story | CONFIRMED | guide; press | none |
| "3× quota" on the coding plan; overnight campaign | CONFIRMED | guide; campaign notice | none |

---

## Corrections summary (EN + ZH both fixed)

1. **code.z.ai (fictional surface)** — index, code, pivot, company (EN+ZH). Replaced with "GLM Coding Plan" / linked `z.ai/subscribe`.
2. **ChatGLM-6B timing** — "six weeks after ChatGPT" → March 14, 2023 (GPT-4 announcement day, ~3.5 months later).
3. **GLM-5.3-Flash TB2.1 harness** — "(mini-swe-agent, 400K)" → "(Claude Code harness)".
4. **P-tuning "predates the company"** — clause removed (P-tuning 2021 vs company 2019).
5. **GLM-ASR star count** — "1.0k+" → 0.9k (855★).
6. **KDD month** — "September" → August (KDD 2024 ran Aug 25–29); timeline span "Jun-Sep" → "Jun-Aug".
7. **Dead links** — m.laohucaijing.com → www.laohucaijing.com; a.yemacaijing.com → www.yemacaijing.com.
8. **Oversubscription** — market-talk 1,164x → final allotment 1,159.46x; allotment source added.
9. **STAR coaching stage** — "accepted the filing" → "status moved to the acceptance stage" (辅导验收).
10. **2025 funding sentence** — 30亿元 round is Dec 2024; March 2025 was the >10亿 round.
11. **Tang Jie stake** — "roughly 13% in the early years" → "a direct stake of roughly seven percent ahead of the listing".
12. **ZCode descriptor** — "terminal agent" → "multi-agent coding workbench" (EN+ZH).
13. **Source hygiene** — The New Stack license piece linked; ThursdAI (unverifiable) dropped; live pricing page linked.
14. **Origins funding phrase** — "over 5 billion yuan raised pre-2023 alone" (unsupportable) → "over 8.3 billion yuan raised in total" (harmonized with the audited totals; ZH gained the amount for parity).

## What remains unverifiable / soft spots (honest list)

- **Tracker price spread**: third-party trackers disagree on plan list prices (≈$72–80 for Pro, ≈$160–168 for Max;
  discounted monthly equivalents 12.60/50.40–56/112–117.60). The page keeps the tracker-recorded figures with
  attribution and points at the live pricing page; Z.ai's own migration notice separately lists $72/$160 monthly.
- **Community items**: `latent.space` (2026-08-22) and `smol.ai` (2026-08-24) are cited as aggregate community
  framing; individual posts were not itemized. Both were kept as labeled community citations only.
- **"Towards AI"** in the Huawei-training cluster: kept only as part of "multiple independent analyses" (that
  plural claim is verified; the specific outlet was not individually located).
- Several Chinese press citations are domain-level (Sina Finance, 163.com, Ebrun homepage) rather than deep links —
  retained per minimal-diff rule; the underlying facts were verified via the articles found on those sites.
- `config.yaml` and `README.md` descriptions still say "code.z.ai" — untouched by this audit's scope; fix flagged
  to the owner.

---

## Appendix — URL audit

All Sources-section URLs were hit with an HTTP client (browser UA). Results (2026-09-29):

- **200 OK**: z.ai, docs.z.ai (release notes, pricing, devpack overview/teamplan/notice, guides, llms.txt,
  api-reference), chat.z.ai, zcode.z.ai, z.ai/subscribe, huggingface.co model cards (5.3/5.3-Flash/5.2/5.1/5/4.7),
  arxiv.org/abs/2602.15763, github.com/zai-org/* (all linked repos + org), github.com/THUDM,
  github.com/drawmeanelephant/la-famille, en.wikipedia.org/wiki/Z.ai, stcn.com article, hub.baai.ac.cn article,
  news.pedaily.cn article, 21jingji.com article(s), rankllms.com, techtrenderyusa.com, zentor.ai,
  inferencex.semianalysis.com/model/glm-5-3, ebrun/sina/163/forbes/tmtpost/10jqka/pconline/qq/guancha homepages.
- **Bot-blocked but alive** (kept): artificialintelligence-news.com article (403 to curl; live via alternate UA).
- **Dead, fixed**: m.laohucaijing.com, a.yemacaijing.com (replaced with working domains).
- **NXDOMAIN (the finding)**: code.z.ai.
