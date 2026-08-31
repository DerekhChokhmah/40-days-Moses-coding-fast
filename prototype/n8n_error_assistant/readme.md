# n8n AI Error Assistant

An AI-powered error diagnosis assistant for n8n workflows.

When an n8n workflow fails, the Error Trigger sends the error information to a FastAPI backend. The backend uses OpenAI to analyze the error and return a structured diagnosis. The result is then sent to a Slack channel.

## Architecture

```text
n8n Workflow
    ↓
Error Trigger
    ↓
HTTP Request
    ↓
FastAPI
    ↓
OpenAI
    ↓
Structured Error Analysis
    ↓
Slack
```

## Features

- Captures n8n workflow errors
- Extracts the failed node, node type, error message, and status code
- Sends error information to a FastAPI backend
- Uses an LLM to analyze the failure
- Produces structured error analysis
- Sends the diagnosis to Slack

## Project Structure

```text
n8n_error_assistant/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── app/
│   ├── analyser.py
│   ├── main.py
│   └── models.py
└── tests/
```

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file containing the required API credentials.

**Do not commit `.env` to GitHub.**

## Run the FastAPI Server

```bash
uvicorn app.main:app --reload
```

The API exposes:

```text
POST /analyze-error
```

## ngrok

Expose the local FastAPI server so that n8n Cloud can reach it:

```bash
ngrok http 8000
```

Use the generated HTTPS URL in the n8n HTTP Request node:

```text
https://YOUR-NGROK-DOMAIN/analyze-error
```

## n8n Configuration

The Error Assistant workflow uses:

```text
Error Trigger
    ↓
HTTP Request
    ↓
Edit Fields
    ↓
Slack
```

The Error Trigger data is mapped into:

```text
node
node_type
error
status_code
```

## AI Output

The AI returns a structured analysis containing:

```text
root_cause
explanation
evidence
fix
next_action
```

The formatted result is then sent to the configured Slack channel.

## Example

A failing HTTP Request returning:

```text
401 Unauthorized
```

is analyzed by the assistant and converted into a developer-oriented diagnosis containing:

- Root cause
- Explanation
- Evidence
- Recommended fix
- Next action

## Status

**Prototype 1 — Functional MVP**