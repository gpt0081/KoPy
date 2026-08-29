from kopy.editor import diagnose_source, info_payload, words_payload
from kopy.education import explain_source


source = '값 = 1\n이프 값:\n    프린트("ok")\n'
print("설명:", explain_source(source))
print("진단:", diagnose_source(source, "sample.kpy"))
print("Core 단어 수:", len(words_payload()["words"]))
print("정보 스키마:", info_payload()["schema"])
