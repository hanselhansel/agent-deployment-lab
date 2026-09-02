import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_required_public_contract_files_exist(self) -> None:
        required_paths = (
            "README.md",
            "AGENTS.md",
            "LICENSE",
            "SECURITY.md",
            "PROMOTION_CHECKLIST.md",
            "templates/workflow/README.md",
            "templates/workflow/manifest.yml",
            "templates/workflow/sample-data/input.json",
            "templates/workflow/src/workflow.py",
            "templates/workflow/tests/test_workflow.py",
        )

        missing = [path for path in required_paths if not (ROOT / path).is_file()]

        self.assertEqual(missing, [])

    def test_promotion_checklist_names_all_evidence_gates(self) -> None:
        checklist = (ROOT / "PROMOTION_CHECKLIST.md").read_text()

        for gate in ("Defensible", "Safe", "Runnable", "Tested", "Useful", "Shareable"):
            with self.subTest(gate=gate):
                self.assertIn(gate, checklist)

    def test_manifest_declares_required_evidence_fields(self) -> None:
        manifest = (ROOT / "templates/workflow/manifest.yml").read_text()

        for key in ("evidence:", "limitations:", "human_fallback:", "reproduction:"):
            with self.subTest(key=key):
                self.assertIn(key, manifest)


if __name__ == "__main__":
    unittest.main()
