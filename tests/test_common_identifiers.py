import unittest

from kopy.translator import to_kopy, translate
from kopy.words import COMMON_IDENTIFIERS, info_for


class CommonIdentifierTests(unittest.TestCase):
    def test_ml_identifiers_translate_to_python(self):
        source = (
            "엑스_트레인, 엑스_테스트, 와이_트레인, 와이_테스트 = split(엑스, 와이)\n"
            "모델.핏(엑스_트레인, 와이_트레인)\n"
            "프레즈 = 모델.프리딕트(엑스_테스트)\n"
            "타깃 = 와이_테스트\n"
        )
        python_source = translate(source).python
        self.assertIn("X_train, X_test, y_train, y_test = split(X, y)", python_source)
        self.assertIn("model.fit(X_train, y_train)", python_source)
        self.assertIn("preds = model.predict(X_test)", python_source)
        self.assertIn("target = y_test", python_source)

    def test_rag_identifiers_translate_to_python(self):
        source = (
            "임베딩즈 = encoder(다큐먼츠)\n"
            "인덱스 = build(임베딩즈)\n"
            "리트리버 = make_retriever(인덱스)\n"
            "리절츠 = 리트리버.search(쿼리)\n"
            "리스폰스 = answer(리절츠, 레퍼런스)\n"
        )
        python_source = translate(source).python
        for expected in (
            "embeddings = encoder(documents)",
            "index = build(embeddings)",
            "retriever = make_retriever(index)",
            "results = retriever.search(query)",
            "response = answer(results, reference)",
        ):
            self.assertIn(expected, python_source)

    def test_extended_rag_identifiers_translate_both_directions(self):
        source = (
            "클라이언트 = make_client()\n"
            "컬렉션 = 클라이언트.get_collection()\n"
            "파이프라인 = build_pipeline()\n"
            "리절트 = 컬렉션.query(쿼리_임베딩즈=임베딩즈, 엔_리절츠=2)\n"
            "리절츠 = encode(아이디즈, 쇼_프로그레스=펄스)\n"
        )
        python_source = translate(source).python
        self.assertIn("client = make_client()", python_source)
        self.assertIn("collection = client.get_collection()", python_source)
        self.assertIn("pipeline = build_pipeline()", python_source)
        self.assertIn("query_embeddings=embeddings", python_source)
        self.assertIn("n_results=2", python_source)
        self.assertIn("encode(ids, show_progress=False)", python_source)

        kopy = to_kopy(python_source).kopy
        for expected in (
            "클라이언트 = make_client()",
            "컬렉션 = 클라이언트.get_collection()",
            "파이프라인 = build_pipeline()",
            "쿼리_임베딩즈=임베딩즈",
            "엔_리절츠=2",
            "아이디즈, 쇼_프로그레스=펄스",
        ):
            self.assertIn(expected, kopy)

    def test_python_to_kopy_common_identifiers(self):
        source = (
            "X_train = scaler.fit(X_train)\n"
            "predictions = model.predict(X_test)\n"
            "edge_index = graph.edge_index\n"
            "embeddings = encoder(query)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("엑스_트레인 = 스케일러.핏(엑스_트레인)", kopy)
        self.assertIn("프레딕션즈 = 모델.프리딕트(엑스_테스트)", kopy)
        self.assertIn("엣지_인덱스 = graph.엣지_인덱스", kopy)
        self.assertIn("임베딩즈 = encoder(쿼리)", kopy)

    def test_import_paths_are_protected_from_common_identifier_rewrites(self):
        source = (
            "from usearch.index import Index\n"
            "index = Index(ndim=3)\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 유서치.index 임포트 인덱스", kopy)
        self.assertIn("인덱스 = 인덱스(ndim=3)", kopy)
        self.assertEqual(translate(kopy).python, source)

        source = "from langchain_core.documents import Document\ndocuments = []\n"
        kopy = to_kopy(source).kopy
        self.assertIn("프롬 랭체인코어.documents 임포트 도큐먼트", kopy)
        self.assertIn("다큐먼츠 = []", kopy)
        self.assertEqual(translate(kopy).python, source)

    def test_strings_comments_and_numeric_literals_are_untouched(self):
        source = (
            "쿼리 = 'query BM25 F1 L2 top_k=2'  # query BM25 F1 L2\n"
            "리절츠 = search(쿼리, top_k=2)\n"
        )
        python_source = translate(source).python
        self.assertIn("'query BM25 F1 L2 top_k=2'", python_source)
        self.assertIn("# query BM25 F1 L2", python_source)
        self.assertIn("top_k=2", python_source)

    def test_top_k_is_intentionally_not_a_common_transliteration(self):
        self.assertNotIn("top_k", COMMON_IDENTIFIERS.values())
        self.assertIn("top_k=2", to_kopy("result = fn(top_k=2)\n").kopy)

    def test_common_identifiers_are_exposed_to_editor_metadata(self):
        info = info_for("엑스_트레인")
        self.assertIsNotNone(info)
        self.assertEqual(info.python, "X_train")
        self.assertEqual(info.category, "identifier")

        info = info_for("쿼리_임베딩즈")
        self.assertIsNotNone(info)
        self.assertEqual(info.python, "query_embeddings")
        self.assertEqual(info.category, "identifier")


if __name__ == "__main__":
    unittest.main()
