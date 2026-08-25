import importlib.util
import os
import subprocess
import sys
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
        python_source = translate(source).python + (
            "\nassert count == 3\n"
            "assert indices.shape == (1, 2)\n"
            "assert int(indices[0, 0]) == 1\n"
            "assert float(distances[0, 0]) < float(distances[0, 1])\n"
            "print('FAISS_RUNTIME_OK')\n"
        )

        env = os.environ.copy()
        env.setdefault("OMP_NUM_THREADS", "1")
        env.setdefault("OMP_THREAD_LIMIT", "1")
        completed = subprocess.run(
            [sys.executable, "-c", python_source],
            capture_output=True,
            text=True,
            env=env,
            timeout=60,
            check=False,
        )

        self.assertEqual(
            completed.returncode,
            0,
            msg=f"stdout:\n{completed.stdout}\nstderr:\n{completed.stderr}",
        )
        self.assertIn("FAISS_RUNTIME_OK", completed.stdout)


if __name__ == "__main__":
    unittest.main()
