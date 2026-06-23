# `Dashboard de Vendas`

> Análise de vendas em tempo real com SQL, DuckDB e Streamlit.

---

![Python](https://img.shields.io/badge/Python-3.13-blue)
![DuckDB](https://img.shields.io/badge/DuckDB-1.5-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![SQL](https://img.shields.io/badge/SQL-DuckDB-orange)

---

## `Objetivo`

Transformar dados brutos de vendas em insights de negócio acionáveis — margem por vendedor, receita por região e lucro por produto numa aplicação web interativa.

---

## `Pipeline`

```
CSV → DuckDB (SQL) → pandas → Streamlit (web)
```

---

## `Análises implementadas`

| `Query` | `Arquivo` | `Insight gerado` |
|---|---|---|
| Receita por região | `sql/01_receita_por_regiao.sql` | Sudeste lidera em volume, Norte e Nordeste lideram em margem % |
| Ranking de vendedores | `sql/02_ranking_vendedores.sql` | João tem maior margem (44.75%) — melhor produto mix |
| Lucro por produto | `sql/03_lucro_por_categoria.sql` | SSD 1TB: maior giro + margem consistente |

---

## `Como rodar`

```bash

# Clonar o repositório
git clone https://github.com/seu-usuario/dashboard_vendas.git
cd dashboard_vendas

# Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# Instalar dependências
pip install pandas duckdb sqlalchemy matplotlib streamlit

# Executar dashboards
python src/banco.py
streamlit run src/app.py
```
