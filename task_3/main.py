import sys
from pathlib import Path



sys.path.append(str(Path(__file__).resolve().parent))

from data.sample_data import generate_sample_data
from analysis.feature_extraction import extract_time_features
from analysis.model import build_and_train_model

def main():
    # Generate random data
    df = generate_sample_data()
    # Extract features and calculate time differences
    df = extract_time_features(df)

    # Print the time differences (in hours, minutes, and seconds)
    for index, row in df.iterrows():
        # Format the output string
        print(f"Difference between {int(row['hour_1']):02}:{int(row['minute_1']):02}:{int(row['second_1']):02} "
              f"and {int(row['hour_2']):02}:{int(row['minute_2']):02}:{int(row['second_2']):02} is "
              f"{int(row['diff_hours'])} hours {int(row['diff_minutes'])} minutes {int(row['diff_seconds'])} seconds")
    print(f"Difference in seconds {int(row['time_diff_sec'])}")

    model = build_and_train_model(df)
    print(f"Predictions: {model.predict(df[['hour_1', 'minute_1', 'second_1', 'hour_2', 'minute_2', 'second_2']])}")


if __name__ == '__main__':
    main()
