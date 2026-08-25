import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("cv2"), "OpenCV is not installed")
class OpenCVRuntimeTests(unittest.TestCase):
    def test_real_opencv_resize_color_blur_edges_and_contours(self):
        source = (
            "임포트 넘파이 애즈 np\n"
            "임포트 오픈씨브이 애즈 cv2\n"
            "image = np.제로즈((8, 8, 3), dtype=np.uint8)\n"
            "image[2:6, 2:6] = 255\n"
            "resized = cv2.리사이즈(image, (16, 16), interpolation=cv2.INTER_NEAREST)\n"
            "gray = cv2.씨브이티컬러(resized, cv2.COLOR_BGR2GRAY)\n"
            "blurred = cv2.가우시안블러(gray, (3, 3), 0)\n"
            "edges = cv2.캐니(blurred, 50, 150)\n"
            "_, binary = cv2.쓰레시홀드(gray, 127, 255, cv2.THRESH_BINARY)\n"
            "contours, hierarchy = cv2.파인드컨투어스(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        self.assertEqual(namespace["resized"].shape, (16, 16, 3))
        self.assertEqual(namespace["gray"].shape, (16, 16))
        self.assertEqual(namespace["blurred"].shape, (16, 16))
        self.assertEqual(namespace["edges"].shape, (16, 16))
        self.assertGreater(int(namespace["edges"].sum()), 0)
        self.assertEqual(len(namespace["contours"]), 1)
        self.assertGreater(float(namespace["cv2"].contourArea(namespace["contours"][0])), 0.0)


if __name__ == "__main__":
    unittest.main()
