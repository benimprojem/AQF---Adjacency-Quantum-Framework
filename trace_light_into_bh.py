import numpy as np
import matplotlib.pyplot as plt

# 1. Uzay ve Rotasyonel Direnç Alanı (Vortex Field)
n = 150
grid = np.linspace(-15, 15, n)
X, Y = np.meshgrid(grid, grid)
R = np.sqrt(X**2 + Y**2)

# Rotasyonel Doygunluk: Merkezde dönen bir direnç yapısı
theta = np.arctan2(Y, X)
# Merkezdeki stres, sarmal bir yapı (vortex) ile dağılır
R_A = np.exp( (2.0 / (R + 0.1)) + 0.5 * np.sin(theta - R/2) )

# 2. Işık Yolu: Açısal momentum (L) ve Stres Gradyanı
def trace_spiral_path(start_pos, steps=1000):
    path = []
    pos = np.array(start_pos, dtype=float)
    dt = 0.05
    # Açısal momentum: Işığın sarmal çizmesini sağlayan bileşen
    L = 2.0 
    
    for _ in range(steps):
        grad_y, grad_x = np.gradient(np.log(R_A + 1e-6))
        # Topolojik Direnç Kuvveti + Açısal Momentum bileşeni
        accel = -np.array([grad_x[int((pos[1]+15)/(30/n)), int((pos[0]+15)/(30/n))], 
                           grad_y[int((pos[1]+15)/(30/n)), int((pos[0]+15)/(30/n))]])
        
        # Hız güncelleme (Sarmal etki)
        vel = accel + np.array([-pos[1], pos[0]]) * (L / (R.max() + 1))
        pos += vel * dt
        path.append(pos.copy())
        
        if np.linalg.norm(pos) < 0.8: break # Olay ufku sınırı
    return np.array(path)

# 3. Görselleştirme
paths = [trace_spiral_path([-12, y]) for y in np.linspace(-5, 5, 15)]

plt.figure(figsize=(12, 10))
plt.contourf(X, Y, np.log(R_A), levels=60, cmap='inferno', alpha=0.6)
plt.colorbar(label='Log(Topolojik Direnç)')

for path in paths:
    plt.plot(path[:,0], path[:,1], color='cyan', alpha=0.6, linewidth=1.2)

plt.title("AQF Sarmal Kara Delik: Işığın Topolojik Vorteks İçine Düşüşü")
plt.xlabel("X (Adjacency)")
plt.ylabel("Y (Adjacency)")
plt.show()