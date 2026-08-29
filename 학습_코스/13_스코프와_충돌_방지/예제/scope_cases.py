from kopy.translator import translate


cases = {
    "팩 활성화": "임포트 넘파이 애즈 np\n값 = np.어레이([1, 2])\n",
    "팩 미활성": "값 = np.어레이([1, 2])\n",
    "PEFT 호출 키워드": "프롬 페프트 임포트 로라컨피그\n설정 = 로라컨피그(로라_알파=16)\n",
    "현재 callee 한계": "프롬 페프트 임포트 로라컨피그\n값 = 다른함수(로라_알파=16)\n",
    "원문 유지 예외": "프롬 헤이스택 임포트 파이프라인\n값 = 파이프라인(top_k=3)\n",
}

for title, source in cases.items():
    print(f"[{title}]")
    print(translate(source).python, end="")
