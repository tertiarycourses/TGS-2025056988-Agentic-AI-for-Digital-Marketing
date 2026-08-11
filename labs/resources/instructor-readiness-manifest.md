# C926 Instructor Readiness Manifest

Complete this checklist before class. Record resource names and PASS evidence in the trainer's private delivery record, not in the public repository.

| Area | Ready when | Minimum role and scope | Rejoin path and exact learner command |
|---|---|---|---|
| Microsoft Foundry project | Learners can read deployments, call the selected language model and view their traces | **Foundry User** on the learner project plus **Reader** on the Foundry resource; use **Foundry Agent Consumer** only for principals that solely invoke published agents | `Copy-Item ..\labs\resources\foundry-verifier-rejoin.json evidence\foundry-verifier-rejoin.json` and run all script self-checks |
| Language deployment | Stable deployment name is confirmed and quota supports the cohort | Instructor owns deployment; learners use it through the project-scoped Foundry role | Use offline retrieval, schema and routing modes |
| Image generation | Approved image model is deployed in a supported region | Foundry project access appropriate to the playground or approved image tool | `Copy-Item ..\labs\resources\rejoin-generated-device-desk.svg work\generated-device-desk.svg` |
| Multimodal understanding | A multimodal model or Content Understanding image analyzer is callable | Same project scope as the selected model or tool | `Copy-Item ..\labs\resources\multimodal-analysis-rejoin.json evidence\multimodal-analysis.json` |
| Speech | WAV input, locale and learner access are tested | Instructor supplies an ephemeral training key privately when keyless access is unavailable | `Copy-Item ..\labs\resources\speech-rejoin-result.json evidence\speech-result.json`; source transcript is `northstar-call-transcript.txt` |
| Translator | Target locale, endpoint and training access are tested | Instructor supplies an ephemeral training key privately when keyless access is unavailable | Copy `translation-review-template.csv` into `work\` and perform the design/review path with supplied text |
| Content Understanding | Foundry resource endpoint is tested; `gpt-4.1` and `text-embedding-3-large` deployments are mapped to their default names for `prebuilt-invoice` | **Cognitive Services User** on the Foundry resource for the learner Entra principal, or an instructor-supplied ephemeral training key; keys never enter shared evidence | `Copy-Item ..\labs\resources\content-understanding-invoice-rejoin.json evidence\invoice-result-sanitized.json` |
| Azure AI Search | Prepared index, integrated vectorizer, semantic configuration and learner query role are tested | **Search Index Data Reader** on the prepared index or search-service scope for learner queries; instructor separately holds the roles needed to manage the index | Copy `search-keyword-rejoin.json`, `search-vector-rejoin.json`, `search-hybrid-rejoin.json` and `search-unsupported-rejoin.json` to the matching `evidence\search-*.json` files; use `search-documents.json` for offline filter checks |
| Observability | Traces appear within the project and sensitive-data settings are understood | Foundry project access plus **Reader** on the connected Application Insights resource when the trace view requires it | Use local transcript timestamps and the copied error-analysis template |
| Evaluation | Available quality and safety evaluators are confirmed for the region | Same Foundry project scope as the evaluation run | Use the documented manual rubric with the same criteria |

## Security readiness

- Use synthetic Northstar data only.
- Prefer Entra identities and least-privilege roles.
- Keep unavoidable training keys in environment variables or an approved secret channel.
- Do not ask learners to copy bearer tokens, connection strings or raw trace payloads into shared files.
- Remove or rotate temporary training access after delivery.
- Verify `requirements-lock.txt` in a clean Python 3.12 environment before each delivery; update the lock only after all self-checks and lab commands pass. `requirements.txt` lists the direct package set.
