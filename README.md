
# `playmath`: um playground para exercício

Repositório simples para exercitar fluxo de trabalho com **Git/GitHub** (branch, commit, PR, code review e CI) usando Python, `pytest`, `ruff` e `mypy`.

## Objetivo

- Exemplo completo pronto: `add(a, b)` já implementada, tipada, documentada e com teste.
- **12 tarefas** (funções) para os alunos implementarem em **PRs** pequenos (1–2 funções + testes por PR).

## Como usar (alunos)

1. **Crie um ambiente** (recomendado Python ≥ 3.10):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # no Windows: .venv\Scripts\activate
   pip install -r requirements-dev.txt
   ```
2. **Rode os testes e linters** localmente:
   ```bash
   pytest -q
   ruff check .
   mypy src
   ```
3. **Implemente uma função** em `src/playmath/basic.py` (edite a docstring se necessário) e
   **crie seus testes** em `tests/test_basic_extra.py` (você pode copiar o estilo de `tests/test_add.py`).  
   Abra um **PR** com o título `feat: implement <nome-da-funcao>` e marque a checklist.

4. (Opcional) **pre-commit**:
   ```bash
   pre-commit install
   ```

## Fluxo sugerido de PR

- 1 PR por função (ou no máximo 2) com testes e docstrings atualizadas.
- CI precisa passar (ruff, mypy, pytest).

## Funções a implementar (12 TODOs)

No arquivo `src/mathlib/basic.py`:
1. `subtract(a, b) -> float`
2. `multiply(a, b) -> float`
3. `divide(a, b) -> float` (ZeroDivisionError para b = 0)
4. `power(base, exp) -> float`
5. `sqrt(x) -> float` (ValueError se x < 0)
6. `factorial(n) -> int` (ValueError se n < 0 ou não inteiro)
7. `is_prime(n) -> bool`
8. `gcd(a, b) -> int`  (resultado não negativo)
9. `lcm(a, b) -> int`  (resultado não negativo)
10. `mean(data) -> float` (ValueError se vazio)
11. `median(data) -> float` (ValueError se vazio)
12. `variance(data, sample=False) -> float` (ValueError se len < 1 para população; < 2 para amostra)

A função `add(a, b)` já está implementada como **exemplo completo** e cobre o fluxo inteiro (docstring, type hints, teste).

## Executando cobertura (opcional)
```bash
pytest --cov=src --cov-report=term-missing
```

## Estrutura
```
.
├── LICENSE
├── README.md
├── requirements-dev.txt
├── pyproject.toml
├── .ruff.toml
├── .gitignore
├── .pre-commit-config.yaml       # opcional
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── playmath/
│       ├── __init__.py
│       └── basic.py
└── tests/
    ├── test_add.py               # exemplo completo
    └── test_basic_extra.py       # você cria/expande
```

Boa prática: manter PRs pequenos e com mensagens de commit claras.
