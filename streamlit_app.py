import streamlit as st
import pandas as pd
import sqlite3
import calendar
import matplotlib.pyplot as plt
import locale

# Establecer el idioma a español
#locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Crear una conexión a la base de datos SQLite (o crear la base de datos si no existe)
conn = sqlite3.connect('gastos.db')

# Crear una tabla de gastos si no existe
conn.execute('''
    CREATE TABLE IF NOT EXISTS gastos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha DATE NOT NULL,
        categoria TEXT NOT NULL,
        monto INTEGER NOT NULL,
        comentario TEXT  -- Agregamos una columna para comentarios
    )
''')

# Título de la aplicación
st.title("Registro de Gastos Mensuales")

# Sidebar para la entrada de datos
st.sidebar.header("Ingrese sus Gastos")

# Obtener la fecha
fecha = st.sidebar.date_input("Fecha", pd.to_datetime("today"))

# Obtener la categoría del gasto
categorias = ["Comida", "Transporte","Peaje","Entretenimiento","Domestico","Arriendo", "Otros"]
categoria = st.sidebar.selectbox("Categoría", categorias)

# Obtener el monto del gasto
monto = st.sidebar.number_input("Monto", value=0, step=1)  # Cambiar el step a 1 para aceptar solo valores enteros

# Obtener el comentario del gasto
comentario = st.sidebar.text_input("Comentario", "")

# Botón para agregar el gasto
if st.sidebar.button("Agregar Gasto"):
    # Insertar el gasto en la base de datos
    conn.execute('INSERT INTO gastos (fecha, categoria, monto, comentario) VALUES (?, ?, ?, ?)', (fecha, categoria, monto, comentario))
    conn.commit()

# Leer los gastos desde la base de datos
gastos = pd.read_sql_query('SELECT * FROM gastos', conn)

# Convertir la columna 'fecha' a tipo datetime
gastos['fecha'] = pd.to_datetime(gastos['fecha'])

# Agregar columna de mes con el nombre del mes
gastos['mes'] = gastos['fecha'].dt.strftime('%B')

# Capitalizar la primera letra de cada palabra en las columnas 'categoria' y 'mes'
gastos['categoria'] = gastos['categoria'].str.title()
gastos['mes'] = gastos['mes'].str.title()

# Redondear y formatear la columna 'monto' como números enteros
gastos['monto'] = gastos['monto'].map('${:,.0f}'.format)

# Mostrar los gastos en la aplicación
st.subheader("Gastos Registrados")
st.dataframe(gastos)

# Gráfico de torta para visualizar la distribución de gastos por categoría
fig, ax = plt.subplots()
gastos_por_categoria = gastos.groupby('categoria')['monto'].count()
ax.pie(gastos_por_categoria, labels=gastos_por_categoria.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.subheader("Distribución de Gastos por Categoría")
st.pyplot(fig)

# Mostrar la suma de gastos por mes con nombre del mes
st.subheader("Suma de Gastos por Mes")
gastos_por_mes = gastos.groupby('mes')['monto'].count()
st.bar_chart(gastos_por_mes)

# Cerrar la conexión a la base de datos al finalizar
conn.close()

