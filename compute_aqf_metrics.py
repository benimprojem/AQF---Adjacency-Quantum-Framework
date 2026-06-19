import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. AYARLAR VE PARAMETRELER ---
GRID_SIZE = 50  # Uzay alanı çözünürlüğü
DELTA_W = 0.5   # Topolojik duyarlılık katsayısı
np.random.seed(42)

def generate_cluster_data(size):
    """Galaktik yoğunluk dağılımını (rho_A) simüle eder."""
    x, y = np.meshgrid(np.linspace(-10, 10, size), np.linspace(-10, 10, size))
    # Küme merkezinde yoğunluk (Gaussian)
    rho_a = 5 * np.exp(-(x**2 + y**2) / 15) + 0.1 * np.random.rand(size, size)
    return rho_a

# --- 2. AQF FORMÜLASYONU ---
def compute_aqf_metrics(rho_a, delta_w):
    """
    AQF denklemlerini uygular:
    W(x) = 1 + delta_w * rho_A
    B(x) = |(W(x))^2 - 1| (Buruşukluk İndeksi)
    """
    W = 1 + delta_w * rho_a
    B = np.abs(W**2 - 1)
    # Zaman genişlemesi katsayısı (g00'ın tersi)
    time_dilation = 1 / (W**2)
    return W, B, time_dilation

# --- 3. ANALİZ VE HESAPLAMA ---
rho_a = generate_cluster_data(GRID_SIZE)
W, B, time_dilation = compute_aqf_metrics(rho_a, DELTA_W)

# --- 4. GÖRSELLEŞTİRME (UZAYIN BURUŞUKLUK HARİTASI) ---
fig = plt.figure(figsize=(12, 6))

# Sol: Ağ Yoğunluğu
ax1 = fig.add_subplot(121, projection='3d')
X, Y = np.meshgrid(np.arange(GRID_SIZE), np.arange(GRID_SIZE))
surf1 = ax1.plot_surface(X, Y, rho_a, cmap='viridis', alpha=0.8)
ax1.set_title("Ağ Yoğunluğu (rho_A)")

# Sağ: AQF Buruşukluk Haritası (B(x))
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(X, Y, B, cmap='inferno', alpha=0.8)
ax2.set_title("Uzay Buruşukluğu (B(x))")

plt.tight_layout()
plt.show()

# --- 5. RAPORLAMA ---
print(f"AQF Analizi Tamamlandı.")
print(f"Maksimum Buruşukluk İndeksi (B_max): {np.max(B):.4f}")
print(f"Minimum Zaman Akış Katsayısı (g00_min): {np.min(time_dilation):.4f}")