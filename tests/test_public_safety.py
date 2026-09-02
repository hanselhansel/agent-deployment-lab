import tempfile
import unittest
from pathlib import Path

from scripts.check_public_safety import scan


class PublicSafetyTests(unittest.TestCase):
    def test_clean_tree_has_no_findings(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("Synthetic public example.\n")

            self.assertEqual(scan(root), [])

    def test_env_file_and_private_key_marker_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".env").write_text("EXAMPLE=value\n")
            private_key_marker = "-----BEGIN " + "PRIVATE KEY-----"
            (root / "example.pem").write_text(private_key_marker + "\n")

            self.assertEqual(len(scan(root)), 2)


if __name__ == "__main__":
    unittest.main()
