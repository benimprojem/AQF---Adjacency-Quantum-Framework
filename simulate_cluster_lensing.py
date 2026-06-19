import numpy as np
import matplotlib.pyplot as plt

# --- 1. KÜME VE GALAKSİ MODELLEME ---
def simulate_cluster_lensing(num_galaxies=15):
    # Galaksi merkezleri (rastgele konumlar)
    pos = np.random.uniform(-5, 5, (num_galaxies, 2))
    
    # Grid üzerinde yoğunluk haritası
    grid = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(grid, grid)
    rho_total = np.zeros_like(X)
    
    for i in range(num_galaxies):
        # Her galaksi bir "adjacency cluster" oluşturur
        dist = np.sqrt((X - pos[i,0])**2 + (Y - pos[i,1])**2)
        rho_total += 2 * np.exp(-dist**2 / 1.5)
        
    # --- 2. AQF DISTORSİYON (W) VE MERCEKLENME ---
    delta_w = 0.8
    W = 1 + delta_w * rho_total # Distorsiyon alanı
    
    # Gradyan (Merceklenme yönü)
    grad_x, grad_y = np.gradient(np.log(W))
    lensing_force = np.sqrt(grad_x**2 + grad_y**2)
    
    return X, Y, W, lensing_force

# --- 3. GÖRSELLEŞTİRME ---
X, Y, W, lens_force = simulate_cluster_lensing()

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

ax[0].imshow(W, extent=[-10, 10, -10, 10], cmap='plasma', origin='lower')
ax[0].set_title("AQF Topolojik Distorsiyon (W)")

ax[1].imshow(lens_force, extent=[-10, 10, -10, 10], cmap='magma', origin='lower')
ax[1].set_title("Toplam Merceklenme Gücü (Gradyan)")

plt.show()