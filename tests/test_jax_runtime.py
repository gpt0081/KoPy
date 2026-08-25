import importlib.util
import unittest

from kopy.translator import translate


@unittest.skipUnless(importlib.util.find_spec("jax"), "JAX is not installed")
class JaxRuntimeTests(unittest.TestCase):
    def test_real_jax_grad_jit_vmap_and_random(self):
        source = (
            "임포트 잭스\n"
            "임포트 잭스.numpy 애즈 jnp\n"
            "X = jnp.어레이([1.0, 2.0, 3.0])\n"
            "loss_fn = lambda x: jnp.썸(jnp.스퀘어(x))\n"
            "grad_fn = 잭스.짓(잭스.그라드(loss_fn))\n"
            "grads = grad_fn(X)\n"
            "batched = 잭스.브이맵(lambda x: x * 2)(X)\n"
            "key = 잭스.random.키(7)\n"
            "sample = 잭스.random.노멀(key, shape=(3,))\n"
        )
        namespace = {}
        exec(translate(source).python, namespace)

        jnp = namespace["jnp"]
        grads = namespace["grads"]
        batched = namespace["batched"]
        sample = namespace["sample"]

        self.assertTrue(bool(jnp.allclose(grads, jnp.array([2.0, 4.0, 6.0]))))
        self.assertTrue(bool(jnp.allclose(batched, jnp.array([2.0, 4.0, 6.0]))))
        self.assertEqual(sample.shape, (3,))
        self.assertTrue(bool(jnp.all(jnp.isfinite(sample))))


if __name__ == "__main__":
    unittest.main()
