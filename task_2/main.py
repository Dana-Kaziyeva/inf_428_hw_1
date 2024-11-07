import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from analysis.aggregated_score import compute_aggregated_threat_score
from data.data_generator import generate_random_data


def main():

    department_configs = [
        {'mean': 30, 'variance': 5, 'num_samples': 100, 'importance': 1},
        {'mean': 50, 'variance': 10, 'num_samples': 150, 'importance': 2},
        {'mean': 40, 'variance': 8, 'num_samples': 120, 'importance': 3},
        {'mean': 20, 'variance': 4, 'num_samples': 90, 'importance': 4},
        {'mean': 70, 'variance': 15, 'num_samples': 200, 'importance': 5},
    ]

    departments_data = [
        generate_random_data(config['mean'], config['variance'], config['num_samples'])
        for config in department_configs
    ]

    importance_weights = [config['importance'] for config in department_configs]

    aggregated_score = compute_aggregated_threat_score(departments_data, importance_weights, z_threshold=2)

    print(f"The aggregated cybersecurity threat score for the company is: {aggregated_score:.2f}")

if __name__ == "__main__":
    main()
