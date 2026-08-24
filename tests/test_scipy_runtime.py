import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("scipy"), "SciPy is not installed")
class SciPyRuntimeTests(unittest.TestCase):
    def test_real_scipy_optimize_stats_and_sparse(self):
        source = (
            "프롬 사이파이.optimize 임포트 미니마이즈\n"
            "프롬 사이파이.stats 임포트 지스코어\n"
            "프롬 사이파이.sparse 임포트 시이에스알매트릭스\n"
            "결과 = 미니마이즈(lambda x: (x[0] - 3.0) ** 2, [0.0])\n"
            "점수 = 지스코어([1.0, 2.0, 3.0])\n"
            "행렬 = 시이에스알매트릭스([[1, 0], [0, 2]])\n"
            "밀집 = 행렬.토어레이()\n"
        )
        namespace = {}
        exec(translate(source).python, namespace, namespace)

        self.assertTrue(namespace["결과"].success)
        self.assertAlmostEqual(float(namespace["결과"].x[0]), 3.0, places=5)
        self.assertAlmostEqual(float(namespace["점수"].mean()), 0.0, places=12)
        self.assertEqual(namespace["행렬"].nnz, 2)
        self.assertEqual(namespace["밀집"].tolist(), [[1, 0], [0, 2]])


if __name__ == "__main__":
    unittest.main()
