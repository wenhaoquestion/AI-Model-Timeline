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


if __name__ == '__main__':
    unittest.main()
