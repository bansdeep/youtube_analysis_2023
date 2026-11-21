import json
import unittest
from statistics import median

from scripts.build import ROOT, load, number, summarize


class SnapshotTests(unittest.TestCase):
    def test_findings(self):
        rows = load()
        stats = summarize(rows)
        self.assertEqual(stats['channels'], 995)
        self.assertEqual(stats['recent_missing'], 337)
        self.assertEqual(stats['zero_views'], 8)
        self.assertEqual(stats['countries']['Unknown'], 122)
        self.assertEqual(stats['countries']['India'], 168)
        self.assertEqual(stats['categories']['Unknown'], 46)
        self.assertEqual(median(r['subscribers'] for r in rows), 17_700_000)
        self.assertEqual(max((r['recent'], r['name']) for r in rows if r['recent'] is not None), (8_000_000, 'MrBeast'))

    def test_numeric_parsing(self):
        self.assertIsNone(number('nan'))
        self.assertEqual(number('0'), 0)
        self.assertEqual(number('2.28E+11'), 228_000_000_000)

    def test_generated_outputs_match_source(self):
        rows = load()
        self.assertEqual(json.loads((ROOT / 'docs/metrics.json').read_text()), summarize(rows))
        html = (ROOT / 'docs/index.html').read_text(encoding='utf-8')
        self.assertEqual(json.loads(html.split('const rows = ', 1)[1].split(';\n', 1)[0]), rows)
