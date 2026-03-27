from collections import defaultdict
from  statistics import mean
from wsgiref.util import setup_testing_defaults

from .base import BaseReport

class AvgStudyReport(BaseReport):
    name = "avg-study"

    def build(self, data):
        grouped = defaultdict(list)

        for row in data:
            student = row["student"]
            study=float(row["study_hours"])
            grouped[student].append(study)

        result=[]

        for student,values in grouped.items():
            result.append((student,mean(values)))

        result.sort(key=lambda x: x[1],reverse=True)

        return result