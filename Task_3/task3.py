import numpy as np
import matplotlib.pyplot as plt

def update_pose_with_noise(x, y, theta, v, omega, dt, mu, sigma_v, sigma_omega):
    v_noisy = v + np.random.normal(mu, sigma_v)
    omega_noisy = omega + np.random.normal(mu, sigma_omega)
    x_new = x + v_noisy * np.cos(theta) * dt
    y_new = y + v_noisy * np.sin(theta) * dt
    theta_new = theta + omega_noisy * dt
    return x_new, y_new, theta_new

def control_law(x, y, theta, goal_x, goal_y, kv, kw):
    error_x = goal_x - x
    error_y = goal_y - y
    error_theta = np.arctan2(error_y, error_x) - theta
    v = kv * np.sqrt(error_x ** 2 + error_y ** 2)
    omega = kw * error_theta
    return v, omega

dt = 0.1
total_time = 20.0
kv = 0.15
kw = 1.5
mu = 0
sigma_v = 0.10
sigma_omega = 0.10

x, y, theta = 0, 0, 0
goal_x, goal_y = 4, -3

history_x, history_y = [x], [y]

for t in np.arange(0, total_time, dt):
    v, omega = control_law(x, y, theta, goal_x, goal_y, kv, kw)
    x, y, theta = update_pose_with_noise(x, y, theta, v, omega, dt, mu, sigma_v, sigma_omega)
    history_x.append(x)
    history_y.append(y)
    if np.sqrt((goal_x - x) ** 2 + (goal_y - y) ** 2) < 0.3:
        break

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
