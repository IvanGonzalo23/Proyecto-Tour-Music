def ubicacion_central(latitudes, longitudes):
    n = len(latitudes)
    lat_promedio = sum(latitudes) / n
    lon_promedio = sum(longitudes) / n
    return lat_promedio, lon_promedio

# Ejemplo de latitudes y longitudes de cuatro ubicaciones (sustituye estos valores con los tuyos)
latitudes = [-24.7874, -24.7883, -24.7996, -24.7869, -24.7890, -24.7911]
longitudes = [-65.4098, -65.4109, -65.4317, -65.4086,-65.4110,-65.4138]

lat_central, lon_central = ubicacion_central(latitudes, longitudes)


lon_central_con_mas_digitos = round(lon_central, 17)

# Convertir la longitud redondeada a una cadena con formato para mostrar más dígitos
lon_central_str = "{:.17f}".format(lon_central_con_mas_digitos)

print(f"Ubicación central: Latitud = {lat_central}, Longitud = {lon_central_str}")

print(len("-24.790383333333335"))