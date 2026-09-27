# E2E scenario matrix

| ID | Scenario | Expected | Status |
|---|---|---|---|
| S01 | DHSC 2020–21 statement + DHSC code updated 2025-03-28 | LATER_REVISION | PASS — tx `0x6ca51490457f78529d4a918e2b64721cfe1369848e398459c93d0fb77c8de198`; readback verified |
| S02 | Same-period synthetic code | ALIGNED | PASS — tx `0x1b89030a3b19e0c72e952a2a393cca753233571f83006e0bbd61dbf0ce18941`; readback verified |
| S03 | Wrong entity / Cabinet Office code | UNRESOLVED | PASS — tx `0x2bec956ade16779ee433fa4a4811813a5a7f89e2ed9883a1f8b04f3a87e164ea`; readback verified |
| S04 | Invalid record/state input | rejected | PASS — finalized tx `0xb9c19e930b445a45c90e7636eb7461d289c981b88eae4ac262bd511d552e1cda`; post-state unchanged |
| S05 | Replay of identical assessment | idempotent | PASS — tx `0x64c9c64659504d66db62f87782dc7b5f97e72670d2cae8c8e6d86430ea9d05d8`; readback unchanged |
| S06 | Supersession and readback | SUPERSEDED | PASS — finalized tx `0x852ac26466d22d30af0b284dd3c43067daa183200ccc6bc45bd6ba1f9c3b44e6`; readback `SUPERSEDED` |

No transaction hash or Explorer URL is claimed before deployment.
