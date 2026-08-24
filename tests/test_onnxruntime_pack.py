import unittest

from kopy.translator import to_kopy, translate


class OnnxRuntimePackTests(unittest.TestCase):
    def test_translate_inference_session_api(self):
        source = (
            "임포트 온엑스런타임 애즈 ort\n"
            "세션 = ort.인퍼런스세션('model.onnx', providers=ort.겟어베일러블프로바이더스())\n"
            "입력이름 = 세션.겟인풋스()[0].name\n"
            "출력이름 = 세션.겟아웃풋스()[0].name\n"
            "결과 = 세션.런([출력이름], {입력이름: 값})\n"
        )
        result = translate(source).python
        self.assertIn("import onnxruntime as ort", result)
        self.assertIn("ort.InferenceSession", result)
        self.assertIn("ort.get_available_providers()", result)
        self.assertIn("세션.get_inputs()", result)
        self.assertIn("세션.get_outputs()", result)
        self.assertIn("세션.run([출력이름]", result)

    def test_reverse_translate_onnxruntime_api(self):
        source = (
            "import onnxruntime as ort\n"
            "options = ort.SessionOptions()\n"
            "options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL\n"
            "session = ort.InferenceSession('model.onnx', sess_options=options)\n"
            "outputs = session.run(None, {'x': values})\n"
        )
        result = to_kopy(source).kopy
        self.assertIn("임포트 온엑스런타임 애즈 ort", result)
        self.assertIn("ort.세션옵션스()", result)
        self.assertIn("ort.그래프옵티마이제이션레벨.인에이블올", result)
        self.assertIn("ort.인퍼런스세션", result)
        self.assertIn("session.런(None", result)


if __name__ == "__main__":
    unittest.main()
