import csv
import os


class DatasetCollector:

    def __init__(self):

        self.filename = "data/dataset/sign_data.csv"

        os.makedirs("data/dataset", exist_ok=True)

    def save_landmarks(self, landmarks, label):

        row = []

        for lm in landmarks:

            _, x, y, z = lm

            row.extend([x, y, z])

        row.append(label)

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(row)