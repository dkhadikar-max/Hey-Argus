# Hey Argus — Architecture

## Purpose
Hey Argus is a standalone personal agentic AI operating assistant. It is not related to BYN or MentraAI.

Argus owns the control plane: identity, orchestration, planning, memory contracts, permissions, tool routing, verification, and auditability.

Open-source projects are capability providers behind stable Argus interfaces. They must remain replaceable.

## High-level system

```text
User
  |
  | Voice / Text
  v
Client (Phone / iPad / Web)
  |
  v
Argus Gateway
  |
  +--> Authentication / Device Trust
  |
  v
Orchestrator
  |
  +--> Context + Memory
  +--> Intent Classification
  +--> Planner
  +--> Agent Router
  +--> Policy Evaluation
  |
  v
Agents
  |
  +--> Personal
  +--> Research
  +--> Coding
  +--> Computer
  +--> Browser
  +--> Communication
  |
  v
Tool Gateway
  |
  +--> GitHub
  +--> Terminal / Sandbox
  +--> Browser
  +--> Files
  +--> External APIs
  |
  v
Verification
  |
  v
Result + Audit Event
```

## Core modules

### Gateway
- API entry point
- Authentication
- Device/session management
- Request validation
- Rate limiting
- Realtime task updates

### Orchestrator
Central decision layer. It does not directly execute arbitrary tools.

```text
Request
 -> normalize
 -> identify intent
 -> retrieve context
 -> create plan
 -> select agent
 -> request tool capabilities
 -> policy check
 -> execute
 -> verify
 -> respond
 -> persist relevant memory
```

### Agents
V1:
- PersonalAgent
- ResearchAgent
- CodingAgent
- ComputerAgent
- BrowserAgent
- CommunicationAgent

Agents must use Argus tool interfaces rather than bypassing the policy layer.

### Tool Gateway
Every external action is represented as a capability-controlled tool. The gateway validates, executes, normalizes results, and emits audit events.

## External capability providers

| Capability | Candidate OSS foundation |
|---|---|
| Coding runtime | OpenHands |
| Controlled computer execution | Open Interpreter |
| Browser automation | Playwright |
| Persistent memory | Mem0 |
| Wake word | openWakeWord / Wyoming |
| Speech recognition | faster-whisper |
| Speech synthesis | Piper |

Integrations must be wrapped behind Argus interfaces so providers can be replaced without changing agent logic.

## Data architecture

PostgreSQL is the system of record.

Redis is used for ephemeral state, caching, queues, locks, and realtime task state.

Recommended PostgreSQL domains:

```text
users
user_devices
sessions
conversations
messages
tasks
task_steps
agents
tool_definitions
permissions
approvals
audit_events
memories
projects
integrations
```

Use pgvector where semantic retrieval is required.

## Task state machine

```text
CREATED
  |
  v
PLANNING
  |
  +----> BLOCKED
  |
  v
POLICY_CHECK
  |
  +----> WAITING_APPROVAL
  |             |
  |             v
  |         APPROVED
  |             |
  +-------------+
  |
  v
EXECUTING
  |
  v
VERIFYING
  |
  +----> FAILED
  |
  v
COMPLETED
```

Users must be able to cancel active tasks.

## Memory architecture

Argus distinguishes:
- Working memory: current task/session context.
- Long-term memory: stable user preferences, projects, goals, and important decisions.
- Semantic memory: searchable knowledge and documents.

Memory writes should be deliberate and policy-controlled. A model must not silently persist arbitrary sensitive content.

Mem0 may provide the memory implementation, but Argus owns the memory contract and retention policy.

## Voice architecture

```text
Microphone
 -> wake-word detector
 -> speech-to-text
 -> speaker/device authentication
 -> Argus Gateway
 -> Orchestrator
 -> Agent
 -> text-to-speech
```

Voice identity is not sufficient authorization for high-risk operations.

## Coding architecture

Coding must run through an isolated execution boundary.

```text
CodingAgent
   |
   v
ExecutionGateway
   |
   v
Sandbox / Workspace
   |
   +--> Repository
   +--> Terminal
   +--> Tests
   +--> Build
   |
   v
Diff + Verification
   |
   v
Approval when required
```

OpenHands can be integrated behind this boundary for software-engineering workflows.

## Security boundaries

No agent may directly access credentials or bypass policy.

Sensitive credentials are exposed only through controlled tool adapters.

Every action has:
- actor
- task ID
- agent
- tool
- capability
- risk classification
- approval state
- timestamp
- result

## Risk model

| Level | Description | Default |
|---|---|---|
| L0 | Read-only/informational | Automatic |
| L1 | Reversible local actions | Automatic in sandbox |
| L2 | Repository or development changes | Policy controlled |
| L3 | External communication/publication | Explicit approval |
| L4 | Financial, credential, destructive, production-critical | Explicit approval every time |

## Client architecture

One backend serves multiple clients:

```text
                 Argus Backend
                /      |      \
             Web     Phone     iPad
```

Clients are presentation and interaction layers. Identity, task state, memory, and authorization remain server-side.

## Design principles

1. Least privilege.
2. Explicit authority.
3. Provider independence.
4. Inspectable plans.
5. Sandboxed execution.
6. Auditable actions.
7. Human approval for high-impact operations.
8. Persistent but selective memory.
9. Fail closed on authorization errors.
10. Stop/kill must terminate active execution as quickly as possible.
