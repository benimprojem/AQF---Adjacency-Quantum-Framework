import numpy as np
import matplotlib.pyplot as plt

def generate_complex_cluster(grid_size=60):
    # Uzay alanı
    x = np.linspace(-15, 15, grid_size)
    y = np.linspace(-15, 15, grid_size)
    X, Y = np.meshgrid(x, y)
    
    # 1. Galaktik Adalar (Galaksileri ayrı ayrı tanımlıyoruz)
    # 5 ana galaksi adası yerleştiriyoruz
    galaxies = [(-5, -5), (5, 5), (-5, 5), (5, -5), (0, 0)]
    B_total = np.zeros_like(X)
    
    for gx, gy in galaxies:
        # Her galaksi bir "Adjacency Fold" (Buruşukluk tepesi)
        B_total += 10 * np.exp(-((X - gx)**2 + (Y - gy)**2) / 2)
        
    # 2. Galaksiler Arası Gerilme Alanı (Inter-cluster tension)
    # Boşluktaki gerilme, galaksiler arası bağdır
    B_total += 0.5 * np.sin(X/2) * np.cos(Y/2) 
    
    return X, Y, B_total

X, Y, B = generate_complex_cluster()

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# 3D Yüzey: Galaktik adalar ve aralarındaki boşluk dokusu
surf = ax.plot_surface(X, Y, B, cmap='terrain', alpha=0.9, edgecolor='k', linewidth=0.1)

ax.set_title("AQF Hiper-Topolojik Küme Modeli (Galaksiler ve Arası Ağ)")
ax.set_zlabel("Topolojik Buruşukluk (Fold Degree)")
fig.colorbar(surf, shrink=0.5, label='Buruşukluk İndeksi')

plt.show()