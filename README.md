## Viridien ML Assignment – Phase 1 Mock API

## Overview

This project is a simple customer support triage system built for the Viridien ML assignment.
The goal was to demonstrate a clear, step-by-step workflow using LangGraph, rather than handling everything inside a single API function.

The agent processes a support ticket by extracting an order ID, classifying the issue, fetching order details from mock data, drafting a reply, and finally passing the suggestion through a lightweight admin review step.

I intentionally kept the logic rule-based and the data mocked so that the behavior is easy to understand, test, and demonstrate.

⸻

## Design Approach

Before writing any code, I first outlined the flow on paper:
	1.	A customer submits a support ticket
	2.	The assistant extracts an order ID from the text
	3.	The issue is classified using simple keyword rules
	4.	Order details are fetched from mock data
	5.	A reply is drafted for the customer
	6.	An admin step approves or flags the action

Once the flow was clear, I implemented each step as a separate LangGraph node so that the shared state could move cleanly through the graph and remain inspectable at every stage.

## Project Structure

viridien-ml-assignment/
├── app/
│   ├── main.py        # FastAPI routes
│   ├── state.py       # Shared Pydantic state
│   ├── nodes.py       # LangGraph node logic
│   └── graph.py       # Graph definition and wiring
├── mock_data/
│   ├── orders.json
│   ├── issues.json
│   └── replies.json
├── tests/
│   └── test.py        # CI smoke test
├── requirements.txt
└── README.md

## Setup
This project was developed using Python 3.11.
Clone the repository, create a virtual environment, and install dependencies:
git clone https://github.com/user_name/repo_name.git
cd repo_name

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Running the API
Start the server with:
uvicorn app.main:app --reload
Once running, you can access:
	•	Swagger UI: http://127.0.0.1:8000/docs
	•	Health check: http://127.0.0.1:8000/health

## Example Usage

I tested the agent using Swagger UI as well as a simple curl request.
curl -X POST http://127.0.0.1:8000/triage/invoke \
  -H "Content-Type: application/json" \
  -d '{
    "ticket_text": "My order ORD1001 is missing an item"
  }'
Example response:
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
    "Drafted reply using order details.",
    "Admin: approved the suggested action."
  ]
}
The messages field makes it easy to see how the state progressed through each node in the graph.

## Testing and CI

A small smoke test is included so that the CI pipeline runs on every push.
This helped verify that dependencies install correctly and that the project imports cleanly in a fresh environment.

Run tests locally with:
pytest -q
The GitHub Actions workflow currently passes on the main branch.

## AI Tool Usage
I used Cursor as a coding assistant while building this project. Cursor was helpful for scaffolding files, refactoring LangGraph nodes, and debugging import and dependency issues.
The overall design decisions, workflow planning, and testing were done manually, with Cursor mainly used to speed up iteration and reduce boilerplate.


