import importlib.util
import io
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("pypdf"), "pypdf is not installed")
class PyPdfRuntimeTests(unittest.TestCase):
    def _build_pdf_with_text(self):
        from pypdf import PdfWriter
        from pypdf.generic import DecodedStreamObject, DictionaryObject, NameObject

        writer = PdfWriter()
        page = writer.add_blank_page(width=300, height=200)

        font = DictionaryObject({
            NameObject("/Type"): NameObject("/Font"),
            NameObject("/Subtype"): NameObject("/Type1"),
            NameObject("/BaseFont"): NameObject("/Helvetica"),
        })
        font_ref = writer._add_object(font)
        page[NameObject("/Resources")] = DictionaryObject({
            NameObject("/Font"): DictionaryObject({NameObject("/F1"): font_ref})
        })

        content = DecodedStreamObject()
        content.set_data(b"BT /F1 12 Tf 20 100 Td (KoPy RAG PDF ingestion) Tj ET")
        page[NameObject("/Contents")] = writer._add_object(content)

        stream = io.BytesIO()
        writer.write(stream)
        stream.seek(0)
        return stream

    def test_real_pdf_reader_and_text_extraction(self):
        pdf_stream = self._build_pdf_with_text()
        source = (
            "프롬 파이피디에프 임포트 피디에프리더\n"
            "reader = 피디에프리더(pdf_stream)\n"
            "page_count = len(reader.pages)\n"
            "text = reader.pages[0].익스트랙트텍스트()\n"
        )
        namespace = {"pdf_stream": pdf_stream}
        exec(translate(source).python, namespace)

        self.assertEqual(namespace["page_count"], 1)
        self.assertIn("KoPy RAG PDF ingestion", namespace["text"])


if __name__ == "__main__":
    unittest.main()
