import geopandas as gpd
import folium
from streamlit_folium import folium_static
import streamlit as st



@st.cache_data() 
def get_data():
# Cargar el archivo SHP en un objeto GeoDataFrame
    shp_path = "USO_suelo_Valdivia2006.shp"
    gdf = gpd.read_file(shp_path)
    # Cargar el segundo archivo SHP en otro objeto GeoDataFrame
    shp2_path = "USO_suelo_LosLagos2006.shp"
    gdf2 = gpd.read_file(shp2_path)
    # Cargar el tercer archivo SHP en otro objeto GeoDataFrame
    shp3_path = "USO_suelo_Mafil_2006.shp"
    gdf3 = gpd.read_file(shp3_path)
    # Cargar el cuarto archivo SHP en otro objeto GeoDataFrame
    shp4_path = "USO_suelo_Panguipulli2006.shp"
    gdf4 = gpd.read_file(shp4_path)
    return gdf, gdf2, gdf3, gdf4



# Crear un objeto Folium Map centrado en los datos de los polígonos
m = folium.Map(location=[-39.8, -72.8], zoom_start=9)


# Agregar los datos de los polígonos al mapa
# Obtener los datos de los polígonos y agregarlos al mapa
gdf, gdf2, gdf3, gdf4 = get_data()

folium.GeoJson(gdf,
               name='Uso de suelo en Valdivia al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

# Agregar los datos de los polígonos del segundo archivo SHP al mapa
folium.GeoJson(gdf2,
               name='Uso de suelo en Los Lagos al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

#Agrega los datos de la tercera capa SHP al mapa
folium.GeoJson(gdf3,
               name='Uso de suelo en Máfil al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna','Uso de suelo al 2006']),
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)

#Agrega los datos de la cuarta capa SHP al mapa
folium.GeoJson(gdf4,
               name='Uso de suelo en Panguipulli al año 2006',
               tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna','Uso de suelo al 2006']),
               show=False# no se moestrara la capa al cargar la página, de lo contrario si es que se desea que se pueda visualizar desde un inicio debe ser con el comando "overlay=True"
               ).add_to(m)
#HASTA ESTE PUNTO SE PUEDEN VISUALIZAR BIEN LAS CAPAS, PERO HACE FALTA AGREGAR EL SELECCTOR DE CAPAS A LA VISUALIZACIÓN EN MAPA.



# Crear el control de capas agrupadas

control = folium.LayerControl()

control.add_to(m)


# Mostrar el mapa en Streamlit
folium_static(m)



