import numpy as np
import matplotlib.pyplot as plt

# 1. 3D Küme Doku Hazırlığı
n = 60
x = np.linspace(-15, 15, n)
y = np.linspace(-15, 15, n)
X, Y = np.meshgrid(x, y)

# Coma benzeri 3 ana yoğunluk merkezi (Galaksiler)
rho = (10 * np.exp(-((X-3)**2 + (Y-3)**2)/5) + 
       8 * np.exp(-((X+4)**2 + (Y+2)**2)/4) + 
       6 * np.exp(-((X)**2 + (Y+5)**2)/6))

W = 1 + 0.6 * rho # Topolojik Distorsiyon alanı

# 2. Işık Yolu Takibi (Gradient Descent on W-Field)
def get_light_paths(start_x, start_y, n_rays=5):
    paths = []
    for i in np.linspace(-1, 1, n_rays):
        path = [[start_x, start_y, 0]]
        curr_pos = np.array([start_x, start_y])
        dt = 0.5
        for _ in range(100):
            # Gradyan: Işık W alanının "yokuş aşağı" aktığı yere çekilir
            grad_y, grad_x = np.gradient(W)
            ix = int(np.clip((curr_pos[0]+15)/0.5, 0, n-1))
            iy = int(np.clip((curr_pos[1]+15)/0.5, 0, n-1))
            
            curr_pos[0] -= grad_x[iy, ix] * dt
            curr_pos[1] -= grad_y[iy, ix] * dt
            # Z ekseni (Fold yüksekliği) buruşukluğu gösterir
            z = W[iy, ix] 
            path.append([curr_pos[0], curr_pos[1], z])
        paths.append(np.array(path))
    return paths

# 3. Görselleştirme
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Yüzey: Galaktik kümenin 3D buruşukluğu
surf = ax.plot_surface(X, Y, W, cmap='viridis', alpha=0.5)

# Işık yolları (Arka plandan küme merkezine)
for path in get_light_paths(-12, 0):
    ax.plot(path[:,0], path[:,1], path[:,2], color='red', linewidth=2)

ax.set_title("AQF 3D Işık Yolu: Topolojik Merceklenme")
ax.set_zlabel("Topolojik Distorsiyon (W)")
plt.show()