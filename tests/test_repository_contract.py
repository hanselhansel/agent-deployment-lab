import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_required_public_contract_files_exist(self) -> None:
        required_paths = (
            ".gitignore",
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

    def test_generated_and_local_secret_files_are_ignored(self) -> None:
        content = (ROOT / ".gitignore").read_text(encoding="utf-8")

        for pattern in ("__pycache__/", "*.py[cod]", ".env", ".env.*"):
            with self.subTest(pattern=pattern):
                self.assertIn(pattern, content)

    def test_documented_and_ci_tests_use_discovery(self) -> None:
        command = "python3 -m unittest discover -s tests -v"

        for relative_path in ("README.md", ".github/workflows/ci.yml"):
            with self.subTest(relative_path=relative_path):
                content = (ROOT / relative_path).read_text(encoding="utf-8")
                self.assertIn(command, content)

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
