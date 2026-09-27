# { "Depends": "py-genlayer:5jycge4q8k23462jtb0b9fyey1s9qz928sz2nbrd9mg4sxqg2qng" }
import genlayer as gl
from genlayer.types import Address


def _resolve(value):
    return value.get() if isinstance(value, gl.Lazy) else value


class HumanRightsSupplyChainStatementConsistencyGate(gl.contract.Contract):
    owner: Address
    organization: str
    state: str
    outcome: str
    replay_key: str
    def __init__(self):
        self.owner = gl.message.sender_address
        self.organization = ""
        self.state = "EMPTY"
        self.outcome = ""
        self.replay_key = ""

    def _require_owner(self):
        if gl.message.sender_address != self.owner:
            raise gl.vm.UserError("OWNER_ONLY")

    @gl.public.write
    def register_profile(self, organization: str) -> int:
        self._require_owner()
        if not organization or len(organization) > 160:
            raise gl.vm.UserError("INVALID_ORGANIZATION")
        if self.state != "EMPTY":
            raise gl.vm.UserError("PROFILE_EXISTS")
        self.organization = organization
        self.state = "REGISTERED"
        return 1

    @gl.public.write
    def seal_period_and_code(self, record_id: int, period_start: str, period_end: str,
                             statement_signed: str, code_updated: str,
                             statement_url: str, code_url: str,
                             statement_hash: str, code_hash: str) -> bool:
        self._require_owner()
        if record_id != 1 or self.state not in ("REGISTERED", "SEALED"):
            raise gl.vm.UserError("INVALID_STATE")
        if not period_start or not period_end or not statement_signed or not code_updated:
            raise gl.vm.UserError("MISSING_DATE")
        if not statement_url.startswith("https://www.gov.uk/") or not code_url.startswith("https://www.gov.uk/"):
            raise gl.vm.UserError("URL_NOT_ALLOWLISTED")
        if len(statement_hash) != 64 or len(code_hash) != 64:
            raise gl.vm.UserError("INVALID_HASH")
        self.state = "SEALED"
        return True

    @gl.public.write
    def assess_publication_alignment(self, record_id: int, organization: str,
                                    statement_period_match: bool, identity_match: bool,
                                    code_date_state: str, code_promised_for_later_statement: bool,
                                    commitment_overlap_mask: int, source_ok: bool,
                                    replay_key: str) -> dict:
        if record_id != 1 or self.state not in ("SEALED", "ASSESSED", "REASSESSED"):
            raise gl.vm.UserError("INVALID_STATE")
        if not replay_key or len(replay_key) > 96:
            raise gl.vm.UserError("INVALID_REPLAY_KEY")
        if self.replay_key == replay_key and self.outcome:
            return {"replay_key": replay_key, "organization": organization,
                    "identity_match": identity_match, "statement_period_match": statement_period_match,
                    "code_date_state": code_date_state, "code_promised_for_later_statement": code_promised_for_later_statement,
                    "commitment_overlap_mask": commitment_overlap_mask, "outcome": self.outcome}
        if not source_ok or not identity_match or not statement_period_match:
            outcome = "UNRESOLVED"
        elif code_date_state == "LATER" or code_promised_for_later_statement:
            outcome = "LATER_REVISION"
        elif code_date_state == "WITHIN_PERIOD":
            outcome = "ALIGNED"
        else:
            outcome = "UNRESOLVED"
        self.replay_key = replay_key
        self.outcome = outcome
        self.state = "ASSESSED"
        result = {"replay_key": replay_key, "organization": organization,
                  "identity_match": identity_match, "statement_period_match": statement_period_match,
                  "code_date_state": code_date_state,
                  "code_promised_for_later_statement": code_promised_for_later_statement,
                  "commitment_overlap_mask": commitment_overlap_mask, "outcome": outcome}
        return result

    @gl.public.write
    def supersede_period(self, record_id: int, successor_id: int) -> bool:
        self._require_owner()
        if record_id != 1 or successor_id != 1:
            raise gl.vm.UserError("UNKNOWN_RECORD")
        if self.state != "ASSESSED":
            raise gl.vm.UserError("INVALID_STATE")
        self.state = "SUPERSEDED"
        return True

    @gl.public.view
    def get_alignment(self, record_id: int) -> dict:
        if record_id != 1 or self.state == "EMPTY":
            raise gl.vm.UserError("UNKNOWN_RECORD")
        return {"organization": self.organization, "state": self.state,
                "outcome": self.outcome, "replay_key": self.replay_key}

    @gl.public.view
    def is_same_period_support(self, record_id: int) -> bool:
        return record_id == 1 and self.outcome == "ALIGNED"
