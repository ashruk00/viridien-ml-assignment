from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

class TriageState(BaseModel):
    messages: List[str] = Field(default_factory=list)
    ticket_text: Optional[str] = None
    order_id: Optional[str] = None
    issue_type: Optional[str] = None
    evidence: Optional[Dict[str, Any]] = None
    recommendation: Optional[str] = None
    draft_reply: Optional[str] = None
