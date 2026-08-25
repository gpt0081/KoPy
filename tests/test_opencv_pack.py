import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class OpenCVPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("opencv")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "cv2")
        self.assertEqual(pack.kopy_module, "오픈씨브이")

    def test_alias_translation_is_namespace_scoped(self):
        source = (
            "임포트 오픈씨브이 애즈 cv2\n"
            "resized = cv2.리사이즈(image, (224, 224))\n"
            "gray = cv2.씨브이티컬러(resized, cv2.COLOR_BGR2GRAY)\n"
            "edges = cv2.캐니(gray, 50, 150)\n"
        )
        python_source = translate(source).python
        self.assertIn("import cv2 as cv2", python_source)
        self.assertIn("cv2.resize(image, (224, 224))", python_source)
        self.assertIn("cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)", python_source)
        self.assertIn("cv2.Canny(gray, 50, 150)", python_source)

    def test_constants_remain_python_native(self):
        source = "임포트 오픈씨브이 애즈 cv\ngray = cv.씨브이티컬러(image, cv.COLOR_BGR2GRAY)\n"
        python_source = translate(source).python
        self.assertIn("cv.COLOR_BGR2GRAY", python_source)

    def test_unimported_word_is_not_global(self):
        source = "result = 리사이즈(image, (4, 4))\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import cv2 as cv\n"
            "resized = cv.resize(image, (32, 32))\n"
            "gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 오픈씨브이 애즈 cv", kopy)
        self.assertIn("cv.리사이즈", kopy)
        self.assertIn("cv.씨브이티컬러", kopy)
        self.assertIn("cv.COLOR_BGR2GRAY", kopy)

    def test_dnn_chain_uses_active_opencv_pack(self):
        source = (
            "임포트 오픈씨브이 애즈 cv2\n"
            "net = cv2.dnn.리드넷프롬오닉스(\"model.onnx\")\n"
            "blob = cv2.dnn.블롭프롬이미지(image, scalefactor=1.0)\n"
            "net.셋인풋(blob)\n"
            "output = net.포워드()\n"
        )
        python_source = translate(source).python
        self.assertIn("cv2.dnn.readNetFromONNX", python_source)
        self.assertIn("cv2.dnn.blobFromImage", python_source)
        self.assertIn("net.setInput(blob)", python_source)
        self.assertIn("net.forward()", python_source)

    def test_help_resolution(self):
        resolved = resolve_pack_member("오픈씨브이.리사이즈")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "resize")

    def test_keyword_arguments_remain_python_spelling(self):
        source = (
            "임포트 오픈씨브이 애즈 cv2\n"
            "blob = cv2.dnn.블롭프롬이미지(image, scalefactor=1.0, size=(224, 224), swapRB=True, crop=False)\n"
        )
        python_source = translate(source).python
        self.assertIn("scalefactor=1.0", python_source)
        self.assertIn("size=(224, 224)", python_source)
        self.assertIn("swapRB=True", python_source)
        self.assertIn("crop=False", python_source)


if __name__ == "__main__":
    unittest.main()
