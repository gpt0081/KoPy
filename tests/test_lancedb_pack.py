import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class LanceDBPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("lancedb")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "lancedb")
        self.assertEqual(pack.kopy_module, "랜스디비")

    def test_lancedb_specific_types_translate(self):
        source = (
            "프롬 랜스디비.pydantic 임포트 랜스모델, 벡터\n"
            "프롬 랜스디비.rerankers 임포트 알알에프리랭커\n"
        )
        python_source = translate(source).python
        self.assertIn("from lancedb.pydantic import LanceModel, Vector", python_source)
        self.assertIn("from lancedb.rerankers import RRFReranker", python_source)

    def test_python_spellings_remain_accepted(self):
        source = (
            "임포트 랜스디비 애즈 ldb\n"
            "db = ldb.connect(path)\n"
            "table = db.create_table('docs', data=documents, mode='overwrite')\n"
            "results = table.search(query).limit(5).to_list()\n"
            "table.add(documents)\n"
        )
        python_source = translate(source).python
        self.assertIn("import lancedb as ldb", python_source)
        for token in (
            "ldb.connect(", "db.create_table(", "table.search(", ".limit(5)",
            ".to_list()", "table.add(", "data=", "mode=",
        ):
            self.assertIn(token, python_source)

    def test_unimported_lancedb_words_are_not_pack_global(self):
        source = "reranker = lib.알알에프리랭커()\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy_transliterates_common_search_vocabulary(self):
        source = (
            "import lancedb as ldb\n"
            "from lancedb.rerankers import RRFReranker\n"
            "db = ldb.connect(path)\n"
            "results = table.search(query).limit(5).to_list()\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 랜스디비 애즈 ldb", kopy)
        self.assertIn("프롬 랜스디비.rerankers 임포트 알알에프리랭커", kopy)
        self.assertIn("ldb.connect(path)", kopy)
        self.assertIn("리절츠 = table.search(쿼리).limit(5).to_list()", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("랜스디비.알알에프리랭커")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "RRFReranker")


if __name__ == "__main__":
    unittest.main()
