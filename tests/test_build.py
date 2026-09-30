"""Regression tests for the dependency-free dataset validator."""
import datetime as dt
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import build


class DateTests(unittest.TestCase):
    def test_full_date_and_legacy_month(self):
        self.assertEqual(build.parse_date('2026-09-30'), dt.date(2026, 9, 30))
        self.assertEqual(build.parse_date('2024-02'), dt.date(2024, 2, 1))

    def test_invalid_dates_rejected(self):
        for value in ('2026', '2026-9-1', '2026-02-29', '2026-13-01', '', None, '2026-01-01-02'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build.parse_date(value)


class DatasetTests(unittest.TestCase):
    def test_previously_published_model_names_remain_findable(self):
        audit = json.loads((build.ROOT / 'docs/record-audit-first-update.json').read_text())
        as_of = json.loads((build.ROOT / 'site.json').read_text())['asOf']
        _, rows, errors, _ = build.load(as_of)
        self.assertFalse(errors)
        names = {(row['c'], name) for row in rows for name in [row['m']] + row.get('aliases', [])}
        previous = [(r['company'], r['old']['m']) for r in audit['mappings']]
        previous += [(r['c'], r['m']) for r in audit['first_update_records']]
        self.assertEqual([key for key in previous if key not in names], [])

    def test_audited_records_have_source_or_explicit_uncertainty(self):
        as_of = json.loads((build.ROOT / 'site.json').read_text())['asOf']
        _, rows, errors, _ = build.load(as_of)
        self.assertFalse(errors)
        self.assertEqual([r['m'] for r in rows if not r.get('s') and r.get('verification') != 'unverified'], [])

    def validate(self, rows, companies=None):
        with tempfile.TemporaryDirectory() as tmp:
            data = Path(tmp)
            (data / 'companies.json').write_text(json.dumps(companies or [
                dict(key='test', name='Test', sub='Test', region='US', china=False)]))
            (data / 'test.json').write_text(json.dumps(rows))
            with patch.object(build, 'DATA', data):
                return build.load('2026-09-30')

    def row(self, **kwargs):
        return dict(dict(lane='Test', m='Test 1', d='2026-09-29', t='flagship', s='https://example.org/release'), **kwargs)

    def test_source_and_status_survive_build(self):
        _, models, errors, _ = self.validate([self.row(verification='unverified')])
        self.assertEqual(errors, [])
        self.assertEqual(models[0]['s'], 'https://example.org/release')
        self.assertEqual(models[0]['verification'], 'unverified')

    def test_future_release_rejected(self):
        self.assertTrue(self.validate([self.row(d='2026-10-01')])[2])

    def test_new_models_need_source_or_uncertainty(self):
        self.assertTrue(self.validate([self.row(s='')])[2])
        self.assertFalse(self.validate([self.row(s='', verification='unverified')])[2])

    def test_unsafe_sources_rejected(self):
        for source in ('javascript:alert(1)', 'http://example.org', 'https://user:secret@example.org/', 'https://[broken', 123):
            with self.subTest(source=source):
                self.assertTrue(self.validate([self.row(s=source)])[2])

    def test_precise_verified_dates_and_uncertain_month(self):
        self.assertTrue(self.validate([self.row(d='2026-09')])[2])
        self.assertFalse(self.validate([self.row(d='2026-09', verification='unverified')])[2])

    def test_duplicates_and_end_before_release_rejected(self):
        self.assertTrue(self.validate([self.row(), self.row()])[2])
        self.assertTrue(self.validate([self.row(end='2026-09-28')])[2])

    def test_company_keys_unique(self):
        co = dict(key='test', name='Test', sub='Test', region='US', china=False)
        self.assertTrue(self.validate([self.row()], [co, co])[2])

    def test_historical_month_retained(self):
        self.assertFalse(self.validate([self.row(d='2024-02', s='')])[2])

    def test_undated_catalog_requires_source_and_uncertainty(self):
        self.assertFalse(self.validate([self.row(d=None, verification='unverified')])[2])
        self.assertTrue(self.validate([self.row(d=None)])[2])
        self.assertTrue(self.validate([self.row(d=None, s='', verification='unverified')])[2])

    def test_unknown_date_does_not_accept_falsy_non_dates(self):
        for value in ([], {}, 0, False, '', 123, True):
            with self.subTest(value=value):
                self.assertTrue(self.validate([self.row(d=value, verification='unverified')])[2])

    def test_legacy_aliases_preserved_and_validated(self):
        _, models, errors, _ = self.validate([self.row(aliases=['Old combined model'])])
        self.assertFalse(errors)
        self.assertEqual(models[0]['aliases'], ['Old combined model'])
        self.assertTrue(self.validate([self.row(aliases='Not an array')])[2])

    def test_milestones_have_precise_dates_and_sources(self):
        event = dict(d='2026-09-30', n='API 正式开放', s='https://example.org/ga')
        self.assertFalse(self.validate([self.row(events=[event])])[2])
        for change in ({'d':'2026-09'}, {'d':'2026-10-01'}, {'s':'javascript:alert(1)'}, {'s':123}, {'n':''}, {'n':123}):
            self.assertTrue(self.validate([self.row(events=[dict(event, **change)])])[2])


if __name__ == '__main__':
    unittest.main()
