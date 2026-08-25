import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("faiss"), "faiss is not installed")
class FaissRuntimeTests(unittest.TestCase):
    def test_real_flat_l2_search(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "임포트 파이스 애즈 faiss\n"
            "vectors = np.어레이([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]], dtype=np.플로트32)\n"
            "query = np.어레이([[1.1, 1.0]], dtype=np.플로트32)\n"
            "index = faiss.인덱스플랫엘투(2)\n"
            "index.add(vectors)\n"
            "distances, indices = index.search(query, 2)\n"
            "count = index.ntotal\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        self.assertEqual(namespace["count"], 3)
        self.assertEqual(namespace["indices"].shape, (1, 2))
        self.assertEqual(namespace["indices"][0, 0], 1)
        self.assertLess(float(namespace["distances"][0, 0]), float(namespace["distances"][0, 1]))


if __name__ == "__main__":
    unittest.main()
