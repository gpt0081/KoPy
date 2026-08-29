from kopy.translator import to_kopy, translate


python_source = 'for value in range(3):\n    print(value)\n'
kopy_source = to_kopy(python_source).kopy
restored = translate(kopy_source).python

print("[KoPy]")
print(kopy_source, end="")
print("[복원 Python]")
print(restored, end="")
print("안정:", restored == python_source)

assert '"for print"' in to_kopy('print("for print")\n').kopy
