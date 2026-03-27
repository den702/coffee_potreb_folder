import pytest
from reports.avg_study import AvgStudyReport

def test_avg_study_report():
    data=[
        {"student": "A","study_hours":"3.5"},
        {"student": "A", "study_hours": "4"},
        {"student": "A", "study_hours": "4.5"},
    ]

    report = AvgStudyReport()
    result = report.build(data)

    assert result == [
        ("A",4.0),
    ]