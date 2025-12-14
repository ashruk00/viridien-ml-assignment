from langgraph.graph import StateGraph

from .state import TriageState
from .nodes import ingest, extract_order_id, classify_issue, fetch_order, draft_reply

graph_builder = StateGraph(TriageState)

graph_builder.add_node("ingest", ingest)
graph_builder.add_node("extract_order_id", extract_order_id)
graph_builder.add_node("classify_issue", classify_issue)
graph_builder.add_node("fetch_order", fetch_order)
graph_builder.add_node("draft_reply", draft_reply)

# Wire the nodes in the specified order
graph_builder.add_edge("ingest", "extract_order_id")
graph_builder.add_edge("extract_order_id", "classify_issue")
graph_builder.add_edge("classify_issue", "fetch_order")
graph_builder.add_edge("fetch_order", "draft_reply")

graph_builder.set_entry_point("ingest")

graph = graph_builder.compile()
