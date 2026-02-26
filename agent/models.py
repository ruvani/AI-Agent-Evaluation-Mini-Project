from dataclasses import dataclass
from typing import List, Dict


@dataclass
class EvaluationScenario:
    objective: str
    expected_outcome: str
    allowed_tools: List[str]


@dataclass
class AgentExecutionLog:
    thoughts: List[str]
    tool_calls: List[Dict]
    final_output: str
    execution_time: float
