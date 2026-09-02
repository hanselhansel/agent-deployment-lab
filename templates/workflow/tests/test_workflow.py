import sys
import unittest
from pathlib import Path


WORKFLOW_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKFLOW_ROOT / "src"))

from workflow import process_case  # noqa: E402


class WorkflowTests(unittest.TestCase):
    def test_complete_case_fails_closed_without_evaluated_automation(self) -> None:
        result = process_case(
            {"case_id": "synthetic-1", "summary": "Synthetic review request."}
        )

        self.assertEqual(
            result,
            {
                "status": "needs_human",
                "reason": "starter has no evaluated automation",
            },
        )

    def test_missing_summary_names_the_missing_field(self) -> None:
        result = process_case({"case_id": "synthetic-1"})

        self.assertEqual(result["status"], "needs_human")
        self.assertEqual(result["missing_fields"], ["summary"])


if __name__ == "__main__":
    unittest.main()
