import argparse
import csv
from tabulate import tabulate

from filter import apply_filter
from aggregate import aggregate


def load_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def parse_args():
    parser = argparse.ArgumentParser(description='Process CSV with filtering and aggregation.')
    parser.add_argument('--file', required=True, metavar='PATH', help='Путь к CSV-файлу')
    parser.add_argument('--where', metavar='FILTER', help='Условие фильтрации, например: price>500')
    parser.add_argument('--aggregate', metavar='AGG', help='Агрегация: column=avg | column=max')
    return parser.parse_args()


def process(args):
    rows = load_csv(args.file)
    if not rows:
        raise ValueError("CSV is empty.")

    if args.where:
        rows = apply_filter(rows, args.where)

    if args.aggregate:
        result = aggregate(rows, args.aggregate)
        print(tabulate(result, headers='keys', tablefmt='rounded_grid'))
    else:
        print(tabulate(rows, headers='keys', tablefmt='rounded_grid') if rows else "No data after filtering.")


def main():
    try:
        args = parse_args()
        process(args)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
