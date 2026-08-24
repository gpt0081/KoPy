import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("datasets"), "Hugging Face Datasets is not installed")
class DatasetsRuntimeTests(unittest.TestCase):
    def test_kopy_datasets_local_preprocessing_executes_offline(self):
        source = (
            "프롬 데이터셋츠 임포트 데이터셋\n"
            "원본 = 데이터셋.프롬딕트({\"text\": [\"alpha\", \"beta\", \"gamma\", \"delta\"], "
            "\"label\": [0, 1, 0, 1]})\n"
            "가공 = 원본.맵(lambda row: {\"length\": 렌(row[\"text\"])})\n"
            "필터됨 = 가공.필터(lambda row: row[\"length\"] >= 4)\n"
            "분할 = 필터됨.트레인테스트스플릿(test_size=0.5, seed=7)\n"
            "열 = 필터됨.컬럼네임스\n"
            "행수 = 필터됨.넘로우스\n"
        )
        namespace: dict[str, object] = {}
        exec(compile(translate(source).python, "<kopy-datasets-smoke>", "exec"), namespace)

        self.assertIn("length", namespace["열"])
        self.assertEqual(namespace["행수"], 4)
        self.assertEqual(set(namespace["분할"].keys()), {"train", "test"})
        self.assertEqual(namespace["분할"]["train"].num_rows + namespace["분할"]["test"].num_rows, 4)


if __name__ == "__main__":
    unittest.main()
