import unittest

from kopy.editor import diagnose_source, info_payload, word_entries, words_payload
from kopy.words import WORDS


class EditorApiTests(unittest.TestCase):
    def test_word_entries_are_derived_from_canonical_words(self):
        entries = word_entries()
        mapping = {entry["kopy"]: entry["python"] for entry in entries}
        self.assertEqual(mapping, WORDS)
        self.assertEqual(len(entries), len(WORDS))

    def test_words_payload_contains_registry_metadata(self):
        payload = words_payload()
        self.assertEqual(payload["schema"], 1)
        self.assertTrue(payload["words"])
        self.assertIn("kopy_version", payload)
        self.assertIn("python_baseline", payload)

    def test_diagnose_reports_spelling_from_core_logic(self):
        payload = diagnose_source('pritn("hello")\n', "demo.kpy")
        spelling = [d for d in payload["diagnostics"] if d["code"] == "spelling"]
        self.assertEqual(len(spelling), 1)
        self.assertEqual(spelling[0]["found"], "pritn")
        self.assertEqual(spelling[0]["suggestion"], "print")

    def test_diagnose_accepts_kopy_tokens(self):
        payload = diagnose_source('프린트("안녕")\n', "demo.kpy")
        self.assertTrue(payload["ok"])
        self.assertEqual(payload["diagnostics"], [])

    def test_info_payload_reports_runtime(self):
        payload = info_payload()
        self.assertEqual(payload["schema"], 1)
        self.assertIn("runtime_python", payload)


if __name__ == "__main__":
    unittest.main()
