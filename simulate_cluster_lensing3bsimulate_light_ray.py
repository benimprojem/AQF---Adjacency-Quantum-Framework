import numpy as np
import matplotlib.pyplot as plt

# 1. Uzay ve Distorsiyon Alanı (W) Hazırlığı
size = 100
x = np.linspace(-10, 10, size)
X, Y = np.meshgrid(x, x)
# Küme merkezi (yoğunluk dağılımı)
rho = 8 * np.exp(-(X**2 + Y**2) / 8) 
W = 1 + 0.5 * rho # AQF Distorsiyon alanı

# 2. Işık Işını Simülasyonu (Gradyan takibi - Lensing)
# Işık, distorsiyonun (W) en düşük olduğu yere doğru "kırılır" (refraksiyon)
def simulate_light_ray(start_pos, steps=200):
    ray = [start_pos]
    pos = np.array(start_pos, dtype=float)
    dt = 0.2
    for _ in range(steps):
        # Gradyan hesapla (Işık W gradyanına dik hareket eder)
        grad_y, grad_x = np.gradient(W)
        ix, iy = int(pos[0]/0.2 + size/2), int(pos[1]/0.2 + size/2)
        if 0 <= ix < size and 0 <= iy < size:
            # İvmelenme: Işık "yoğunluk kuyusuna" doğru bükülür
            pos[0] -= grad_x[iy, ix] * dt
            pos[1] -= grad_y[iy, ix] * dt
        ray.append(pos.copy())
    return np.array(ray)

# 3. Görselleştirme
rays = [simulate_light_ray([-8, y0]) for y0 in np.linspace(-4, 4, 10)]

plt.figure(figsize=(10, 8))
plt.imshow(W, extent=[-10, 10, -10, 10], cmap='magma', origin='lower', alpha=0.6)
for ray in rays:
    plt.plot(ray[:,0], ray[:,1], color='cyan', alpha=0.7)
plt.title("AQF Topolojik Merceklenme: Işık Yolu Simülasyonu")
plt.xlabel("X (Adjacency)")
plt.ylabel("Y (Adjacency)")
plt.colorbar(label='Topolojik Distorsiyon (W)')
plt.show()