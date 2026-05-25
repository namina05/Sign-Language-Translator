import csv
import os


class DatasetCollector:

    def __init__(self):

        self.filename = "data/dataset/sign_data.csv"

        os.makedirs("data/dataset", exist_ok=True)

    def save_landmarks(self, landmarks, label):
        if not landmarks:
            return

        row = []
        wrist_x=landmarks[0][1]
        wrist_y = landmarks[0][2]
        wrist_z = landmarks[0][3]
        for lm in landmarks:

            _, x, y, z = lm

            row.extend([x-wrist_x, y-wrist_y, z-wrist_z])

        row.append(label)

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(row)