import geopandas as gpd
import folium
from streamlit_folium import folium_static
from folium.plugins import GroupedLayerControl
from folium.plugins import MarkerCluster
import streamlit as st


@st.cache_data() 
def get_data():
# Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "Cuenca_Valdivia.shp"
    gdf = gpd.read_file(shp_path)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
    shp2_path = "USO_suelo_LosLagos2006.shp"
    gdf2 = gpd.read_file(shp2_path)
    return gdf, gdf2

# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.81, -73.2467], zoom_start=10)

# Agregar los datos de los polígonos al mapa
# Obtener los datos de los polígonos y agregarlos al mapa
gdf, gdf2 = get_data()
folium.GeoJson(gdf,
               name='Polígonos',
               tooltip=folium.GeoJsonTooltip(fields=['NOM_SSUBC', 'COD_SSUBC'], aliases=['Nombre subsub cuenca','Código subsub cuenca']),
               overlay=True
              ).add_to(m)

# Agregar los datos de los polígonos del segundo archivo SHP al mapa
folium.GeoJson(gdf2,
               name='Capa_2',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
               overlay=True
              ).add_to(m)
#HASTA ESTE PUNTO SE PUEDEN VISUALIZAR BIEN LAS CAPAS, PERO HACE FALTA AGREGAR EL SELECCTOR DE CAPAS A LA VISUALIZACIÓN EN MAPA.



# Mostrar el mapa en Streamlit
folium_static(m)



