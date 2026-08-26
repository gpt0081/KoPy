import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class SQLiteVecPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("sqlite-vec")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "sqlite_vec")
        self.assertEqual(pack.kopy_module, "에스큐엘라이트벡")

    def test_python_binding_members_translate(self):
        source = (
            "임포트 sqlite3\n"
            "임포트 에스큐엘라이트벡 애즈 sv\n"
            "connection = sqlite3.connect(':memory:')\n"
            "sv.로드(connection)\n"
            "blob = sv.시리얼라이즈플로트32(embedding)\n"
        )
        python_source = translate(source).python
        self.assertIn("import sqlite_vec as sv", python_source)
        self.assertIn("sv.load(connection)", python_source)
        self.assertIn("sv.serialize_float32(embedding)", python_source)

    def test_generic_sqlite_and_search_vocabulary_stays_python(self):
        source = (
            "임포트 에스큐엘라이트벡 애즈 sv\n"
            "sv.로드(connection)\n"
            "rows = connection.execute(query, [embedding]).fetchall()\n"
        )
        python_source = translate(source).python
        self.assertIn("connection.execute(query, [embedding]).fetchall()", python_source)

    def test_unimported_words_are_not_global(self):
        source = "blob = 에스큐엘라이트벡.시리얼라이즈플로트32(embedding)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_round_trip(self):
        source = (
            "import sqlite_vec as sv\n"
            "sv.load(connection)\n"
            "blob = sv.serialize_float32(embedding)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 에스큐엘라이트벡 애즈 sv", kopy)
        self.assertIn("sv.로드(connection)", kopy)
        self.assertIn("sv.시리얼라이즈플로트32(embedding)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("에스큐엘라이트벡.시리얼라이즈플로트32")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "serialize_float32")


if __name__ == "__main__":
    unittest.main()
