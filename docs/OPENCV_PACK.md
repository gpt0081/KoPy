# OpenCV Library Pack

KoPy 0.5.20의 OpenCV 팩은 Python 패키지 `opencv-python`/`opencv-python-headless`가 제공하는 `cv2` 모듈을 namespace-scoped 방식으로 음역합니다. OpenCV 자체를 재구현하지 않으며 실제 이미지·영상 처리는 upstream OpenCV가 담당합니다.

## 설치

일반 데스크톱 환경:

```powershell
python -m pip install opencv-python
```

GUI가 필요 없는 서버·CI 환경:

```powershell
python -m pip install opencv-python-headless
```

OpenCV 패키지들은 모두 같은 `cv2` namespace를 제공하므로 한 환경에 여러 변형을 동시에 설치하지 않는 것을 권장합니다.

## 기본 예제

```kopy
임포트 오픈씨브이 애즈 cv2

image = cv2.이미리드("photo.jpg")
resized = cv2.리사이즈(image, (224, 224))
gray = cv2.씨브이티컬러(resized, cv2.COLOR_BGR2GRAY)
edges = cv2.캐니(gray, 50, 150)
cv2.이미라이트("edges.png", edges)
```

위 코드는 다음 표준 Python 흐름으로 변환됩니다.

```python
import cv2

image = cv2.imread("photo.jpg")
resized = cv2.resize(image, (224, 224))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
cv2.imwrite("edges.png", edges)
```

## 지원 범위

주요 범위는 다음과 같습니다.

- 이미지 입출력: `imread`, `imwrite`
- 변환: `resize`, `cvtColor`, `flip`, `rotate`, affine/perspective warp
- 필터: `GaussianBlur`, `medianBlur`, `bilateralFilter`
- 엣지·임계값·형태학: `Canny`, `threshold`, `adaptiveThreshold`, `Sobel`, `morphologyEx`, `erode`, `dilate`
- 윤곽선·기하: `findContours`, `contourArea`, `arcLength`, `boundingRect`, `approxPolyDP`
- 그리기: `line`, `rectangle`, `circle`, `polylines`, `putText`
- 영상 I/O: `VideoCapture`, `VideoWriter`, `read`, `release`
- DNN: `readNet`, `readNetFromONNX`, `blobFromImage`, `setInput`, `forward`

전체 목록은 `kopy packs opencv`로 확인할 수 있습니다.

## Python 표현을 일부러 남기는 부분

KoPy의 목적은 OpenCV 원문 코드를 가리는 것이 아니라 원문 Python/OpenCV 코드를 읽는 능력으로 연결하는 것입니다. 따라서 다음은 의도적으로 Python 원형을 유지합니다.

- `cv2.COLOR_BGR2GRAY`, `cv2.INTER_AREA`, `cv2.THRESH_BINARY`, `cv2.RETR_EXTERNAL` 같은 OpenCV 상수
- `interpolation=`, `scalefactor=`, `size=`, `swapRB=`, `crop=`, `thickness=` 같은 키워드 인자
- `image`, `gray`, `edges`, `frame`, `cap`처럼 OpenCV 학습 자료에서 자주 보는 변수명

이 원칙은 상수·키워드·관례를 원문 코드와 바로 대응해 익히기 위한 것입니다.

## 충돌 방지

`리사이즈`, `노멀라이즈`, `스플릿`, `리드`, `겟`, `셋`처럼 다른 라이브러리에서도 등장할 수 있는 이름은 Core 전역 번역에 추가하지 않습니다. `cv2`/`오픈씨브이`가 import되어 활성화된 경우에만 OpenCV 팩의 어휘로 해석됩니다. 여러 활성 팩 사이에서 뜻이 모호하면 KoPy는 임의로 추측하지 않습니다.

## CI

KoPy의 AI Pack Matrix에서는 GUI 의존성이 없는 `opencv-python-headless`를 Windows, Ubuntu, macOS에 실제 설치한 뒤 NumPy 배열을 이용해 `resize`, `cvtColor`, `GaussianBlur`, `Canny`, `threshold`, `findContours`를 실행하고 결과를 검증합니다.
