import os
import re
import json

from .state import TriageState
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MOCK_DIR = os.path.join(ROOT, "mock_data")

def load_mock(name):
    with open(os.path.join(MOCK_DIR, name), "r", encoding="utf-8") as f:
        return json.load(f)

ORDERS = load_mock("orders.json")
ISSUES = load_mock("issues.json")
REPLIES = load_mock("replies.json")

def ingest(state: TriageState) -> TriageState:
    msg = f"Ticket received: {state.ticket_text}"
    state.messages.append(msg)
    return state

def extract_order_id(state: TriageState) -> TriageState:
    # Extract order IDs like ORD1234
    if not state.order_id and state.ticket_text:
        match = re.search(r"(ORD\d{4})", state.ticket_text, re.IGNORECASE)
        if match:
            state.order_id = match.group(1).upper()
            state.messages.append(f"Extracted order_id: {state.order_id}")
        else:
            state.messages.append("No order_id found")
    return state

def classify_issue(state: TriageState) -> TriageState:
    text = (state.ticket_text or "").lower()
    state.issue_type = "unknown"
    state.recommendation = "review"
    for rule in ISSUES:
        if rule["keyword"].lower() in text:
            state.issue_type = rule["issue_type"]
            state.recommendation = rule.get("recommendation", "review")
            state.messages.append(f"Issue classified as: {state.issue_type}")
            break
    if state.issue_type == "unknown":
        state.messages.append("Issue type could not be classified")
    return state

def fetch_order(state: TriageState) -> TriageState:
    if state.order_id:
        match = next((o for o in ORDERS if o["order_id"] == state.order_id), None)
        if match:
            state.evidence = match
            state.messages.append(f"Fetched order: {state.order_id}")
        else:
            state.evidence = None
            state.messages.append(f"No order found for {state.order_id}")
    else:
        state.messages.append("No order_id available to fetch order")
    return state

def draft_reply(state: TriageState) -> TriageState:
    template = next((r["template"] for r in REPLIES if r["issue_type"] == state.issue_type), None)
    order = state.evidence if isinstance(state.evidence, dict) else None
    reply = ""
    if template:
        if order:
            reply = template.replace("{{customer_name}}", order.get("customer_name","Customer")) \
                .replace("{{order_id}}", order.get("order_id",""))

            state.messages.append("Drafted reply using order details.")
        else:
            reply = template
            state.messages.append("Drafted reply without order details.")
    else:
        reply = "We received your request and will get back to you soon."
        state.messages.append("No template found for issue type; drafted generic reply.")
    state.draft_reply = reply
    return state
