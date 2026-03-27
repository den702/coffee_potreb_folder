import pytest
from reports.median_coffee import MedianCoffeeReport


def test_median_report():
    data = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "200"},
        {"student": "A", "coffee_spent": "300"},
        {"student": "B", "coffee_spent": "50"},
        {"student": "B", "coffee_spent": "150"},
    ]

    report = MedianCoffeeReport()
    result = report.build(data)

    assert result == [
        ("A", 200),
        ("B", 100),
    ]