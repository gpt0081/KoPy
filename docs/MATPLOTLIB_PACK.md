# Matplotlib Pack

KoPy의 Matplotlib 팩은 Matplotlib 자체를 다시 구현하지 않습니다. `matplotlib`이 import된 파일에서만 주요 API 이름을 KoPy 음역과 Python 원형 사이에서 번역하며, 실제 Figure/Axes 생성과 렌더링은 설치된 Matplotlib이 담당합니다.

지원 모듈 이름은 `matplotlib`, `맷플롯립`이고 일반적인 `plt` 별칭을 인식합니다. `matplotlib.pyplot`의 `plot`, `scatter`, `bar`, `hist`, `imshow`, `subplots`, `savefig`, 제목·축 라벨·범례·grid 계열과 Figure/Axes 객체의 대표 메서드를 지원합니다.

```kopy
임포트 맷플롯립.pyplot 애즈 plt

에폭 = [1, 2, 3, 4]
손실 = [1.0, 0.7, 0.5, 0.35]

피겨, 축 = plt.서브플롯츠()
축.플롯(에폭, 손실, marker="o", label="loss")
축.셋타이틀("Training loss")
축.셋엑스라벨("Epoch")
축.셋와이라벨("Loss")
축.레전드()
피겨.세이브피그("loss.png")
plt.클로즈(피겨)
```

위 코드는 핵심적으로 다음 Python API로 번역됩니다.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(..., marker="o", label="loss")
ax.set_title("Training loss")
fig.savefig("loss.png")
plt.close(fig)
```

## 설치

KoPy 팩과 실제 Matplotlib은 별개입니다.

```bash
python -m pip install "matplotlib>=3.11,<3.12"
```

## 충돌 방지

`marker=`, `label=`, `figsize=`, `dpi=`, `cmap=` 같은 키워드 인자는 Python 원형을 유지합니다. 이런 이름은 라이브러리와 함수 문맥에 따라 의미가 달라질 수 있으므로 KoPy Core 전역 단어표에 넣지 않습니다.

또한 Matplotlib 팩은 import된 파일에서만 활성화됩니다. 따라서 Matplotlib을 import하지 않은 파일의 `플롯`, `스캐터` 같은 사용자 식별자는 자동으로 바뀌지 않습니다.
