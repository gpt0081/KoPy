import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class SentenceTransformersPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("sentence-transformers")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "sentence_transformers")
        self.assertEqual(pack.kopy_module, "센텐스트랜스포머스")

    def test_namespace_scoped_translation(self):
        source = (
            "임포트 센텐스트랜스포머스 애즈 st\n"
            "model = st.센텐스트랜스포머('local-model')\n"
            "embeddings = model.인코드(sentences, convert_to_tensor=True)\n"
            "scores = st.유틸.코사인심(embeddings, embeddings)\n"
            "hits = st.유틸.시맨틱서치(embeddings[:1], embeddings, top_k=2)\n"
        )
        python_source = translate(source).python
        self.assertIn("import sentence_transformers as st", python_source)
        self.assertIn("st.SentenceTransformer('local-model')", python_source)
        self.assertIn("model.encode(sentences, convert_to_tensor=True)", python_source)
        self.assertIn("st.util.cos_sim(embeddings, embeddings)", python_source)
        self.assertIn("st.util.semantic_search(embeddings[:1], embeddings, top_k=2)", python_source)

    def test_unimported_members_are_not_global(self):
        source = "scores = st.유틸.코사인심(a, b)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import sentence_transformers as st\n"
            "scores = st.util.cos_sim(a, b)\n"
            "hits = st.util.semantic_search(a, b, top_k=3)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 센텐스트랜스포머스 애즈 st", kopy)
        self.assertIn("st.유틸.코사인심(a, b)", kopy)
        self.assertIn("st.유틸.시맨틱서치(a, b, top_k=3)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("센텐스트랜스포머스.센텐스트랜스포머")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "SentenceTransformer")

    def test_generic_keywords_remain_python(self):
        source = (
            "임포트 센텐스트랜스포머스 애즈 st\n"
            "embeddings = model.인코드(sentences, batch_size=16, convert_to_tensor=True, normalize_embeddings=True)\n"
        )
        python_source = translate(source).python
        for token in ("batch_size=", "convert_to_tensor=", "normalize_embeddings="):
            self.assertIn(token, python_source)


if __name__ == "__main__":
    unittest.main()
