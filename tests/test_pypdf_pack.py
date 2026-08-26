import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class PyPdfPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("pypdf")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.module, "pypdf")
        self.assertEqual(pack.kopy_module, "파이피디에프")

    def test_reader_and_extract_text_translate(self):
        source = (
            "프롬 파이피디에프 임포트 피디에프리더\n"
            "리더 = 피디에프리더('document.pdf')\n"
            "텍스트 = '\\n'.join(page.익스트랙트텍스트() or '' for page in 리더.페이지즈)\n"
        )
        python_source = translate(source).python
        self.assertIn("from pypdf import PdfReader", python_source)
        self.assertIn("reader = PdfReader('document.pdf')", python_source)
        self.assertIn("page.extract_text()", python_source)
        self.assertIn("reader.pages", python_source)

    def test_writer_specific_methods_translate(self):
        source = (
            "프롬 파이피디에프 임포트 피디에프라이터\n"
            "라이터 = 피디에프라이터()\n"
            "라이터.애드블랭크페이지(width=612, height=792)\n"
            "라이터.애드메타데이터({'/Title': 'KoPy'})\n"
        )
        python_source = translate(source).python
        self.assertIn("from pypdf import PdfWriter", python_source)
        self.assertIn("writer.add_blank_page(width=612, height=792)", python_source)
        self.assertIn("writer.add_metadata({'/Title': 'KoPy'})", python_source)

    def test_python_spellings_remain_accepted(self):
        source = (
            "프롬 파이피디에프 임포트 피디에프리더\n"
            "reader = 피디에프리더(path)\n"
            "pages = reader.pages\n"
            "metadata = reader.metadata\n"
            "text = pages[0].익스트랙트텍스트()\n"
        )
        python_source = translate(source).python
        self.assertIn("reader = PdfReader(path)", python_source)
        self.assertIn("pages = reader.pages", python_source)
        self.assertIn("metadata = reader.metadata", python_source)
        self.assertIn("text = pages[0].extract_text()", python_source)

    def test_unimported_pack_word_is_not_global(self):
        source = "텍스트 = page.익스트랙트텍스트()\n"
        self.assertEqual(translate(source).python, "text = page.익스트랙트텍스트()\n")

    def test_python_to_kopy_round_trip(self):
        source = (
            "from pypdf import PdfReader, PdfWriter\n"
            "reader = PdfReader(path)\n"
            "text = reader.pages[0].extract_text()\n"
            "writer = PdfWriter()\n"
            "writer.add_blank_page(width=612, height=792)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 파이피디에프 임포트 피디에프리더, 피디에프라이터", kopy)
        self.assertIn("리더 = 피디에프리더(path)", kopy)
        self.assertIn("텍스트 = 리더.페이지즈[0].익스트랙트텍스트()", kopy)
        self.assertIn("라이터 = 피디에프라이터()", kopy)
        self.assertIn("라이터.애드블랭크페이지(width=612, height=792)", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("파이피디에프.익스트랙트텍스트")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "extract_text")


if __name__ == "__main__":
    unittest.main()
