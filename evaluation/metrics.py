def evaluate_task_completion(log, expected_outcome):
    return expected_outcome.lower() in log.final_output.lower()


def evaluate_reasoning(thoughts, objective):
    if not thoughts:
        return 0.0

    aligned = 0
    objective_keyword = objective.lower().split()[0]

    for step in thoughts:
        if objective_keyword in step.lower():
            aligned += 1

    return aligned / len(thoughts)


def evaluate_tool_usage(tool_calls, allowed_tools):
    if not tool_calls:
        return 1.0

    valid = 0

    for call in tool_calls:
        if call["tool_name"] in allowed_tools:
            if isinstance(call.get("parameters"), dict):
                valid += 1

    return valid / len(tool_calls)


def evaluate_latency(execution_time, threshold=5.0):
    return execution_time <= threshold


def aggregate_scores(completion, reasoning, tool_usage, latency):
    return (
        0.4 * int(completion) +
        0.3 * reasoning +
        0.2 * tool_usage +
        0.1 * int(latency)
    )
