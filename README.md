# `Dashboard de Vendas`

> Análise de vendas em tempo real com SQL, DuckDB e Streamlit.

---

![Python](https://img.shields.io/badge/Python-3.13-blue)
![DuckDB](https://img.shields.io/badge/DuckDB-1.5-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![SQL](https://img.shields.io/badge/SQL-DuckDB-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## `Objetivo`

Transformar dados brutos de vendas em insights de negócio acionáveis margem por vendedor, receita por região e lucro por produto numa aplicação web interativa.

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
| Ranking de vendedores | `sql/02_ranking_vendedores.sql` | João tem maior margem (44.75%) melhor produto mix |
| Lucro por produto | `sql/03_lucro_por_categoria.sql` | SSD 1TB: maior giro + margem consistente |

---

## `Como rodar`

```bash
# Clonar o repositório
git clone https://github.com/Arthur-Baptista-dos-Santos/dashboard-vendas.git
cd dashboard-vendas

# Criar ambiente virtual
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Executar o pipeline SQL e subir o dashboard
python src/banco.py
streamlit run src/app.py
```

---

## `Estrutura`

```
dashboard-vendas/
├── dados/
│   └── vendas.csv                    # dataset de vendas
├── sql/
│   ├── 01_receita_por_regiao.sql     # receita e margem por região
│   ├── 02_ranking_vendedores.sql     # ranking por margem
│   └── 03_lucro_por_categoria.sql    # lucro por produto
├── src/
│   ├── banco.py                      # carrega CSV e persiste no DuckDB
│   ├── graficos.py                   # gráficos com matplotlib
│   └── app.py                        # dashboard Streamlit
├── .gitignore
├── requirements.txt
└── readme.md
```

---

## `Conceitos aplicados`

- **`DuckDB`**: banco analítico embutido, sem servidor, executa SQL direto sobre DataFrames
- **`SQL analítico`**: queries com GROUP BY, ORDER BY e cálculo de margem para insights de negócio
- **`Streamlit`**: transforma scripts Python em dashboards web interativos
- **`Pipeline CSV→SQL→Web`**: fluxo completo de dados brutos a visualização de negócio

---

## `Demonstração`

**Painel de Vendas**: KPIs consolidados (R$ 196.520 em receita, 40.9% de margem média) com gráficos de receita por região, margem por vendedor e lucro por produto.

![Dashboard de Vendas](docs/screenshots/dashboard.png)

---

## `Licença`

Distribuído sob a licença MIT. Veja [LICENSE](LICENSE) para mais informações.

---

## `Autor`

**Arthur Baptista dos Santos**
RM 565346 · Inteligência Artificial · FIAP 2025-2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Arthur%20Baptista-0077B5?logo=linkedin)](https://linkedin.com/in/arthur-baptista-dos-santos)
[![GitHub](https://img.shields.io/badge/GitHub-Arthur--Baptista--dos--Santos-181717?logo=github)](https://github.com/Arthur-Baptista-dos-Santos)
