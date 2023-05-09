# Crear una referencia a los objetos GeoJson de las capas
poligonos_layer = folium.GeoJson(gdf,
                                 name='Polígonos',
                                 tooltip=folium.GeoJsonTooltip(fields=['NOM_SSUBC', 'COD_SSUBC'], aliases=['Nombre subsub cuenca','Código subsub cuenca']),
                                 overlay=True)
capa_2_layer = folium.GeoJson(gdf2,
                              name='Capa_2',
                              tooltip=folium.GeoJsonTooltip(fields=['COMUNA','USO_ACTUAL'], aliases=['Comuna', 'Uso de suelo al 2006']),
                              overlay=True)

# Agregar los objetos GeoJson al mapa
poligonos_layer.add_to(m)
capa_2_layer.add_to(m)

# Crear el objeto GroupedLayerControl con las referencias a las capas
layer_control = GroupedLayerControl(
    base_overlays={
        "Polígonos": poligonos_layer, # Referencia al objeto GeoJson de la capa "Polígonos"
    },
    grouped_overlays={
        "Capa_2": capa_2_layer # Referencia al objeto GeoJson de la capa "Capa_2"
    },
)


# Agregar el controlador de capas al mapa
layer_control.add_to(m)
