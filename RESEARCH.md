# Human Rights Supply Chain Statement Consistency Gate

## STUDIO DEV RESEARCH UPDATE — 2026-09-27
- **Technical slug/class:** `human-rights-supply-chain-statement-consistency-gate`.
- **Network boundary:** Studio Dev only, using the current documented GenLayer CLI/SDK and current Intelligent Contract API. No legacy network, chain, RPC, private key, deployment, broadcast, or Studio test is part of this research.
- **Studio Dev feasibility verdict:** REVISE. The temporal alignment gate is suitable for a Studio Dev build only after a CLI HTML-fetch probe; the current source pair intentionally proves LATER_REVISION rather than same-period alignment.
- **External-source rule:** only the named allowlisted official domains may be fetched; redirects, blocked pages, source drift, parser ambiguity, validator disagreement, or missing authoritative fields produce `UNRESOLVED` and do not create a favorable state.
- **Build handoff condition:** AI chính may start Stage 3 only after confirming current CLI/API compatibility, storage and nondeterministic-call syntax, Equivalence Principle behavior, and a bounded Studio Dev HTML/PDF/source-access probe. Research evidence is not deployment or E2E evidence.

## STAGE 1

- **Objective/users:** Check whether a public supplier-code revision may validly be treated as contemporaneous support for commitments in one organization's signed modern-slavery statement. Procurement registries consume a bounded publication-alignment signal; no misconduct or supplier-behavior finding.
- **Trust problem / GenLayer:** documents may use different terminology and one publisher may selectively summarize them. Independent validators should agree before a contradiction signal affects onboarding.
- **Mechanism/actors/evidence:** organization owner seals exact identity, statement period, statement signature date, supplier-code publication/update date, and two official URLs/hashes; assessor returns `identity_match`, `statement_period_match`, `code_date_state`, `code_promised_for_later_statement`, bounded commitment-overlap mask, and `ALIGNED/LATER_REVISION/UNRESOLVED`. A later code may confirm topic continuity but cannot prove same-period consistency.
- **Concrete public source set, checked 2026-09-21:** [DHSC's modern-slavery statement](https://www.gov.uk/government/organisations/department-of-health-and-social-care/about/modern-slavery-statement) identifies DHSC, covers 2020-04-01 through 2021-03-31, was approved/signed in October 2021, and says a health-family-wide supplier code was being developed for reference in the next statement. The [DHSC supplier code](https://www.gov.uk/government/publications/dhsc-supplier-code-of-conduct/dhsc-supplier-code-of-conduct) identifies DHSC, is marked updated 2025-03-28, and includes human-rights/modern-slavery requirements. The real fixture must therefore output `LATER_REVISION`, not `ALIGNED` or `CONTRADICTORY`. Counterexamples are a Cabinet Office code misidentified as DHSC or omission of the 2025 update date; both yield `UNRESOLVED`.
- **Validator:** leader and validators independently refetch/extract full masks; exact-match consequential tuple; deterministic aggregate.
- **Closest:** Research Conflict Disclosure Consistency Registry and App Privacy Declaration Consistency Registry. Inherited: cross-publication consistency masks. Material difference: compares a governance commitment chain across statement, procurement policy, and supplier code with reporting-period binding; it is not source-to-source disclosure taxonomy parity. Difference medium-high; new value is a reusable procurement intake gate.
- **Risks/feasibility:** cannot detect undisclosed conduct and cannot prove historical consistency. MVP intentionally supports the evidenced negative temporal result; exact retrieval hashes bind drift. Both sources are public HTML; current GenVM access remains a later build-stage check.
- **Stage 1 acceptance:** explicit safe claim, independent sources, material multi-document mechanism, closed downstream signal, no name collision.

## STAGE 2

- **Model/lifecycle:** `OrganizationProfile`, `StatementPeriod`, `Manifest`, `Assessment`; `REGISTERED -> SEALED -> ASSESSED -> REASSESSED | SUPERSEDED`.
- **Invariants/storage:** exact organization, statement period/signature date, and code update date; exactly two DHSC HTML origins; `ALIGNED` requires a defensible code revision within the sealed statement period, while any later dated revision deterministically yields `LATER_REVISION`; new period is a new record; append-only results.
- **API/auth:** `register_profile`, `seal_period_and_code`, `assess_publication_alignment`, `supersede_period`, `get_alignment`, `is_same_period_support`. Owner lifecycle; public assessment; bounds/hash/URL/date/enum/mask/replay validation.
- **Prompt/EP:** delimit sources and reject embedded instructions; leader/validator independently derive complete tuple; explanations display-only.
- **Error/retry/replay/appeal/timeout:** unavailable/identity mismatch => UNRESOLVED; identical replay idempotent; corrected source creates child assessment; appeal references prior ID; timeout does not mutate.
- **Tests/E2E:** actual 2020-21 statement versus 2025 code => `LATER_REVISION`, same-period synthetic aligned fixture, wrong entity, missing/update date, omitted later-statement phrase, hostile text, malformed fields, disagreement, auth, duplicate, supersession, rollback/readback.
- **CLI/architecture:** later current Studio Dev CLI, explicit account; one contract/test/README/samples/evidence matrix, SDK only. Exclude supplier scoring, web crawler, sanctions checks, payments, frontend.
- **Acceptance/status:** exact negative temporal fixture and safe claim aligned; `REVISE BEFORE BUILD — pending Studio Dev CLI/source-access verification`.
- **Final research disposition:** `REVISE BEFORE BUILD` — Stage 3 may begin only after the Studio Dev CLI/source-access checks listed above pass; no research-only evidence is a deployment or E2E result.
