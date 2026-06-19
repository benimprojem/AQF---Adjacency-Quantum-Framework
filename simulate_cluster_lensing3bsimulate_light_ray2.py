import numpy as np
import matplotlib.pyplot as plt

# 1. Küme (Düğüm Yoğunluğu) Tanımlama
size = 100
grid = np.linspace(-10, 10, size)
X, Y = np.meshgrid(grid, grid)

# Küme merkezinde yoğun bir 'Fold' (Topolojik kuyu) tanımlıyoruz
rho = 10 * np.exp(-((X)**2 + (Y)**2) / 10) 
W = 1 + 0.8 * rho # Distorsiyon alanı

# 2. Çoklu Yol (Lensing) Simülasyonu
# Kaynak (Source) pozisyonu: Kümenin tam arkası [-9, 0]
def trace_multiple_rays(start, steps=300):
    paths = []
    # Işığın hafif farklı açılarla çıktığını simüle ediyoruz
    for angle in np.linspace(-0.5, 0.5, 5):
        pos = np.array(start, dtype=float)
        vel = np.array([1.0, angle]) # İlk hız vektörü
        path = [pos.copy()]
        for _ in range(steps):
            # Gradyan: Işık W'nin azaldığı (düğüm yoğunluğu az) yere çekilir
            grad_y, grad_x = np.gradient(W)
            ix, iy = int((pos[0]+10)/0.2), int((pos[1]+10)/0.2)
            if 0 <= ix < size and 0 <= iy < size:
                vel[0] -= grad_x[iy, ix] * 0.05
                vel[1] -= grad_y[iy, ix] * 0.05
            pos += vel * 0.1
            path.append(pos.copy())
        paths.append(np.array(path))
    return paths

paths = trace_multiple_rays([-9, 0])

# 3. Görselleştirme
plt.figure(figsize=(10, 8))
plt.imshow(W, extent=[-10, 10, -10, 10], cmap='inferno', origin='lower', alpha=0.3)
for p in paths:
    plt.plot(p[:,0], p[:,1], color='cyan', linewidth=1.5)
plt.scatter([0], [0], color='red', marker='+', s=200, label="Küme Merkezi (Saturasyon)")
plt.title("AQF Topolojik Merceklenme: Çoklu Yol Çatallanması")
plt.legend()
plt.show()