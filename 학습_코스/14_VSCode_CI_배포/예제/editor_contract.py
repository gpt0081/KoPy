from kopy.editor import diagnose_source, info_payload, words_payload


info = info_payload()
words = words_payload()
diagnosis = diagnose_source('프린트("ok")\n', "sample.kpy")

print("정보 스키마:", info["schema"])
print("단어 스키마:", words["schema"])
print("단어 수:", len(words["words"]))
print("진단 스키마:", diagnosis["schema"])
print("정상:", diagnosis["ok"])
