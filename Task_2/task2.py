import numpy as np
import matplotlib.pyplot as plt

# Parameters for simulation
dt = 0.1
total_time = 9.78
v = 0.30
omega = 1.0

mu = 0
sigma_v = 0.01
sigma_omega = 0.005


x = np.array([0.0, 0.0, 0.0])

# Store history for plotting
history = np.zeros((int(total_time / dt) + 1, 3))
history[0] = x

for i in range(1, int(total_time / dt) + 1):
    v_noisy = v + np.random.normal(mu, sigma_v)
    omega_noisy = omega + np.random.normal(mu, sigma_omega)


    dx = np.array([np.cos(x[2]), np.sin(x[2]), omega])

    x += v * dx * dt

    history[i] = x

x_hist, y_hist, theta_hist = history[:, 0], history[:, 1], history[:, 2]

plt.figure()
plt.plot(x_hist, y_hist, label='Robot Path')
plt.quiver(x_hist[::10], y_hist[::10], np.cos(theta_hist[::10]), np.sin(theta_hist[::10]), scale=20)
plt.xlabel('X position')
plt.ylabel('Y position')
plt.title('Simulation of Dead Reckoning Localization')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()
