import numpy as np
import matplotlib.pyplot as plt

# Parámetros para el círculo de radio 3 centrado en (-1, 0)
radio = 3
centro_x = -1
centro_y = 0
num_puntos = 1000000  # Número de puntos a generar
lado_cuadrado = 2 * radio  # El cuadrado va desde (-4, -3) hasta (2, 3)

# Generar puntos aleatorios en el cuadrado
puntos_x = np.random.uniform(centro_x - radio, centro_x + radio, num_puntos)
puntos_y = np.random.uniform(centro_y - radio, centro_y + radio, num_puntos)

# Contar cuántos puntos están dentro del círculo
dentro_circulo = (puntos_x - centro_x)**2 + (puntos_y - centro_y)**2 <= radio**2
puntos_dentro = np.sum(dentro_circulo)

# Estimar el área del círculo
area_cuadrado = lado_cuadrado**2
area_circulo_real = np.pi * (radio**2)
area_estimacion = (puntos_dentro / num_puntos) * area_cuadrado

# Generar puntos para la visualización
num_puntos_visualizacion = 10000
puntos_x_vis = np.random.uniform(centro_x - radio, centro_x + radio, num_puntos_visualizacion)
puntos_y_vis = np.random.uniform(centro_y - radio, centro_y + radio, num_puntos_visualizacion)

# Determinar si los puntos están dentro del círculo para la visualización
dentro_circulo_vis = (puntos_x_vis - centro_x)**2 + (puntos_y_vis - centro_y)**2 <= radio**2

# Crear gráfico
plt.figure(figsize=(6, 6))
plt.scatter(puntos_x_vis[dentro_circulo_vis], puntos_y_vis[dentro_circulo_vis], color='green', s=1, label='Dentro del círculo')
plt.scatter(puntos_x_vis[~dentro_circulo_vis], puntos_y_vis[~dentro_circulo_vis], color='red', s=1, label='Fuera del círculo')
plt.title(f'Estimación del área del círculo (radio=3, centro=(-1,0))\nEstimación: {area_estimacion:.5f}')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

print(f"Área Real del círculo: {area_circulo_real:.5f}")
print(f"Estimación del área del círculo: {area_estimacion:.5f} con {num_puntos} puntos")
