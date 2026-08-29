import io
import tokenize

from kopy.translator import translate


source = '프린트("이프 프린트")  # 이프 프린트\n'
for token in tokenize.generate_tokens(io.StringIO(source).readline):
    if token.type in {tokenize.NAME, tokenize.STRING, tokenize.COMMENT}:
        print(tokenize.tok_name[token.type], repr(token.string))

result = translate(source)
print("변환:", result.python, end="")
print("교체:", result.replacements)
