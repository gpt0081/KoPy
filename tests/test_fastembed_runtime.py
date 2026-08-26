import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("fastembed"), "fastembed is not installed")
class FastEmbedRuntimeTests(unittest.TestCase):
    def test_real_cross_encoder_reranking(self):
        source = (
            "프롬 패스트임베드.rerank.cross_encoder 임포트 텍스트크로스인코더\n"
            "query = 'Who maintains Qdrant FastEmbed?'\n"
            "documents = [\n"
            "    'This sentence is about unrelated weather.',\n"
            "    'FastEmbed is supported by and maintained by Qdrant.',\n"
            "]\n"
            "reranker = 텍스트크로스인코더(model_name='Xenova/ms-marco-MiniLM-L-6-v2')\n"
            "scores = list(reranker.rerank(query, documents))\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        scores = namespace["scores"]
        self.assertEqual(len(scores), 2)
        self.assertGreater(float(scores[1]), float(scores[0]))


if __name__ == "__main__":
    unittest.main()
