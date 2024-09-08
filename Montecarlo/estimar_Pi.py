import numpy as np
import matplotlib.pyplot as plt

# Parámetros
num_puntos = 1000000  # Número inicial de puntos a generar
precision_deseada = 1e-5  # Precisión de 5 cifras

# Función para estimar Pi con Montecarlo
def estimar_pi_montecarlo(num_puntos):
    puntos_x = np.random.uniform(-1, 1, num_puntos)
    puntos_y = np.random.uniform(-1, 1, num_puntos)
    dentro_circulo = puntos_x**2 + puntos_y**2 <= 1
    puntos_dentro = np.sum(dentro_circulo)
    return 4 * (puntos_dentro / num_puntos)

# Loop para lograr precisión deseada
pi_estimacion = 0
diferencia = 1  # Iniciar con una diferencia mayor que la precisión deseada
while diferencia > precision_deseada:
    pi_estimacion = estimar_pi_montecarlo(num_puntos)
    diferencia = abs(np.pi - pi_estimacion)

# Generar puntos para la visualización
num_puntos_visualizacion = 10000
puntos_x = np.random.uniform(-1, 1, num_puntos_visualizacion)
puntos_y = np.random.uniform(-1, 1, num_puntos_visualizacion)

# Determinar si los puntos están dentro del círculo
dentro_circulo = puntos_x**2 + puntos_y**2 <= 1

# Crear gráfico
plt.figure(figsize=(6, 6))
plt.scatter(puntos_x[dentro_circulo], puntos_y[dentro_circulo], color='green', s=1, label='Dentro del círculo')
plt.scatter(puntos_x[~dentro_circulo], puntos_y[~dentro_circulo], color='red', s=1, label='Fuera del círculo')
plt.title(f'Estimación de Pi usando Montecarlo\nEstimación: {pi_estimacion:.5f}')
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

print(f"Estimación de Pi: {pi_estimacion:.5f}")
