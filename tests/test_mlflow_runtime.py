import importlib.util
import tempfile
import unittest
from pathlib import Path

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("mlflow"), "MLflow is not installed")
class MLflowRuntimeTests(unittest.TestCase):
    def test_kopy_mlflow_local_tracking_executes(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            tracking = (Path(tmpdir) / "mlruns").resolve().as_uri()
            source = (
                "임포트 엠엘플로우 애즈 mlf\n"
                f"mlf.셋트래킹유알아이({tracking!r})\n"
                "mlf.셋익스페리먼트('kopy-runtime')\n"
                "위드 mlf.스타트런(run_name='smoke') 애즈 실행:\n"
                "    mlf.로그파람('learning_rate', 0.01)\n"
                "    mlf.로그메트릭('loss', 0.25)\n"
                "    mlf.셋태그('source', 'kopy')\n"
                "    mlf.로그텍스트('KoPy MLflow runtime test', 'notes.txt')\n"
                "    런아이디값 = 실행.인포.런아이디\n"
                "조회 = mlf.겟런(런아이디값)\n"
                "파라미터값 = 조회.데이터.파람즈['learning_rate']\n"
                "메트릭값 = 조회.데이터.메트릭스['loss']\n"
                "태그값 = 조회.데이터.태그스['source']\n"
            )
            namespace: dict[str, object] = {}
            python_source = translate(source).python
            exec(compile(python_source, "<kopy-mlflow-smoke>", "exec"), namespace)

            self.assertEqual(namespace["파라미터값"], "0.01")
            self.assertAlmostEqual(float(namespace["메트릭값"]), 0.25)
            self.assertEqual(namespace["태그값"], "kopy")
            self.assertTrue(namespace["런아이디값"])


if __name__ == "__main__":
    unittest.main()
