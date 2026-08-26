import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("usearch"), "usearch is not installed")
class USearchRuntimeTests(unittest.TestCase):
    def test_real_local_vector_search(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "프롬 유서치.index 임포트 인덱스\n"
            "vectors = np.어레이([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype=np.플로트32)\n"
            "keys = np.어레이([10, 20, 30], dtype=np.인트64)\n"
            "query = np.어레이([0.95, 0.05, 0.0], dtype=np.플로트32)\n"
            "index = 인덱스(ndim=3, metric='cos', dtype='f32')\n"
            "index.add(keys, vectors)\n"
            "matches = index.search(query, 2)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        matches = namespace["matches"]
        index = namespace["index"]

        self.assertEqual(len(index), 3)
        self.assertEqual(len(matches), 2)
        self.assertEqual(int(matches[0].key), 10)
        self.assertLess(float(matches[0].distance), float(matches[1].distance))
        self.assertLess(float(matches[0].distance), 0.01)


if __name__ == "__main__":
    unittest.main()
