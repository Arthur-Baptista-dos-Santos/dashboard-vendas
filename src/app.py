import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("Dashboard de Vendas")

con = duckdb.connect("dados/vendas.db")

regiao = con.execute(open("sql/01_receita_por_regiao.sql").read()).fetchdf()
vendedores = con.execute(open("sql/02_ranking_vendedores.sql").read()).fetchdf()
categorias = con.execute(open("sql/03_lucro_por_categoria.sql").read()).fetchdf()

con.close()

col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {regiao['receita_total'].sum():,.0f}")
col2.metric("Lucro Total", f"R$ {regiao['lucro_total'].sum():,.0f}")
col3.metric("Margem Média", f"{(regiao['lucro_total'].sum() / regiao['receita_total'].sum() * 100):.1f}%")

st.divider()

col4, col5 = st.columns(2)

with col4:
    st.subheader("Receita por Região")
    st.bar_chart(regiao.set_index("regiao")["receita_total"])

with col5:
    st.subheader("Margem % por Vendedor")
    st.bar_chart(vendedores.set_index("vendedor")["margem_pct"])

st.subheader("Lucro por Produto")
st.bar_chart(categorias.set_index("produto")["lucro_total"])
