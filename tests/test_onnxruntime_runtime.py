import importlib.util
import tempfile
import unittest
from pathlib import Path

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("onnxruntime"), "ONNX Runtime is not installed")
@unittest.skipUnless(importlib.util.find_spec("onnx"), "ONNX is not installed")
@unittest.skipUnless(importlib.util.find_spec("numpy"), "NumPy is not installed")
class OnnxRuntimeRuntimeTests(unittest.TestCase):
    def test_kopy_onnxruntime_executes_tiny_add_model(self):
        import onnx
        from onnx import TensorProto, helper

        x = helper.make_tensor_value_info("x", TensorProto.FLOAT, [None, 2])
        y = helper.make_tensor_value_info("y", TensorProto.FLOAT, [None, 2])
        z = helper.make_tensor_value_info("z", TensorProto.FLOAT, [None, 2])
        node = helper.make_node("Add", ["x", "y"], ["z"])
        graph = helper.make_graph([node], "kopy_add", [x, y], [z])
        model = helper.make_model(
            graph,
            producer_name="kopy-test",
            opset_imports=[helper.make_opsetid("", 18)],
        )
        model.ir_version = 9
        onnx.checker.check_model(model)

        with tempfile.TemporaryDirectory() as tmpdir:
            model_path = Path(tmpdir) / "add.onnx"
            onnx.save(model, model_path)
            source = (
                "임포트 온엑스런타임 애즈 ort\n"
                "임포트 넘파이 애즈 np\n"
                f"세션 = ort.인퍼런스세션({str(model_path)!r}, providers=['CPUExecutionProvider'])\n"
                "입력들 = 세션.겟인풋스()\n"
                "출력들 = 세션.겟아웃풋스()\n"
                "a = np.어레이([[1.0, 2.0]], np.플로트32)\n"
                "b = np.어레이([[3.0, 4.0]], np.플로트32)\n"
                "결과 = 세션.런(None, {입력들[0].name: a, 입력들[1].name: b})[0]\n"
                "프로바이더 = 세션.겟프로바이더스()\n"
            )
            namespace: dict[str, object] = {}
            exec(compile(translate(source).python, "<kopy-onnxruntime-smoke>", "exec"), namespace)

        result = namespace["결과"]
        self.assertEqual(result.shape, (1, 2))
        self.assertEqual(result.tolist(), [[4.0, 6.0]])
        self.assertIn("CPUExecutionProvider", namespace["프로바이더"])


if __name__ == "__main__":
    unittest.main()
