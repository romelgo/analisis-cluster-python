# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/151qZP36lMqf68ZJhARbeb20cand-ky_S

**Resumen**:
"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Cargar el archivo CSV (este es tu archivo)
file_path = 'datos.csv'
df = pd.read_csv(file_path)

# Seleccionar las columnas relevantes para el análisis de conglomerados
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Aplicación del algoritmo K-means
kmeans = KMeans(n_clusters=3, random_state=42)  # Cambia n_clusters según tus necesidades
kmeans.fit(data_scaled)

# Asignación de etiquetas a cada punto de datos
labels = kmeans.labels_

# Agregar las etiquetas al DataFrame original
df['Cluster'] = labels

# Visualización de los conglomerados (solo se usarán las primeras dos variables para graficar)
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=labels, cmap='viridis')
plt.title('Resultado del K-means clustering')
plt.xlabel('Edad (escalada)')
plt.ylabel('Divertid (escalada)')
plt.show()

# Mostrar centroides
centroids = kmeans.cluster_centers_
print('Centroides de los clusters:', centroids)

# Mostrar el DataFrame con los clusters asignados
print(df.head())

"""***Detalles:..***

---

# **calcular la matriz de proximidades**
"""

# Seleccionar las columnas relevantes para el análisis
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Calcular la matriz de distancias utilizando la distancia euclidiana
# pdist calcula las distancias por pares entre los puntos
distance_matrix = pdist(data_scaled, metric='euclidean')

# Convertir la matriz de distancias a una forma cuadrada (de proximidades)
proximity_matrix = squareform(distance_matrix)

# Convertir la matriz a un DataFrame para una visualización más clara
proximity_df = pd.DataFrame(proximity_matrix, index=df.index, columns=df.index)

# Mostrar las primeras filas de la matriz de proximidades
print(proximity_df.head())

"""# **Historial de conglomeración (dendrograma):**"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Seleccionar las columnas relevantes para el análisis de conglomerados jerárquicos
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Calcular la matriz de enlaces utilizando el método 'ward' (puedes cambiarlo por otros como 'single', 'complete')
linked = linkage(data_scaled, method='ward')

# Graficar el dendrograma
plt.figure(figsize=(10, 7))
dendrogram(linked,
           orientation='top',
           distance_sort='descending',
           show_leaf_counts=True)
plt.title('Dendrograma - Historial de Conglomeración')
plt.xlabel('Índice de Muestras')
plt.ylabel('Distancia Euclidiana')
plt.show()

"""# **¿Qué método de conglomeración es mejor?**

# Ward's Method (ward):

**Descripción:** Minimiza la varianza total dentro de cada conglomerado. Es uno de los métodos más utilizados porque tiende a generar conglomerados más compactos y de tamaño similar.

**Ventaja:** Es útil cuando los conglomerados tienen forma esférica y cuando se busca minimizar la variabilidad dentro de los conglomerados.
Cuándo usarlo: Si quieres que los conglomerados sean lo más compactos y homogéneos posible.

# **Gráfico de Componentes Principales (PCA)**
"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# Seleccionar las columnas relevantes para el análisis
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Aplicar PCA para reducir a 2 componentes principales
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data_scaled)

# Crear un DataFrame con los resultados de los componentes principales
df_pca = pd.DataFrame(pca_result, columns=['Componente 1', 'Componente 2'])

# Graficar los dos primeros componentes principales
plt.figure(figsize=(8, 6))
plt.scatter(df_pca['Componente 1'], df_pca['Componente 2'], c='blue', edgecolor='k', s=50)
plt.title('Gráfico de Componentes Principales (PCA)')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.grid(True)
plt.show()

# Opcional: Mostrar la varianza explicada por cada componente
explained_variance = pca.explained_variance_ratio_
print(f'Varianza explicada por el Componente 1: {explained_variance[0]:.2f}')
print(f'Varianza explicada por el Componente 2: {explained_variance[1]:.2f}')

"""# **Dendrograma Mejorado - Método de Ward**"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Seleccionar las columnas relevantes para el análisis
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Aplicación del algoritmo jerárquico aglomerativo con el método de Ward
linked = linkage(data_scaled, method='ward')

# Tamaño de la figura para mejorar la visualización
plt.figure(figsize=(12, 8))

# Generar el dendrograma con etiquetas de hojas
dendrogram(linked,
           orientation='top',  # Cambia a 'left' o 'right' para otra orientación
           labels=df.index,  # Etiquetas para las hojas
           distance_sort='descending',  # Ordenar por distancia
           show_leaf_counts=True,  # Mostrar el número de puntos en cada conglomerado
           leaf_rotation=90,  # Rotación de etiquetas de las hojas
           leaf_font_size=10,  # Tamaño de la fuente de las etiquetas
           color_threshold=0.7 * max(linked[:, 2]),  # Umbral para colorear clusters
           above_threshold_color='gray'  # Color para las uniones que están por encima del umbral
           )

# Título y etiquetas de los ejes
plt.title('Dendrograma Mejorado - Método de Ward', fontsize=14)
plt.xlabel('Índice de Muestras o Casos', fontsize=12)
plt.ylabel('Distancia Euclidiana', fontsize=12)

# Mostrar el dendrograma
plt.tight_layout()
plt.show()

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Seleccionar las columnas para el análisis de regresión
# Cambia 'columna_X' y 'columna_Y' por las columnas que quieras analizar
X = df[['Edad']]  # Variable independiente (predictora)
y = df['Divertid']  # Variable dependiente (a predecir)

# Crear y ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predecir valores de 'y' utilizando el modelo ajustado
y_pred = model.predict(X)

# Crear un diagrama de dispersión
plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, y_pred, color='red', label='Línea de regresión')

# Añadir títulos y etiquetas
plt.title('Diagrama de Dispersión con Línea de Regresión')
plt.xlabel('Edad')  # Cambia según tu variable X
plt.ylabel('Divertid')  # Cambia según tu variable Y
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()

# Mostrar la pendiente y la intersección de la recta de regresión
print(f'Pendiente (coeficiente): {model.coef_[0]}')
print(f'Intersección: {model.intercept_}')

"""# **ANOVA**"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


# Realizar ANOVA
# Cambia 'Divertid' por la variable dependiente y 'Sexo' por la variable independiente
model = ols('Divertid ~ C(Sexo)', data=df).fit()
anova_table = anova_lm(model, typ=2)

# Calcular eta cuadrado (tamaño del efecto)
anova_table['eta_sq'] = anova_table['sum_sq'] / sum(anova_table['sum_sq'])

# Calcular eta cuadrado parcial
anova_table['eta_sq_partial'] = anova_table['sum_sq'] / (anova_table['sum_sq'] + anova_table['resid'] if 'resid' in anova_table.columns else anova_table['sum_sq'])

# Mostrar la tabla de ANOVA con el tamaño del efecto
print(anova_table)

"""# **Clustering K-means**"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Seleccionar las columnas relevantes para el análisis de K-means
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos (opcional pero recomendado para K-means)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Definir el número de clusters (k)
k = 3  # Cambia este valor según tus necesidades

# Aplicar el algoritmo K-means
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(data_scaled)

# Asignación de etiquetas a cada punto de datos
labels = kmeans.labels_

# Agregar las etiquetas al DataFrame original
df['Cluster'] = labels

# Información de los centroides
centroids = kmeans.cluster_centers_

# Visualización de los resultados utilizando las primeras dos características
plt.figure(figsize=(8, 6))
plt.scatter(data_scaled[:, 0], data_scaled[:, 1], c=labels, cmap='viridis', s=50)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X')  # Marcadores de centroides
plt.title('Clustering K-means')
plt.xlabel('Edad (escalada)')
plt.ylabel('Divertid (escalada)')
plt.grid(True)
plt.show()

# Mostrar el DataFrame con los clusters asignados
print(df.head())

"""# **Diagrama de Dispersión Agrupado con K-means**"""

# Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



# Seleccionar las columnas relevantes para el análisis de K-means
data = df[['Edad', 'Divertid', 'Pidocomp', 'Aprendom', 'Excur', 'Quitatie', 'Nomeint', 'Gustovis']]

# Estandarización de los datos (opcional pero recomendado para K-means)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Definir el número de clusters (k) = 3
k = 3  # Agrupación en 3 clusters

# Aplicar el algoritmo K-means
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(data_scaled)

# Asignación de etiquetas a cada punto de datos
labels = kmeans.labels_

# Agregar las etiquetas al DataFrame original
df['Cluster'] = labels

# Información de los centroides
centroids = kmeans.cluster_centers_

# Visualización de los resultados utilizando las primeras dos características (Ej: Edad y Divertid)
plt.figure(figsize=(8, 6))
for cluster in range(k):
    # Filtrar los puntos que pertenecen a cada cluster
    plt.scatter(data_scaled[labels == cluster, 0], data_scaled[labels == cluster, 1],
                label=f'Cluster {cluster+1}', s=50)

# Graficar los centroides
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.75, marker='X', label='Centroides')

# Títulos y etiquetas
plt.title('Diagrama de Dispersión Agrupado con K-means')
plt.xlabel('Edad (escalada)')
plt.ylabel('Divertid (escalada)')
plt.legend()
plt.grid(True)
plt.show()

# Mostrar el DataFrame con los clusters asignados
print(df.head())