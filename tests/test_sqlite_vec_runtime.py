import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("sqlite_vec"), "sqlite-vec is not installed")
class SQLiteVecRuntimeTests(unittest.TestCase):
    def test_real_sqlite_vector_search(self):
        source = (
            "임포트 sqlite3\n"
            "임포트 에스큐엘라이트벡 애즈 sqlite_vec\n"
            "connection = sqlite3.connect(':memory:')\n"
            "connection.enable_load_extension(True)\n"
            "sqlite_vec.로드(connection)\n"
            "connection.enable_load_extension(False)\n"
            "connection.execute('CREATE VIRTUAL TABLE vec_items USING vec0(embedding float[3])')\n"
            "items = [(1, [1.0, 0.0, 0.0]), (2, [0.0, 1.0, 0.0]), (3, [0.0, 0.0, 1.0])]\n"
            "포 item_id, embedding 인 items:\n"
            "    connection.execute('INSERT INTO vec_items(rowid, embedding) VALUES (?, ?)', [item_id, sqlite_vec.시리얼라이즈플로트32(embedding)])\n"
            "query = [0.95, 0.05, 0.0]\n"
            "rows = connection.execute('SELECT rowid, distance FROM vec_items WHERE embedding MATCH ? ORDER BY distance LIMIT 2', [sqlite_vec.시리얼라이즈플로트32(query)]).fetchall()\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)
        rows = namespace["rows"]
        connection = namespace["connection"]

        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0][0], 1)
        self.assertLess(float(rows[0][1]), float(rows[1][1]))
        self.assertLess(float(rows[0][1]), 0.01)
        vec_version = connection.execute("select vec_version()").fetchone()[0]
        self.assertTrue(str(vec_version))


if __name__ == "__main__":
    unittest.main()
