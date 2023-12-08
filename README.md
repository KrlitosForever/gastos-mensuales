# Aplicación de control de Gastos

# Índice
- [Introducción](#introducción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)


# Introducción

A continuación se detalla el desarrollo de una aplicación simple para el registro de gastos del hogar utilizando Streamlit y SQLite. La aplicación permite a los usuarios agregar, visualizar y analizar sus gastos mensuales de manera eficiente.

# Requisitos

Para ejecutar la aplicación, se requieren los siguientes elementos:

- **Python:** La aplicación está escrita en Python, por lo que necesitarás tener Python instalado en tu sistema. Puedes descargar la última versión de Python desde [python.org](https://www.python.org/downloads/).


# Instalación

1. **Clonar el Repositorio:**
   Descarga o clona el repositorio desde GitHub:

   ```bash
   git clone https://github.com/KrlitosForever/gastos-mensuales.git
   ```

2. **Crear un Entorno Virtual (Opcional pero Recomendado):**
   Se recomienda crear un entorno virtual para evitar conflictos con las dependencias de otros proyectos. Utiliza el siguiente comando:

   ```bash
   python -m venv venv
   ```

3. **Activar el Entorno Virtual (Windows):**
   ```bash
   .\venv\Scripts\activate
   ```

   **Activar el Entorno Virtual (Linux/Mac):**
   ```bash
   source venv/bin/activate
   ```

4. **Instalar Dependencias:**
   Navega al directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

# Uso

1. **Ejecutar la Aplicación:**
   Desde el directorio del proyecto, ejecuta el siguiente comando para iniciar la aplicación:

   ```bash
   streamlit run streamlit_app.py
   ```

   Esto abrirá la aplicación en tu navegador predeterminado.

2. **Agregar Gastos:**
   Utiliza la barra lateral para agregar nuevos gastos proporcionando la fecha, categoría, monto y comentario.

3. **Visualizar Gastos:**
   Observa la tabla de registros y los gráficos de distribución de gastos por categoría.

## Donaciones
Si quieres que el canal siga creciendo puedes ayudar comprandome un cafe🥤

<a href="https://www.buymeacoffee.com/KrlitosForever" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>