"""Official OpenCV library pack for KoPy.

Covers common image loading, transformation, filtering, edge detection, drawing,
contours, video I/O and DNN helpers. Actual computer-vision execution remains
upstream OpenCV through the ``cv2`` Python module.
"""

from __future__ import annotations

from .base import LibraryPack


OPENCV_PACK = LibraryPack(
    name="opencv",
    module="cv2",
    kopy_module="오픈씨브이",
    preferred_aliases=("cv2", "cv"),
    description="이미지·영상 전처리와 컴퓨터비전을 위한 OpenCV(cv2) API 팩",
    members={
        # Image I/O and transforms
        "이미리드": "imread",
        "이미라이트": "imwrite",
        "리사이즈": "resize",
        "씨브이티컬러": "cvtColor",
        "플립": "flip",
        "로테이트": "rotate",
        "워프어파인": "warpAffine",
        "워프퍼스펙티브": "warpPerspective",
        "겟로테이션매트릭스투디": "getRotationMatrix2D",
        "겟퍼스펙티브트랜스폼": "getPerspectiveTransform",

        # Filtering / morphology / thresholding
        "가우시안블러": "GaussianBlur",
        "미디안블러": "medianBlur",
        "블러": "blur",
        "빌래터럴필터": "bilateralFilter",
        "쓰레시홀드": "threshold",
        "어댑티브쓰레시홀드": "adaptiveThreshold",
        "캐니": "Canny",
        "소벨": "Sobel",
        "라플라시안": "Laplacian",
        "모폴로지익스": "morphologyEx",
        "이로드": "erode",
        "딜레이트": "dilate",
        "겟스트럭처링엘리먼트": "getStructuringElement",

        # Array / color utilities
        "노멀라이즈": "normalize",
        "스플릿": "split",
        "머지": "merge",
        "인레인지": "inRange",
        "비트와이즈앤드": "bitwise_and",
        "비트와이즈오알": "bitwise_or",
        "비트와이즈엑스오알": "bitwise_xor",
        "비트와이즈낫": "bitwise_not",
        "애드웨이티드": "addWeighted",

        # Geometry / contours / features
        "파인드컨투어스": "findContours",
        "드로우컨투어스": "drawContours",
        "컨투어에어리어": "contourArea",
        "아크렝스": "arcLength",
        "바운딩렉트": "boundingRect",
        "미니어리어렉트": "minAreaRect",
        "어프록스폴리디피": "approxPolyDP",
        "모멘츠": "moments",
        "굿피처스토트랙": "goodFeaturesToTrack",

        # Drawing / annotation
        "라인": "line",
        "렉탱글": "rectangle",
        "서클": "circle",
        "폴리라인즈": "polylines",
        "풋텍스트": "putText",

        # Video I/O
        "비디오캡처": "VideoCapture",
        "비디오라이터": "VideoWriter",
        "비디오라이터포씨씨": "VideoWriter_fourcc",
        "아이즈오픈드": "isOpened",
        "리드": "read",
        "릴리즈": "release",
        "겟": "get",
        "셋": "set",

        # DNN helpers exposed by cv2/dnn objects
        "리드넷": "readNet",
        "리드넷프롬오닉스": "readNetFromONNX",
        "블롭프롬이미지": "blobFromImage",
        "셋인풋": "setInput",
        "포워드": "forward",
    },
    member_descriptions={
        "imread": "이미지 파일을 NumPy 배열로 읽습니다.",
        "resize": "이미지 크기를 변경합니다.",
        "cvtColor": "색상 공간을 변환합니다.",
        "GaussianBlur": "가우시안 블러를 적용합니다.",
        "Canny": "Canny 엣지 검출을 수행합니다.",
        "findContours": "이진 이미지에서 윤곽선을 찾습니다.",
        "VideoCapture": "카메라 또는 영상 파일 입력을 엽니다.",
        "readNetFromONNX": "ONNX 네트워크를 OpenCV DNN으로 읽습니다.",
    },
    examples={
        "resize": (
            "임포트 오픈씨브이 애즈 cv2\nresized = cv2.리사이즈(image, (224, 224))",
            "import cv2\nresized = cv2.resize(image, (224, 224))",
        ),
        "cvtColor": (
            "임포트 오픈씨브이 애즈 cv2\ngray = cv2.씨브이티컬러(image, cv2.COLOR_BGR2GRAY)",
            "import cv2\ngray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)",
        ),
        "Canny": (
            "임포트 오픈씨브이 애즈 cv2\nedges = cv2.캐니(gray, 50, 150)",
            "import cv2\nedges = cv2.Canny(gray, 50, 150)",
        ),
    },
)
