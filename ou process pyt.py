import numpy as np
import matplotlib.pyplot as plt
theta = 3.0 
mu = 1.0 
sigma = 0.1
T = 2.0 
N = 1000 
dt = T/N
t = np.linspace(0, T, N) 
X = np.zeros(N) 
X[0] = 1.5 
for i in range(1, N):
    dw= np.sqrt(dt) * np.random.randn()
    X[i] = X[i-1] + theta* (mu - X[i-1])*dt + sigma*dw

plt.plot(t, X, label='OU process $X_t$')
plt.axhline (mu, linestyle='--', label='Mean level $\mu$')
plt.title('Simulated Ornstein-Uhlenbeck Process')
plt.xlabel('Time $t$')
plt.ylabel('$X_t$')
plt.legend()
plt.grid(True)
plt.show()