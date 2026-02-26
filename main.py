import json
import argparse
from agent.simple_agent import SimpleAgent
from agent.models import EvaluationScenario
from evaluation.evaluator import run_evaluation


def load_scenario(path):
    with open(path, "r") as f:
        data = json.load(f)

    return EvaluationScenario(
        objective=data["objective"],
        expected_outcome=data["expected_outcome"],
        allowed_tools=data["allowed_tools"],
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenario", required=True)
    args = parser.parse_args()

    scenario = load_scenario(args.scenario)

    agent = SimpleAgent(allowed_tools=scenario.allowed_tools)
    log = agent.run(scenario.objective)

    results = run_evaluation(log, scenario)

    print("\n=== Evaluation Report ===")
    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
