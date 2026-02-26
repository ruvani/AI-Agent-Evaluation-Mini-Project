from evaluation.metrics import (
    evaluate_task_completion,
    evaluate_reasoning,
    evaluate_tool_usage,
    evaluate_latency,
    aggregate_scores,
)


def run_evaluation(log, scenario):
    completion = evaluate_task_completion(log, scenario.expected_outcome)
    reasoning_score = evaluate_reasoning(log.thoughts, scenario.objective)
    tool_usage_score = evaluate_tool_usage(log.tool_calls, scenario.allowed_tools)
    latency_ok = evaluate_latency(log.execution_time)

    final_score = aggregate_scores(
        completion,
        reasoning_score,
        tool_usage_score,
        latency_ok,
    )

    return {
        "completion": completion,
        "reasoning_score": reasoning_score,
        "tool_usage_score": tool_usage_score,
        "latency_ok": latency_ok,
        "final_score": round(final_score, 2),
    }
