import unittest

from kopy.packs.registry import pack_by_name, resolve_pack_member
from kopy.translator import to_kopy, translate


class JaxPackTests(unittest.TestCase):
    def test_pack_is_registered(self):
        pack = pack_by_name("jax")
        self.assertIsNotNone(pack)
        self.assertEqual(pack.kopy_module, "잭스")

    def test_jax_numpy_alias_translation_is_namespace_scoped(self):
        source = (
            "임포트 잭스.numpy 애즈 jnp\n"
            "X = jnp.어레이([[1.0, 2.0], [3.0, 4.0]])\n"
            "loss = jnp.미인(jnp.스퀘어(X))\n"
        )
        python_source = translate(source).python
        self.assertIn("import jax.numpy as jnp", python_source)
        self.assertIn("jnp.array", python_source)
        self.assertIn("jnp.mean(jnp.square(X))", python_source)

    def test_top_level_transform_and_random_translation(self):
        source = (
            "임포트 잭스\n"
            "f = 잭스.잇(lambda x: x ** 2)\n"
            "df = 잭스.그라드(f)\n"
            "key = 잭스.랜덤.키(42)\n"
            "a, b = 잭스.랜덤.스플릿(key)\n"
        )
        python_source = translate(source).python
        self.assertIn("jax.jit", python_source)
        self.assertIn("jax.grad", python_source)
        self.assertIn("jax.random.key(42)", python_source)
        self.assertIn("jax.random.split(key)", python_source)

    def test_from_import_translation(self):
        source = "프롬 잭스 임포트 그라드, 밸류앤드그라드\n"
        python_source = translate(source).python
        self.assertIn("from jax import grad, value_and_grad", python_source)

    def test_unimported_jax_word_is_not_global(self):
        source = "result = 그라드(f)\n"
        self.assertEqual(translate(source).python, source)

    def test_python_to_kopy(self):
        source = (
            "import jax\n"
            "import jax.numpy as jnp\n"
            "X = jnp.array([1.0, 2.0])\n"
            "df = jax.grad(lambda x: jnp.sum(jnp.square(x)))\n"
        )
        kopy = to_kopy(source).kopy
        self.assertIn("임포트 잭스", kopy)
        self.assertIn("임포트 잭스.numpy 애즈 jnp", kopy)
        self.assertIn("jnp.어레이", kopy)
        self.assertIn("잭스.그라드", kopy)
        self.assertIn("jnp.썸(jnp.스퀘어(x))", kopy)

    def test_help_resolution(self):
        resolved = resolve_pack_member("잭스.그라드")
        self.assertIsNotNone(resolved)
        _, info = resolved
        self.assertEqual(info.python, "grad")

    def test_keywords_remain_python_spelling(self):
        source = (
            "임포트 잭스.numpy 애즈 jnp\n"
            "X = jnp.어레이([1, 2, 3], dtype=jnp.float32)\n"
        )
        python_source = translate(source).python
        self.assertIn("dtype=jnp.float32", python_source)


if __name__ == "__main__":
    unittest.main()
