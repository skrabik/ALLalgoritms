import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 12, 500)  # Создаем массив значений времени от 0 до 12 с шагом 0.1
x = 3*t - 0.25*t**2 # Рассчитываем координату x для каждого значения времени

plt.figure(figsize=(10, 6))
plt.plot(t, x, label='x = 3t - 0.25t^2', color='b')
plt.xlabel('Время t')
plt.ylabel('Координата x')
plt.title('График зависимости координаты x от времени t')
plt.grid(True)
plt.legend()
plt.show()


s = 3*t**2/2 - 0.25*t**3/3  # Вычисляем путь s как интеграл координаты x по времени

plt.figure(figsize=(10, 6))
plt.plot(t, s, label='s = 3t^2/2 - 0.25t^3/3', color='r')
plt.xlabel('Время t')
plt.ylabel('Путь s')
plt.title('График зависимости пути от времени')
plt.grid(True)
plt.legend()
plt.show()