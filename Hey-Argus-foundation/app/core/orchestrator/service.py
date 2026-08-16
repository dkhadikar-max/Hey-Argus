from dataclasses import dataclass


@dataclass
class AgentRequest:
    user_id: str
    message: str


class ArgusOrchestrator:
    """Initial orchestration boundary.

    V1 implementation will add context retrieval, planning, policy evaluation,
    agent routing, execution, verification, and audit emission.
    """

    async def handle(self, request: AgentRequest) -> dict:
        return {
            "status": "accepted",
            "message": request.message,
            "next": "planner",
        }
