from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import re
import unittest
from pathlib import Path

from kopy import PYTHON_BASELINE, __version__
from kopy.packs.registry import all_packs
from kopy.runtime import compile_source

from 학습_코스.course_testkit import capture_kopy


ROOT = Path(__file__).resolve().parents[2]
COURSE = ROOT / "학습_코스"
LESSON_NAMES = [
    "00_KoPy와_Python",
    "01_값과_자료형",
    "02_조건문과_반복문",
    "03_함수와_스코프",
    "04_자료구조와_컴프리헨션",
    "05_문자열과_파일",
    "06_예외와_클래스",
    "07_모듈과_테스트",
    "08_토큰_번역기",
    "09_역변환과_왕복_변환",
    "10_CLI와_학습도구",
    "11_진단과_편집기_API",
    "12_라이브러리_팩",
    "13_스코프와_충돌_방지",
    "14_VSCode_CI_배포",
    "15_종합_연습",
]
OPTIONAL_RUNTIME_LESSONS = {"12_라이브러리_팩", "13_스코프와_충돌_방지"}
EXPECTED_CORE_MODULES = {
    "__init__",
    "__main__",
    "cli",
    "config",
    "editor",
    "education",
    "runtime",
    "spelling",
    "translator",
    "words",
    "packs.base",
    "packs.registry",
}
FORBIDDEN_FRAMES = (
    "\uace0\ubb34",
    "\uc7ac\uace0",
    "\ubc1c\uc8fc",
    "\uacbd\uc9c4\ucf00\ubbf8\uce7c",
    "\uacbd\uc9c4\ucf10\ud14d",
)
MARKDOWN_LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _capture_python(path: Path) -> str:
    source = path.read_text(encoding="utf-8")
    code = compile(source, str(path), "exec")
    output = io.StringIO()
    namespace = {"__name__": "__main__", "__file__": str(path), "__package__": None}
    with contextlib.redirect_stdout(output):
        exec(code, namespace, namespace)
    return output.getvalue()


def _load_test_module(path: Path):
    name = "course_solution_test_" + "_".join(path.relative_to(COURSE).parts).replace(".", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CourseStructureTests(unittest.TestCase):
    def test_manifest_matches_core(self):
        manifest = json.loads((COURSE / "COURSE_MANIFEST.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["kopy_version"], __version__)
        self.assertEqual(manifest["python_baseline"], PYTHON_BASELINE)
        self.assertEqual(manifest["pack_count"], len(all_packs()))
        self.assertEqual(manifest["lesson_count"], len(LESSON_NAMES))
        self.assertEqual(set(manifest["covered_core_modules"]), EXPECTED_CORE_MODULES)

    def test_lesson_structure(self):
        actual = sorted(path.name for path in COURSE.iterdir() if path.is_dir() and re.match(r"^\d{2}_", path.name))
        self.assertEqual(actual, sorted(LESSON_NAMES))
        for name in LESSON_NAMES:
            lesson = COURSE / name
            with self.subTest(lesson=name):
                self.assertTrue((lesson / "README.md").is_file())
                example_dir = lesson / "예제"
                self.assertTrue(example_dir.is_dir())
                kopy_stems = {path.stem for path in example_dir.glob("*.kpy")}
                python_stems = {path.stem for path in example_dir.glob("*.py")}
                self.assertTrue(kopy_stems & python_stems, "KoPy/Python 대응 예제가 필요합니다.")
                if name != "15_종합_연습":
                    self.assertTrue((lesson / "문제" / "test_exercise.py").is_file())
                    self.assertTrue((lesson / "정답" / "test_solution.py").is_file())

    def test_no_unrelated_domain_frame(self):
        for path in COURSE.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".py", ".kpy", ".json", ".txt"}:
                continue
            text = path.read_text(encoding="utf-8")
            for forbidden in FORBIDDEN_FRAMES:
                with self.subTest(path=path, forbidden=forbidden):
                    self.assertNotIn(forbidden, text)

    def test_root_readme_links_course(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("학습_코스/README.md", readme)

    def test_internal_markdown_links_exist(self):
        missing: list[str] = []
        for path in COURSE.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK.findall(text):
                target = raw_target.split("#", 1)[0]
                if not target or "://" in target or target.startswith("mailto:"):
                    continue
                resolved = path.parent / target
                if not resolved.exists():
                    missing.append(f"{path.relative_to(ROOT)} → {raw_target}")
        self.assertEqual(missing, [])


class CourseExecutionTests(unittest.TestCase):
    def test_all_examples_and_solutions_compile(self):
        targets = list(COURSE.glob("[0-9][0-9]_*/예제/*.kpy"))
        targets.extend(COURSE.rglob("정답/*.kpy"))
        for path in sorted(set(targets)):
            with self.subTest(path=path.relative_to(ROOT)):
                source = path.read_text(encoding="utf-8")
                compile_source(source, str(path), spelling=False)

    def test_core_example_pairs_have_same_output(self):
        for lesson_name in LESSON_NAMES:
            if lesson_name in OPTIONAL_RUNTIME_LESSONS:
                continue
            example_dir = COURSE / lesson_name / "예제"
            for kopy_path in example_dir.glob("*.kpy"):
                python_path = kopy_path.with_suffix(".py")
                if not python_path.exists():
                    continue
                with self.subTest(lesson=lesson_name, example=kopy_path.name):
                    self.assertEqual(capture_kopy(kopy_path), _capture_python(python_path))

    def test_reference_solution_suites_pass(self):
        failures: list[str] = []
        test_paths = sorted(COURSE.rglob("정답/test_solution.py"))
        self.assertGreaterEqual(len(test_paths), 16)
        for path in test_paths:
            module = _load_test_module(path)
            suite = unittest.defaultTestLoader.loadTestsFromModule(module)
            output = io.StringIO()
            result = unittest.TextTestRunner(stream=output, verbosity=1).run(suite)
            if not result.wasSuccessful():
                failures.append(f"{path.relative_to(ROOT)}\n{output.getvalue()}")
        self.assertEqual(failures, [])

    def test_pack_registry_is_teachable(self):
        packs = all_packs()
        self.assertEqual(len(packs), 51)
        for pack in packs:
            with self.subTest(pack=pack.name):
                self.assertTrue(pack.name)
                self.assertTrue(pack.module)
                self.assertTrue(pack.kopy_module)
                self.assertTrue(pack.description)
                self.assertTrue(pack.members)


if __name__ == "__main__":
    unittest.main()
