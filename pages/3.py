gdf, gdf2, gdf3, gdf4 = get_data()
capa_1_layer = folium.GeoJson(gdf,
                              name='Polígonos',
                              tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
                              overlay=True
                             ).add_to(m)

# Agregar los datos de los polígonos del segundo archivo SHP al mapa
capa_2_layer = folium.GeoJson(gdf2,
                              name='Capa_2',
                              tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
                              overlay=True
                              ).add_to(m)

#Agrega los datos de la tercera capa SHP al mapa
capa_3_layer = folium.GeoJson(gdf3,
                              name='Capa_3',
                              tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna','Uso de suelo al 2006']),
                              overlay=True
                              ).add_to(m)

#Agrega los datos de la cuarta capa SHP al mapa
capa_4_layer = folium.GeoJson(gdf4,
                              name='Capa_4',
                              tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna','Uso de suelo al 2006']),
                              overlay=True
                              ).add_to(m)
#HASTA ESTE PUNTO SE PUEDEN VISUALIZAR BIEN LAS CAPAS, PERO HACE FALTA AGREGAR EL SELECCTOR DE CAPAS A LA VISUALIZACIÓN EN MAPA.

# Crear el objeto GroupedLayerControl con las referencias a las capas
layer_control = GroupedLayerControl(
    base_overlays={
        "Polígonos": capa_1_layer, # Referencia al objeto GeoJson de la capa "Polígonos"
    },
    grouped_overlays={
        "Capa_2": capa_2_layer, # Referencia al objeto GeoJson de la capa "Capa_2"
        "Capa_3": capa_3_layer, # Referencia al objeto GeoJson de la capa "Capa_3"
        "Capa_4": capa_4_layer, # Referencia al objeto GeoJson de la capa "Capa_4" 
    },
    groups={
        "Capas": {
            "Capa_2": capa_2_layer,
            "Capa_3": capa_3_layer,
            "Capa_4": capa_4_layer,
        }
    }
)


# Agregar el controlador de capas al mapa
layer_control.add_to(m)

# Mostrar el mapa en Streamlit
folium_static(m)
