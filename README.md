
# `playmath`: um playground para exercício

Repositório simples para exercitar fluxo de trabalho com **Git/GitHub** (branch, commit, PR, code review e CI) usando Python, `pytest`, `ruff` e `mypy`.

## Objetivo

- Exemplo completo pronto: `add(a, b)` já implementada, tipada, documentada e com teste.
- **12 tarefas** (funções) para os alunos implementarem em **PRs** pequenos (1–2 funções + testes por PR).

## Como usar

1. **Crie um ambiente** (recomendado Python >= 3.10):
   ```bash
   # Esse comando cria um ambiente virtual chamado .venv
   # O ambiente será um diretório de mesmo nome
   python -m venv .venv
   # O comando abaixo ativa o ambiente virtual no seu terminal
   source .venv/bin/activate  # no Windows: .venv\Scripts\activate
   ```
2. **Instale as dependências do projeto dentro do ambiente virtual**:
   ```bash
   pip install -e .
   ```
3. **Instale os checker e formatadores automáticos via pre-commit**:
   ```bash
   pre-commit install
   ```
4. **Rode os testes e linters** localmente:
   ```bash
   pytest -q
   ruff check .
   mypy src
   ```
5. **Implemente uma função** em `src/playmath/basic.py` (edite a docstring se necessário) e
   **crie seus testes** em `tests/test_basic_extra.py` (você pode copiar o estilo de `tests/test_add.py`).
   Abra um **PR** com o título título informativo. Exemplo: `Implement functions X, Y, Z, etc` e marque a checklist.

**Note:** toda vez que for trabalhar no `playmath`, você deve ativar o ambiente virtual de trabalho, que no caso é o `.venv`. Se for utilizar o VS Code, você também deve selecionar o interpretador Python contido nesse ambiente virtual.

## Fluxo sugerido de PR

- 1 PR por função (ou no máximo 2) com testes e docstrings atualizadas.
- CI precisa passar (ruff, mypy, pytest).

## Funções a implementar (8 TODOs)

No arquivo `src/mathlib/basic.py`:
1. `subtract(a, b) -> float`
2. `multiply(a, b) -> float`
3. `divide(a, b) -> float` (ZeroDivisionError para b = 0)
4. `power(base, exp) -> float`
5. `sqrt(x) -> float` (ValueError se x < 0)
6. `factorial(n) -> int` (ValueError se n < 0 ou não inteiro)
7. `is_prime(n) -> bool`
8.  `mean(data) -> float` (ValueError se vazio)

A pontuação do Assignment é baseada nos testes unitários de cada função. Se todos os 8 testes passarem, a solução do Assignment recebe nota máxima.

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
