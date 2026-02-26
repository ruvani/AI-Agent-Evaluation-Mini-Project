import time
from typing import Dict, List
from agent.models import AgentExecutionLog


class SimpleAgent:
    def __init__(self, allowed_tools: List[str]):
        self.allowed_tools = allowed_tools

    def run(self, objective: str) -> AgentExecutionLog:
        start_time = time.time()

        thoughts = []
        tool_calls = []

        # Reasoning simulation
        thoughts.append(f"Understanding objective: {objective}")
        thoughts.append("Plan: Check calendar availability")
        thoughts.append("Plan: Schedule meeting if slot available")

        # Simulated tool call
        if "calendar_api" in self.allowed_tools:
            tool_calls.append({
                "tool_name": "calendar_api",
                "parameters": {
                    "date": "2026-03-01",
                    "priority": "high"
                }
            })

        final_output = "Meeting successfully scheduled for 2026-03-01."

        execution_time = time.time() - start_time

        return AgentExecutionLog(
            thoughts=thoughts,
            tool_calls=tool_calls,
            final_output=final_output,
            execution_time=execution_time
        )
