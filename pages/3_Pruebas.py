import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static
import numpy as np

st.title("Ejemplo de trabajo con Python")
st.write("Durante el año 2022, se me encargó realizar el trabajo cartográfico asociado al territorio de acción de la Asociación de Municipalidades Paisajes de Conservación por la Biodiversidad de la Región de Los Ríos, asociación compuesta por las comunas de Panguipulli, Los Lagos, Máfil y Valdivia. Dentro del trabajo realizado y de mi labor como geógrafo, debí desarrolla diversas cartografías del territorio de acción de la asociación.")
st.write("A continuación, podrán observar el Uso del Suelo al año 2006 en lo que actualmente sería el territorio de acción de esta asociación de municipios, este mapa fue desarrollado con la base de datos que posee CONAF para la Región de Los Ríos y para el caso de esta página web, se desarrolló con Python para su visualización.")

# Lee el archivo shapefile
gdf1 = gpd.read_file("Suelo_territorio_accion2006_R14.shp")

# Crea el mapa utilizando la librería matplotlib
fig, ax = plt.subplots(figsize=(10, 10))

# Obtén los atributos únicos de la columna que deseas asignar colores diferentes
unique_attributes_1 = gdf1['USO_ACTUAL'].unique()

# Define una paleta de colores con la misma longitud que los atributos únicos
colors_1 = plt.cm.Set1(np.linspace(0, 1, len(unique_attributes_1)))

# Asigna colores a los atributos correspondientes en cada capa
for i, attribute in enumerate(unique_attributes_1):
    gdf1[gdf1['USO_ACTUAL'] == attribute].plot(ax=ax, color=colors_1[i])

ax.set_title('Uso de suelo en territorio de acción 2006.')

# Crea la leyenda utilizando los atributos y los colores correspondientes
handles = [plt.Rectangle((0, 0), 1, 1, color=colors_1[i]) for i, _ in enumerate(unique_attributes_1)]
labels = unique_attributes_1

# Ajusta la leyenda en varias columnas y la posiciona debajo del mapa
legend = ax.legend(handles, labels, loc='upper center', ncol=3, bbox_to_anchor=(0.5, -0.2), fontsize='small', title='Leyenda')

# Ajusta los márgenes del gráfico para separar la leyenda del mapa
plt.subplots_adjust(bottom=0)

# Visualiza el mapa en Streamlit
st.pyplot(fig)
