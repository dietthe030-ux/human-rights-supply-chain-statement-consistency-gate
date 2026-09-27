# Human Rights Supply Chain Statement Consistency Gate

Contract-only Intelligent Contract for a bounded procurement intake signal: whether a supplier-code revision is contemporaneous support for one organisation's signed modern-slavery statement. It does not assess misconduct or supplier behaviour.

## Status

Stage 3 implementation and local validation are complete. Studio Dev deployment is blocked until the mandatory anonymous PRE-DEPLOY dual review is available. No deployment, transaction, Git commit, or push has been performed.

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

## Scope boundary

This repository is contract-only. No frontend, browser deployment, legacy network, MCP, or `E:\GenLayer` access is used.
