# Hey Argus

> A private, secure, agentic personal AI operating assistant.

**Hey Argus** is designed to become a personal AI system that can understand natural language and voice, remember useful context, research information, write and execute code, operate controlled computer/browser environments, manage day-to-day tasks, and coordinate specialized AI agents.

Argus is designed as a **control plane**, not merely a chatbot.

---

## Vision

The interaction should be simple:

> **"Hey Argus, handle this."**

Argus determines what the user wants, plans the work, selects the appropriate agent and tools, executes within defined permissions, verifies the result, and reports back.

```text
User
 │
 │ Voice / Text
 ▼
Hey Argus
 │
 ▼
Identity
 │
 ▼
Intent
 │
 ▼
Planner
 │
 ▼
Orchestrator
 │
 ├── Personal Agent
 ├── Research Agent
 ├── Coding Agent
 ├── Computer Agent
 ├── Browser Agent
 └── Communication Agent
 │
 ▼
Policy / Permission Engine
 │
 ▼
Tools / External Systems
 │
 ▼
Verification
 │
 ▼
Result