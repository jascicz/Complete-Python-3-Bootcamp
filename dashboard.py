import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Mi Primera Aplicación en Streamlit")

# Cargar un DataFrame
df = pd.DataFrame({
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
    'Edad': [24, 27, 22, 32],
    'Ciudad': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
})

# Mostrar la tabla de datos
st.write("Aquí están los datos:")
st.write(df)

# Gráfico simple
st.write("Gráfico de Edad:")
fig, ax = plt.subplots()
ax.bar(df['Nombre'], df['Edad'])
st.pyplot(fig)

# Interactividad con un widget
edad_minima = st.slider('Selecciona la edad mínima', min_value=20, max_value=40, value=25)
st.write(f"Usuarios con edad mayor o igual a {edad_minima}:")
st.write(df[df['Edad'] >= edad_minima])
