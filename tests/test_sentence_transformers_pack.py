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
            "모델 = st.센텐스트랜스포머('local-model')\n"
            "임베딩즈 = 모델.인코드(sentences, convert_to_tensor=True)\n"
            "스코어즈 = 모델.시밀래리티(임베딩즈, 임베딩즈)\n"
        )
        python_source = translate(source).python
        self.assertIn("import sentence_transformers as st", python_source)
        self.assertIn("model = st.SentenceTransformer('local-model')", python_source)
        self.assertIn("embeddings = model.encode(sentences, convert_to_tensor=True)", python_source)
        self.assertIn("scores = model.similarity(embeddings, embeddings)", python_source)

    def test_dotted_submodule_paths_remain_python_native(self):
        source = (
            "임포트 센텐스트랜스포머스 애즈 st\n"
            "프롬 sentence_transformers.models 임포트 BoW\n"
            "프롬 sentence_transformers.util 임포트 semantic_search\n"
        )
        python_source = translate(source).python
        self.assertIn("from sentence_transformers.models import BoW", python_source)
        self.assertIn("from sentence_transformers.util import semantic_search", python_source)

    def test_unimported_members_are_not_global(self):
        source = "embeddings = model.인코드(sentences)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import sentence_transformers as st\n"
            "model = st.SentenceTransformer('local-model')\n"
            "embeddings = model.encode(sentences)\n"
            "scores = model.similarity(embeddings, embeddings)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 센텐스트랜스포머스 애즈 st", kopy)
        self.assertIn("모델 = st.센텐스트랜스포머('local-model')", kopy)
        self.assertIn("임베딩즈 = 모델.인코드(sentences)", kopy)
        self.assertIn("스코어즈 = 모델.시밀래리티(임베딩즈, 임베딩즈)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("센텐스트랜스포머스.센텐스트랜스포머")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "SentenceTransformer")

    def test_generic_keywords_remain_python(self):
        source = (
            "임포트 센텐스트랜스포머스 애즈 st\n"
            "임베딩즈 = 모델.인코드(sentences, batch_size=16, convert_to_tensor=True, normalize_embeddings=True)\n"
        )
        python_source = translate(source).python
        for token in ("batch_size=", "convert_to_tensor=", "normalize_embeddings="):
            self.assertIn(token, python_source)


if __name__ == "__main__":
    unittest.main()
