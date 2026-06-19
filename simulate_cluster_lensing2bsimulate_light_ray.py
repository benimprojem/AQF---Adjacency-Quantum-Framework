import numpy as np
import matplotlib.pyplot as plt

# 1. Uzay Izgarası ve Küme Tanımlama
size = 150
grid = np.linspace(-15, 15, size)
X, Y = np.meshgrid(grid, grid)

# 2. Çoklu Galaksi Yapısı (Her galaksinin farklı yoğunluk ve boyutu var)
# Galaxy_i = (x, y, yoğunluk, boyut)
galaxies = [(-7, -5, 15, 2.0), (3, 4, 20, 1.5), (6, -3, 12, 2.5), (-2, 2, 25, 1.2)]

rho_total = np.zeros_like(X)
for gx, gy, density, size_factor in galaxies:
    # Her galaksi bir Gaussian "Adjacency Fold" (Topolojik Buruşukluk)
    rho_total += density * np.exp(-((X-gx)**2 + (Y-gy)**2) / (size_factor**2))

W = 1 + 0.3 * rho_total  # Topolojik Distorsiyon alanı

# 3. Işık Yolu Simülasyonu (Bileşke gradyanı takip et)
def get_lensed_paths_multi(start_x, start_y, n_rays=10):
    paths = []
    for y_offset in np.linspace(-2, 2, n_rays):
        path = []
        pos = np.array([start_x, start_y + y_offset])
        for _ in range(500):
            grad_y, grad_x = np.gradient(W)
            ix, iy = int((pos[0]+15)/0.2), int((pos[1]+15)/0.2)
            if 0 <= ix < size and 0 <= iy < size:
                # Topolojik direnç gradyanına göre sapma
                pos[0] += 0.3 # İlerleme hızı
                pos[1] -= grad_y[iy, ix] * 0.5 
                path.append(pos.copy())
        paths.append(np.array(path))
    return paths

paths = get_lensed_paths_multi(-14, 0)

# 4. Görselleştirme
plt.figure(figsize=(12, 10))
plt.contourf(X, Y, W, levels=30, cmap='inferno', alpha=0.4)
plt.colorbar(label='Topolojik Düğüm Yoğunluğu (W)')

# Galaksileri işaretle
for gx, gy, d, s in galaxies:
    plt.scatter(gx, gy, color='white', s=d*5, edgecolors='black')

# Işık yolları (Çatallanma ve Merceklenme)
for p in paths:
    plt.plot(p[:,0], p[:,1], color='cyan', linewidth=1.2, alpha=0.9)

plt.title("AQF Çoklu Galaksi Kümesi ve Topolojik Merceklenme")
plt.xlabel("X (Adjacency)")
plt.ylabel("Y (Adjacency)")
plt.show()