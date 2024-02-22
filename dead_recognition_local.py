import numpy as np
import matplotlib.pyplot as plt

print('Enter x: ')
x0 = input()
print('Enter Y: ')
y0 = input()
print('Enter theta0: ')
theta0 = input()



# Parameters
v = 0.3
omega = 0.0
dt = 0.1
t_end = 10

t = np.arange(0, t_end, dt)

x = np.zeros_like(t)
y = np.zeros_like(t)
theta = np.zeros_like(t)

x[0], y[0], theta[0] = x0, y0, theta0

for i in range(1, len(t)):
    theta[i] = theta0

    x[i] = x[i - 1] + v * np.cos(theta[i - 1]) * dt
    y[i] = y[i - 1] + v * np.sin(theta[i - 1]) * dt

plt.figure(figsize=(12, 6))
plt.plot(x, y, label='Robot Path')
plt.plot(x[0], y[0], 'go', label='Start')
plt.plot(x[-1], y[-1], 'ro', label='End')
plt.quiver(x[::5], y[::5], np.cos(theta[::5]), np.sin(theta[::5]), scale=20)
plt.title('Robot Trajectory with Zero Angular Velocity')
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
