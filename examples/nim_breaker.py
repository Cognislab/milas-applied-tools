"""
NIM-Breaker v0.1

A minimal update breaker for AI agent loops.

This example is part of MiLAS Applied Tools.
It is not a complete agent safety system.
It simply demonstrates a small "update pressure suppression" mechanism:
after a configurable number of consecutive updates, the breaker enters
a cooldown period and temporarily blocks further updates.

Author: Mameta Edanari / Cognis-Lab
License: MIT
"""


class NIMBreaker:
    """
    A minimal breaker for repeated agent updates or tool calls.

    Parameters
    ----------
    threshold : int
        Number of consecutive updates allowed before the breaker activates.
    cooldown : int
        Number of turns during which updates are blocked after activation.
    """

    def __init__(self, threshold: int = 5, cooldown: int = 3):
        if threshold <= 0:
            raise ValueError("threshold must be greater than 0")
        if cooldown < 0:
            raise ValueError("cooldown must be 0 or greater")

        self.threshold = threshold
        self.cooldown = cooldown
        self.update_count = 0
        self.cooldown_remaining = 0

    def should_update(self) -> bool:
        """
        Return True if the agent is allowed to continue updating.

        Return False if the breaker is active or enters cooldown.
        """
        if self.cooldown_remaining > 0:
            self.cooldown_remaining -= 1
            return False

        self.update_count += 1

        if self.update_count >= self.threshold:
            self.update_count = 0
            self.cooldown_remaining = self.cooldown
            return False

        return True

    def reset(self) -> None:
        """
        Reset the breaker state.
        """
        self.update_count = 0
        self.cooldown_remaining = 0

    def status(self) -> dict:
        """
        Return the current internal status of the breaker.
        """
        return {
            "threshold": self.threshold,
            "cooldown": self.cooldown,
            "update_count": self.update_count,
            "cooldown_remaining": self.cooldown_remaining,
        }


def run_agent_step(step: int) -> None:
    """
    Dummy agent step for demonstration.
    Replace this with an actual agent update or tool call.
    """
    print(f"Step {step}: agent update executed")


if __name__ == "__main__":
    breaker = NIMBreaker(threshold=5, cooldown=3)

    for i in range(1, 16):
        if breaker.should_update():
            run_agent_step(i)
        else:
            print(f"Step {i}: NIM-Breaker active. Update paused.")
            print(f"Status: {breaker.status()}")
