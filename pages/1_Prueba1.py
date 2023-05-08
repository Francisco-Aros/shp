import geopandas as gpd
import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

# Lee el archivo shapefile
gdf1 = gpd.read_file("Cuenca_Valdivia.shp")
gdf2 = gpd.read_file("USO_suelo_LosLagos2006.shp")

# Crea el mapa utilizando la librería matplotlib
fig, ax = plt.subplots()
gdf1.plot(ax=ax, color ='blue')
gdf2.plot(ax=ax, color='red')

ax.set_title('Uso de suelo Los Lagos al 2006.')
ax.legend(['Cuencas del Río Valdivia', 'Uso de suelo en Los Lagos al 2006.'])


# Visualiza el mapa en Streamlit
st.pyplot(fig)


##VISUALIZAR CAPAS EN UN MAPA ESTILO GMAPS U OPENSTREETMAPS.

# Lee los archivos shapefile
gdf1 = gpd.read_file("Cuenca_Valdivia.shp")
gdf2 = gpd.read_file("USO_suelo_LosLagos2006.shp")

# Crea un mapa de folium centrado en una ubicación específica
m = folium.Map(location=[-39.81, -73.2467], zoom_start=10)

# Agrega las capas al mapa de folium
folium.GeoJson(gdf1).add_to(m)
folium.GeoJson(gdf2).add_to(m)

# Muestra el mapa en Streamlit
folium_static(m)
