import numpy as np
import matplotlib.pyplot as plt

# 1. Uzay ve Polar Direnç Alanı
n = 100 # Izgara boyutunu optimize ettim
grid = np.linspace(-10, 10, n)
X, Y = np.meshgrid(grid, grid)
R = np.sqrt(X**2 + Y**2)
theta = np.arctan2(Y, X)

# Direnç fonksiyonu
resistance = np.exp( (3.0 / (R + 0.5)) - 0.5 * np.cos(2 * theta) )

# 2. Işık Yolu ve Deşarj Simülasyonu
def simulate_discharge(n_rays=15):
    paths = []
    for i in np.linspace(-1, 1, n_rays):
        path = []
        pos = np.array([-9.0, i * 2])
        vel = np.array([0.4, 0.0])
        
        for _ in range(400):
            # Koordinatları 0-99 arasına indirge (indeks güvenliği)
            ix = int(np.clip((pos[0] + 10) / 20 * (n - 1), 0, n - 1))
            iy = int(np.clip((pos[1] + 10) / 20 * (n - 1), 0, n - 1))
            
            # Gradyan hesapla
            grad_y, grad_x = np.gradient(np.log(resistance + 1e-6))
            
            # İvme ve Hız kontrolü
            accel = -0.5 * np.array([grad_x[iy, ix], grad_y[iy, ix]])
            rot = np.array([-pos[1], pos[0]]) * 0.05
            
            # Merkeze yaklaştıkça ivmeyi sönümle (ivme -> 0)
            dist_to_center = np.linalg.norm(pos)
            damping = np.clip(dist_to_center - 0.8, 0, 1)
            
            vel = (vel + accel + rot) * damping
            pos += vel * 0.2
            
            path.append(pos.copy())
            if dist_to_center < 0.8: break # Doygunluk noktası
        paths.append(np.array(path))
    return paths

paths = simulate_discharge()

# 3. Görselleştirme
plt.figure(figsize=(10, 10))
plt.contourf(X, Y, np.log(resistance), levels=50, cmap='inferno', alpha=0.4)

for path in paths:
    p = np.array(path)
    plt.plot(p[:,0], p[:,1], color='cyan', alpha=0.6, linewidth=1)

# Jet (Kırmızı kutup ışınları)
plt.plot([0, 0], [1, 10], color='red', linestyle='--', linewidth=3)
plt.plot([0, 0], [-1, -10], color='red', linestyle='--', linewidth=3)

plt.scatter([0], [0], color='white', s=100, edgecolors='black')
plt.title("AQF: İvme Sıfırlanması ve Topolojik Jet Deşarjı")
plt.xlim(-10, 10); plt.ylim(-10, 10)
plt.show()