import numpy as np
import matplotlib.pyplot as plt

mu_0 = np.array([0, 0, 0])
Sigma_0 = np.eye(3)

dt = 0.1
V_k = 1.0
omega_k = 0.1
Q_x = np.eye(3) * 0.1

def compute_H_k(mu_theta_k_minus_1):
    theta_k_minus_1 = mu_theta_k_minus_1[2]
    H_k = np.array([
        [1, 0, -dt * V_k * np.sin(theta_k_minus_1)],
        [0, 1, dt * V_k * np.cos(theta_k_minus_1)],
        [0, 0, 1]
    ])
    return H_k

mu_k = mu_0
Sigma_k = Sigma_0

x_trajectory = [mu_0[0]]
y_trajectory = [mu_0[1]]

for k in range(1, 100):
    H_k = compute_H_k(mu_k)

    Sigma_k = H_k @ Sigma_k @ H_k.T + Q_x

    mu_k = np.array([mu_k[0] + dt * V_k * np.cos(mu_k[2]),
                     mu_k[1] + dt * V_k * np.sin(mu_k[2]),
                     mu_k[2] + dt * omega_k])

    x_trajectory.append(mu_k[0])
    y_trajectory.append(mu_k[1])

plt.plot(x_trajectory, y_trajectory, label='Траектория движения робота')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Траектория движения робота')
plt.legend()
plt.grid(True)
plt.show()
