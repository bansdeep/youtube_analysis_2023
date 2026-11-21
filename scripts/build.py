"""Build the dashboard and snapshot metrics using only the Python standard library."""
import csv
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'Global YouTube Statistics.csv'


def number(value):
    return None if value.strip().lower() in {'', 'nan'} else int(Decimal(value))


def label(value):
    return 'Unknown' if value.strip().lower() in {'', 'nan'} else value.strip()


def load():
    with SOURCE.open(encoding='latin-1', newline='') as source:
        rows = [dict(rank=number(r['rank']), name=r['Youtuber'],
                     country=label(r['Country']), category=label(r['category']),
                     subscribers=number(r['subscribers']), views=number(r['video views']),
                     recent=number(r['subscribers_for_last_30_days']))
                for r in csv.DictReader(source)]
    if sorted(r['rank'] for r in rows) != list(range(1, len(rows) + 1)):
        raise ValueError('Expected one row per unique consecutive source rank')
    return rows


def summarize(rows):
    countries = Counter(r['country'] for r in rows)
    categories = Counter(r['category'] for r in rows)
    return dict(channels=len(rows), countries=dict(countries.most_common()),
                categories=dict(categories.most_common()),
                recent_missing=sum(r['recent'] is None for r in rows),
                zero_views=sum(r['views'] == 0 for r in rows))


def main():
    rows = load()
    payload = json.dumps(rows, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c')
    template = (ROOT / 'scripts/dashboard.html').read_text(encoding='utf-8')
    (ROOT / 'docs/index.html').write_text(template.replace('/* SNAPSHOT */', payload), encoding='utf-8')
    (ROOT / 'docs/metrics.json').write_text(json.dumps(summarize(rows), indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
