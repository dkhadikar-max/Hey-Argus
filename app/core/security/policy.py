from enum import IntEnum


class RiskLevel(IntEnum):
    L0 = 0
    L1 = 1
    L2 = 2
    L3 = 3
    L4 = 4


class PolicyEngine:
    """Fail-closed policy boundary for Argus actions."""

    async def authorize(
        self,
        *,
        user_id: str,
        capability: str,
        risk: RiskLevel,
        approved: bool = False,
    ) -> bool:
        if risk >= RiskLevel.L4:
            return approved
        if risk >= RiskLevel.L3:
            return approved
        return True
