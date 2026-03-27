from collections import defaultdict
from statistics import mean
from .base import BaseReport

class AvgSleepReport(BaseReport):
    name = ("avg-sleep")

    def build(self, data):
        grouped=defaultdict(list)

        for row in data:
            student = row["student"]
            sleep=float(row["sleep_hours"])
            grouped[student].append(sleep)

        result=[]

        for student,values in grouped.items():
            result.append((student, mean(values)))

        result.sort(key=lambda x: x[1],reverse=True)

        return result
