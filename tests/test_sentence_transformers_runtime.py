import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("sentence_transformers"), "sentence-transformers is not installed")
class SentenceTransformersRuntimeTests(unittest.TestCase):
    def test_real_sentence_transformers_bow_encode_similarity_and_search(self):
        source = (
            "임포트 센텐스트랜스포머스 애즈 st\n"
            "프롬 sentence_transformers.models 임포트 BoW\n"
            "프롬 sentence_transformers.util 임포트 semantic_search\n"
            "vocab = ['hello', 'world', 'kopy']\n"
            "bow = BoW(vocab)\n"
            "model = st.센텐스트랜스포머(modules=[bow])\n"
            "sentences = ['hello world', 'hello kopy', 'world']\n"
            "embeddings = model.인코드(sentences, convert_to_tensor=True)\n"
            "scores = model.시밀래리티(embeddings[:1], embeddings)\n"
            "hits = semantic_search(embeddings[:1], embeddings, top_k=2)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        embeddings = namespace["embeddings"]
        scores = namespace["scores"]
        hits = namespace["hits"]
        self.assertEqual(tuple(embeddings.shape), (3, 3))
        self.assertEqual(tuple(scores.shape), (1, 3))
        self.assertEqual(hits[0][0]["corpus_id"], 0)
        self.assertAlmostEqual(hits[0][0]["score"], 1.0, places=5)
        self.assertEqual(len(hits[0]), 2)


if __name__ == "__main__":
    unittest.main()
