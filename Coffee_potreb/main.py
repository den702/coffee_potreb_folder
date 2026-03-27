import argparse
from tabulate import tabulate

from reader import read_files
from reports import REPORTS


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    args = parser.parse_args()

    if args.report not in REPORTS:
        print("Unknown report")
        return

    data = read_files(args.files)
    report = REPORTS[args.report]

    result = report.build(data)

    headers_map = {
        "median-coffee": ["Student", "Median coffee"],
        "avg-sleep": ["Student", "Avg sleep"],
        "avg-study": ["Student","Avg study"],
    }

    headers = headers_map.get(args.report, ["Student", "Value"])

    print(tabulate(result, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    main()