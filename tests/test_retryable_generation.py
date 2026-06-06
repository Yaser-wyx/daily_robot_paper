import unittest
from unittest.mock import patch

import requests

from robopulse import daily as daily_module
from robopulse.config import (
    ARXIV_NOT_UPDATED_EXIT_CODE,
    GENERAL_FAILURE_EXIT_CODE,
    RETRYABLE_GENERATION_EXIT_CODE,
)


class DummyResponse:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.exceptions.HTTPError(response=self)


class DailyRetryableGenerationTests(unittest.TestCase):
    def test_arxiv_timeout_returns_retryable_generation_code(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch("robopulse.arxiv.requests.get", side_effect=requests.exceptions.Timeout):
                self.assertEqual(daily_module.main(), RETRYABLE_GENERATION_EXIT_CODE)

    def test_arxiv_connection_error_returns_retryable_generation_code(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch("robopulse.arxiv.requests.get", side_effect=requests.exceptions.ConnectionError):
                self.assertEqual(daily_module.main(), RETRYABLE_GENERATION_EXIT_CODE)

    def test_arxiv_request_exception_returns_retryable_generation_code(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch("robopulse.arxiv.requests.get", side_effect=requests.exceptions.RequestException):
                self.assertEqual(daily_module.main(), RETRYABLE_GENERATION_EXIT_CODE)

    def test_arxiv_5xx_returns_retryable_generation_code(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch("robopulse.arxiv.requests.get", return_value=DummyResponse(status_code=503)):
                self.assertEqual(daily_module.main(), RETRYABLE_GENERATION_EXIT_CODE)

    def test_arxiv_4xx_returns_general_failure_code(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch("robopulse.arxiv.requests.get", return_value=DummyResponse(status_code=404)):
                self.assertEqual(daily_module.main(), GENERAL_FAILURE_EXIT_CODE)

    def test_arxiv_not_updated_returns_existing_code(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch.object(daily_module, "fetch_arxiv_papers", side_effect=daily_module.ArxivNotUpdatedError):
                self.assertEqual(daily_module.main(), ARXIV_NOT_UPDATED_EXIT_CODE)

    def test_screening_failure_returns_retryable_generation_code(self):
        papers = [{"id": "2501.00001", "title": "Paper", "authors": "Author", "abstract": "Abstract"}]
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch.object(daily_module, "fetch_arxiv_papers", return_value=papers):
                with patch.object(daily_module, "editor_screening", return_value=None):
                    self.assertEqual(daily_module.main(), RETRYABLE_GENERATION_EXIT_CODE)

    def test_analysis_failure_returns_retryable_generation_code(self):
        papers = [{"id": "2501.00001", "title": "Paper", "authors": "Author", "abstract": "Abstract"}]
        screening_result = {
            "title": "RoboPulse | Test",
            "opening_summary": "",
            "shortlist_ids": ["2501.00001"],
            "selected_ids": ["2501.00001"],
        }
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=True):
            with patch.object(daily_module, "fetch_arxiv_papers", return_value=papers):
                with patch.object(daily_module, "editor_screening", return_value=screening_result):
                    with patch.object(daily_module, "enrich_shortlist_with_html", return_value=papers):
                        with patch.object(daily_module, "analyze_shortlist", return_value=None):
                            self.assertEqual(daily_module.main(), RETRYABLE_GENERATION_EXIT_CODE)

    def test_runtime_requirement_failure_stays_general_failure(self):
        with patch.object(daily_module, "ensure_runtime_requirements", return_value=False):
            self.assertEqual(daily_module.main(), GENERAL_FAILURE_EXIT_CODE)


if __name__ == "__main__":
    unittest.main()
