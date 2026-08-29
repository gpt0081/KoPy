import contextlib
import io

from kopy.cli import main


for arguments in (["version"], ["help", "프린트"], ["packs", "numpy"]):
    stdout = io.StringIO()
    stderr = io.StringIO()
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        code = main(list(arguments))
    print(arguments, "종료 코드:", code)
    print(stdout.getvalue().splitlines()[0])
