# Phase 1 — Public
Minimal mock API and multi-turn demo interactions for ticket triage.
Viridien ML Assignment – Phase 1 Mock API

This project implements a mock customer support triage agent using FastAPI and LangGraph.
The agent ingests a customer support ticket, extracts an order ID, classifies the issue, fetches order data, and drafts a response.

🚀 Features

FastAPI-based REST API

Rule-based issue classification

Order lookup using mock data

State-based agent workflow using LangGraph

Drafted customer replies

CI pipeline with passing tests

📁 Project Structure
viridien-ml-assignment/
├── app/
│   ├── main.py        # FastAPI app & routes
│   ├── state.py       # Pydantic state model
│   ├── nodes.py       # Agent node logic
│   └── graph.py       # LangGraph workflow
├── mock_data/
│   ├── orders.json
│   ├── issues.json
│   └── replies.json
├── tests/
│   └── test.py        # CI smoke test
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/ashruk00/viridien-ml-assignment.git
cd viridien-ml-assignment

2️⃣ Create and activate virtual environment
python -m venv venv


Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the API
uvicorn app.main:app --reload


The API will be available at:

Swagger UI: http://127.0.0.1:8000/docs

Health Check: http://127.0.0.1:8000/health

🔁 Example: Invoke the Triage Agent
curl Example
curl -X POST "http://127.0.0.1:8000/triage/invoke" \
  -H "Content-Type: application/json" \
  -d '{
    "ticket_text": "My order ORD1001 is missing an item"
  }'

Sample Response
{
  "order_id": "ORD1001",
  "issue_type": "missing_item",
  "order": {
    "order_id": "ORD1001",
    "customer_name": "Ava Chen",
    "email": "ava.chen@example.com"
  },
  "reply_text": "Hi Ava Chen, thanks for letting us know. We have escalated order ORD1001 to locate the missing item.",
  "messages": [
    "Ticket received: My order ORD1001 is missing an item",
    "Extracted order_id: ORD1001",
    "Issue classified as: missing_item",
    "Fetched order: ORD1001",
    "Drafted reply using order details."
  ]
}

🧪 Tests & CI

CI runs automatically on every push using GitHub Actions

Tests executed via pytest

Current pipeline status: Passing ✅

Run tests locally:

pytest -q

🤖 How I Used Cursor

I used Cursor as my primary development environment to scaffold the FastAPI project, refactor the LangGraph workflow, and iteratively build and debug the agent nodes. Cursor’s inline AI assistance helped accelerate development, maintain clean structure across files, and quickly resolve integration and CI issues.
