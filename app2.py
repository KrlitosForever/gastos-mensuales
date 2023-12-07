import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import matplotlib.pyplot as plt

# Crear o conectar a la base de datos SQLite
conn = sqlite3.connect('gastos.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE,
        categoria TEXT,
        monto REAL,
        comentario TEXT
    )
''')
conn.commit()

# Sidebar
st.sidebar.header('Agregar Gasto')
fecha = st.sidebar.date_input('Fecha', pd.Timestamp.now())
categoria = st.sidebar.selectbox('Categoría', ['Comida', 'Bencina', 'Peaje', 'Arriendo', 'Transporte', 'Entretenimiento'])
monto = st.sidebar.number_input('Monto', value=0.0, min_value=0.0)
comentario = st.sidebar.text_input('Comentario')

if st.sidebar.button('Agregar Gasto'):
    nuevo_gasto = (fecha, categoria, monto, comentario)
    cursor.execute('''
        INSERT INTO gastos (fecha, categoria, monto, comentario)
        VALUES (?, ?, ?, ?)
    ''', nuevo_gasto)
    conn.commit()

# Página principal
st.title('Registro de Gastos del Hogar')

# Leer datos desde la base de datos
df = pd.read_sql_query('SELECT * FROM gastos', conn)

# Mostrar tabla de gastos
st.subheader('Registros de Gastos')
st.dataframe(df)

# Mostrar gráfico de distribución de montos por categoría
st.subheader('Distribución de Gastos por Categoría')
fig = px.pie(df, names='categoria', values='monto', title='Distribución de Gastos por Categoría')
st.plotly_chart(fig)

# Cerrar la conexión a la base de datos al finalizar
conn.close()
