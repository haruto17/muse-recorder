import csv
import os

fieldnames = [
    "Music Name",
    "Achievement",
    "Max Combo",
    "Perfect",
    "Great",
    "Pass",
    "Miss",
    "Score",
    "Datetime",
]


def write_csv(data):
    path = "data/" + data[0] + ".csv"
    is_file = os.path.isfile(path)
    if is_file:
        with open(path, "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(
                {
                    "Music Name": data[0],
                    "Achievement": data[1],
                    "Max Combo": data[2],
                    "Perfect": data[3],
                    "Great": data[4],
                    "Pass": data[5],
                    "Miss": data[6],
                    "Score": data[7],
                    "Datetime": data[8],
                }
            )
    else:
        with open(path, "w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(
                {
                    "Music Name": data[0],
                    "Achievement": data[1],
                    "Max Combo": data[2],
                    "Perfect": data[3],
                    "Great": data[4],
                    "Pass": data[5],
                    "Miss": data[6],
                    "Score": data[7],
                    "Datetime": data[8],
                }
            )
