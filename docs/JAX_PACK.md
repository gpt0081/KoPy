# JAX Library Pack

KoPy 0.5.19의 JAX 팩은 `jax / 잭스`와 `jax.numpy` 흐름을 namespace-scoped 방식으로 지원합니다. 실제 배열 계산, 자동미분, JIT 컴파일과 벡터화는 upstream JAX/jaxlib가 수행합니다.

## 설치

KoPy의 개발 기준은 Python 3.12.10입니다. JAX 0.11.1은 Python 3.12 이상을 요구하므로 현재 기준과 호환됩니다.

```powershell
python -m pip install "jax>=0.11.1,<0.12"
```

CPU CI에서는 위 패키지를 그대로 사용합니다. GPU/TPU 설치는 JAX 공식 설치 지침에 따라 별도로 구성하세요.

## 기본 예제

```kopy
임포트 잭스
임포트 잭스.numpy 애즈 jnp

X = jnp.어레이([1.0, 2.0, 3.0])
loss_fn = lambda x: jnp.썸(jnp.스퀘어(x))
grad_fn = 잭스.잇(잭스.그라드(loss_fn))
grads = grad_fn(X)

프린트(grads)
```

대응 Python은 다음과 같습니다.

```python
import jax
import jax.numpy as jnp

X = jnp.array([1.0, 2.0, 3.0])
loss_fn = lambda x: jnp.sum(jnp.square(x))
grad_fn = jax.jit(jax.grad(loss_fn))
grads = grad_fn(X)

print(grads)
```

`X`, `loss_fn`, `grad_fn`, `grads`, `jnp` 같은 실제 JAX/Python 관례는 학습을 위해 의도적으로 남길 수 있습니다.

## 지원 범위

대표 지원 API:

- 변환: `grad`, `value_and_grad`, `jit`, `vmap`, `pmap`, `jacfwd`, `jacrev`, `hessian`
- 런타임: `device_put`, `device_get`, `devices`, `default_backend`, `block_until_ready`
- `jax.numpy`: `array`, `asarray`, `zeros`, `ones`, `arange`, `reshape`, `stack`, `concatenate`, `matmul`, `sum`, `mean`, `where`, `exp`, `log`, `sqrt` 등
- `jax.random`: `key`, `PRNGKey`, `split`, `fold_in`, `normal`, `uniform`, `randint`, `bernoulli`, `categorical`, `permutation`
- `jax.nn`: `relu`, `gelu`, `sigmoid`, `softmax`, `log_softmax`, `one_hot`
- `jax.lax`: `scan`, `fori_loop`, `cond`, `while_loop`, `stop_gradient`

CLI에서 전체 멤버를 확인할 수 있습니다.

```powershell
kopy packs jax
```

## 충돌 방지

JAX API 이름은 Core 전역 단어표에 추가하지 않습니다. `잭스`, `jax`, `jax.numpy`가 import된 파일에서만 팩이 활성화됩니다.

다음과 같은 키워드 인자는 여러 라이브러리에서 공통으로 쓰이므로 Python 원형을 유지합니다.

```text
dtype= shape= axis= device= static_argnums= static_argnames=
in_axes= out_axes= donate_argnums= has_aux=
```

이 원칙은 KoPy 코드가 원문 Python/JAX 코드로 자연스럽게 이어지도록 하는 교육 목적과도 맞습니다.
