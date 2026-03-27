from collections import defaultdict
from statistics import median
from .base import BaseReport


class MedianCoffeeReport(BaseReport):
    name = "median-coffee"

    def build(self, data):
        grouped = defaultdict(list)

        for row in data:
            student = row["student"]
            coffee = float(row["coffee_spent"])
            grouped[student].append(coffee)

        result = []

        for student, values in grouped.items():
            result.append((student, median(values)))

        result.sort(key=lambda x: x[1], reverse=True)

        return result