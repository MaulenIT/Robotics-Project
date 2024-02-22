import numpy as np
import matplotlib.pyplot as plt


# Функция для обновления положения робота
def update_pose(x, y, theta, v, omega, dt):
    x_new = x + v * np.cos(theta) * dt
    y_new = y + v * np.sin(theta) * dt
    theta_new = theta + omega * dt
    return x_new, y_new, theta_new


# Функция для расчёта управляющих сигналов
def control_law(x, y, theta, goal_x, goal_y, kv, kw):
    error_x = goal_x - x
    error_y = goal_y - y
    error_theta = np.arctan2(error_y, error_x) - theta

    v = kv * np.sqrt(error_x ** 2 + error_y ** 2)
    omega = kw * error_theta

    return v, omega


# Параметры симуляции
dt = 0.1
total_time = 20.0
kv = 0.15
kw = 1.5

# Начальное положение робота и цель
x, y, theta = 0, 0, 0
goal_x, goal_y = 4, -3

# История положений для визуализации
history_x = [x]
history_y = [y]

# Цикл симуляции
for t in np.arange(0, total_time, dt):
    v, omega = control_law(x, y, theta, goal_x, goal_y, kv, kw)
    x, y, theta = update_pose(x, y, theta, v, omega, dt)

    history_x.append(x)
    history_y.append(y)

    # Условие остановки, если робот достаточно близко к цели
    if np.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2) < 0.3:
        break

# Визуализация пути робота
plt.figure()
plt.plot(history_x, history_y, label='Path of the robot')
plt.plot(goal_x, goal_y, 'rx', label='Goal')
plt.title('Robot Path to Goal')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
