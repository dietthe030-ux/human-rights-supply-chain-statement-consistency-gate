# Human Rights Supply Chain Statement Consistency Gate

Contract-only Intelligent Contract for a bounded procurement intake signal: whether a supplier-code revision is contemporaneous support for one organisation's signed modern-slavery statement. It does not assess misconduct or supplier behaviour.

## Status

Stage 3 implementation, Studio Dev deployment, and full E2E validation are complete. The task-local workflow disabled anonymous review, so the release evidence is bound to the public revision and finalized Studio Dev transactions below.

## Contract API

- `register_profile(organization)` — owner creates an append-only record.
- `seal_period_and_code(...)` — owner seals dates, allowlisted GOV.UK URLs, and SHA-256 hashes.
- `assess_publication_alignment(...)` — public assessment with deterministic `ALIGNED`, `LATER_REVISION`, or `UNRESOLVED` outcome and replay idempotency.
- `supersede_period(record_id, successor_id)` — owner closes an assessed period.
- `get_alignment(record_id)`, `is_same_period_support(record_id)` — public views.

`LATER_REVISION` is the expected result for the DHSC 2020–21 statement and 2025-03-28 supplier code fixture. A later revision cannot prove same-period support.

## Verification

- Direct tests: `3 passed`.
- GenVM lint/validation: passed with the pinned `py-genlayer` dependency and Studio Next toolchain.
- Network readiness: Studio Dev, chain ID `61997`, canonical RPC `https://studio-dev.genlayer.com/api`.

## Live deployment

- Network: Studio Dev, chain ID `61997`
- Contract: `0xED43b573d981fF10F2cA9983a1BAcB61a39cEb36`
- Deployment transaction: `0x88ec88b7a14e2f09fcc161c9776ed286b8869ccab007115e6adfd8038924aa14`
- Explorer: `https://explorer-studio-dev.genlayer.com/address/0xED43b573d981fF10F2cA9983a1BAcB61a39cEb36`
- E2E evidence: [evidence/E2E_MATRIX.md](evidence/E2E_MATRIX.md)
- Public repository: `https://github.com/dietthe030-ux/human-rights-supply-chain-statement-consistency-gate`
- All six scenarios in the E2E matrix passed with finalized receipts and authoritative readback.

## Scope boundary

This repository is contract-only. No frontend, browser deployment, legacy network, MCP, or `E:\GenLayer` access is used.
