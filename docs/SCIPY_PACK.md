# SciPy Library Pack

KoPy의 SciPy 팩은 SciPy를 다시 구현하지 않습니다. `scipy`/`사이파이` 네임스페이스가 활성화된 코드에서 공개 API 이름만 KoPy 표현과 Python 표현 사이에서 번역하고 실제 계산은 설치된 SciPy가 수행합니다.

## 설치

```powershell
python -m pip install "scipy>=1.18,<1.19"
```

## 예시

```kopy
프롬 사이파이.optimize 임포트 미니마이즈
프롬 사이파이.stats 임포트 지스코어
프롬 사이파이.sparse 임포트 시이에스알매트릭스

결과 = 미니마이즈(lambda x: (x[0] - 3.0) ** 2, [0.0])
점수 = 지스코어([1.0, 2.0, 3.0])
행렬 = 시이에스알매트릭스([[1, 0], [0, 2]])
밀집 = 행렬.토어레이()
```

위 코드는 `scipy.optimize.minimize`, `scipy.stats.zscore`, `scipy.sparse.csr_matrix`, `csr_matrix.toarray`를 호출하는 표준 Python 코드로 변환됩니다.

## 지원 영역

현재 팩은 `optimize`, `stats`, `sparse`, `linalg`, `signal`, `spatial`, `integrate`, `interpolate`, `fft`, `ndimage`, `special`의 자주 쓰는 공개 API를 우선 지원합니다.

`method=`, `bounds=`, `options=`, `axis=`, `dtype=` 같은 키워드 인자는 Python 원형을 유지합니다. 이 이름들은 다른 라이브러리에서도 널리 쓰이므로 전역 번역하면 모호성이 생길 수 있습니다.

## 검증

GitHub Actions의 AI Pack Matrix에서 Windows, Ubuntu, macOS에 실제 SciPy를 설치하고 최적화, 통계, 희소행렬 연산을 실행합니다. 외부 데이터 다운로드는 사용하지 않습니다.
