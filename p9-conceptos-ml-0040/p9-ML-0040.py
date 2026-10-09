# Hugo Fabian NC = 0040
# nl = 17
import pandas as pd

# 17.
datos17 = {
    'distancia_km': [2.6, 4.7, 1.3, 3.3, 5.9],
    'trafico_nivel': [1, 2, 3, 1, 3],
    'edad_repartidor': [29, 38, 21, 32, 43],
    'tiempo_entrega_min': [19, 38, 13, 22, 56]
}

df = pd.DataFrame(datos17)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['distancia_km', 'trafico_nivel', 'edad_repartidor']] # Features / Entradas
y = df['tiempo_entrega_min']                                  # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Huo Fabian NC = 0040")

print("+-+-+-+-+-+-+-+-+ segundo codigo-+-+-+-+-+-+-+-+-+")

# Hugo Fabian NC = 0040
# nl = 17
import pandas as pd

# 1. Dataset
datos = {
    'edad': [45, 23, 60, 35, 50],
    'nivel_glucosa': [140, 85, 180, 95, 130],
    'presion_arterial': [80, 70, 90, 75, 85],
    'indice_masa_corporal': [28.5, 21.0, 33.2, 24.1, 29.8],
    'diagnostico_diabetes': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(datos)

# 2. Separar Variables de Entrada (X) y Variable Objetivo (y)
X = df[['edad', 'nivel_glucosa', 'presion_arterial', 'indice_masa_corporal']] # Features / Entradas
y = df['diagnostico_diabetes']                                            # Target / Salida

# 3. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

print("Hugo Fabian NC = 0040")
