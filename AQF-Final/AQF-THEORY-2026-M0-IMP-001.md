# AQF Teknik Dokümantasyonu: M0–M1 Arayüz Empedansı ve Kuantum Tünelleme Mekanizması

**Doküman Kodu:** `AQF-THEORY-2026-M0-IMP-001`

**Konu:** Metriksiz Kök Katman ($M_0$) ile Topolojik Izgara ($M_1$) Arasındaki Sınır Geçiş Empedansı ve Kuantum Tünelleme Formülasyonu

**Statü:** Resmi Kuramsal Notasyon

---

## 1. Giriş ve Topolojik Tanımlar

AQF mimarisinde, Standart Kuantum Mekaniği'ndeki potansiyel bariyerlerini aşma (kuantum tünelleme) olayı, parçacığın $M_1$ metrik uzayında fiziksel bir mesafe katetmesi olarak değil; metriksiz $M_0$ kök zemini üzerinden gerçekleşen bir topolojik baypas olarak tanımlanır.

### Metrik Özellikleri:

* **$M_1$ Katmanı (Metrik Manifold):** $g_{\mu\nu} \neq 0$
Masaüstü uzay-zaman. Mesafe ($\Delta s$) ve öz-zaman ($\Delta \tau$) tanımlıdır.
* **$M_0$ Katmanı (Kök Zemin):** $g_{\mu\nu} = 0$
Metriksiz alt katman. Uzaysal mesafe ($\Delta s = 0$) ve zamansal süreç ($\Delta \tau = 0$) tanımsızdır (sıfırdır).

---

## 2. $M_0$–$M_1$ Arayüz Sınır Empedansı (Boundary Impedance)

$M_1$ uzay-zamanında tanımlı $L$ uzunluğundaki bir potansiyel bariyeri, $M_0$ içindeki bir mesafe değildir. $L$, parçacığın $M_1$ katmanındaki faz tutarlılığını korumak zorunda olduğu **Arayüz Sınır Boyudur**.

### 2.1 Yerel Sınır Empedans Yoğunluğu ($z_{M_0}$)

$M_1$ üzerindeki bir $x$ noktasında, parçacığın enerjisi ($E$) ile $M_1$ potansiyeli ($V(x)$) arasındaki uyumsuzluktan doğan yerel empedans yoğunluğu $z_{M_0}(x)$ şu şekilde tanımlanır:

$$z_{M_0}(x) \equiv \alpha \cdot \sqrt{\frac{2m}{\hbar^2} \Big( V(x) - E \Big)}$$

Burada:

* $\alpha \approx 1$, $M_1$ ızgarası ile $M_0$ zemini arasındaki dimensionless (boyutsuz) topolojik bağlaşım katsayısıdır.
* $m$, $M_1$ katmanına projekte olmuş düğümün efektif kütlesidir.
* $V(x) > E$ şartı, $M_1$ uzayında klasik olarak yasaklanmış potansiyel bölgesini ifade eder.

### 2.2 Toplam Sınır Empedansı ($Z_{\text{toplam}}$)

Parçacığın $M_1$ üzerindeki $L$ genişliğindeki bariyer boyunca $M_0$ kanalına tutunma direncini belirleyen toplam sınır empedansı, yerel empedans yoğunluğunun sınır integralidir:

$$Z_{\text{toplam}}(L) = \int_{0}^{L} z_{M_0}(x) \, dx$$

Sabit bir potansiyel engeli ($V(x) = V_0 = \text{sabit}$) durumunda integral doğrusal hale gelir:

$$Z_{\text{toplam}}(L) = z_{M_0} \cdot L = \sqrt{\frac{2m(V_0 - E)}{\hbar^2}} \cdot L$$

---

## 3. Tünelleme Olasılığı ve Faz Sönümlenmesi

$M_1$ manifoldunun $A$ noktasından ($x=0$) $M_0$ zeminine inip, $\Delta s = 0$ mesafeyle $B$ noktasına ($x=L$) projekte olan fazın, sönümlenmeden karşıya geçme olasılığı $P(L)$, toplam sınır empedansının eksponansiyel bastırması olarak hesaplanır:

$$P(L) = \exp\left( -2 \cdot Z_{\text{toplam}}(L) \right) = \exp\left( -2 \int_{0}^{L} z_{M_0}(x) \, dx \right)$$

Homojen bariyer ($V_0$) koşulunda bu ifade standart WKB formülasyonuna tam olarak denklenir:

$$P(L) = e^{-2 \cdot k_{M_0} \cdot L}$$

Burada $k_{M_0}$, $M_0$ sönüm katsayısıdır:

$$k_{M_0} = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$$

---

## 4. Uzay-Zaman Metrik Bütçesi ($1 + 0 + 1$ İlkesi)

Kuantum tünelleme esnasında $M_1$ dış gözlemcisine göre ışık hızından hızlı ($v > c$) veya anlık görünen geçiş süreci, $M_0$ topolojik metrik bütçesinde $c$ lokal hız sınırını ihlal etmez.

$$\Delta s_{\text{toplam}} = \Delta s_{M_1\to M_0} + \Delta s_{M_0} + \Delta s_{M_0\to M_1}$$

$$\Delta s_{\text{toplam}} = 1\,\ell_P + 0 + 1\,\ell_P = 2\,\ell_P$$

$$\Delta t_{\text{toplam}} = 1\,t_P + 0 + 1\,t_P = 2\,t_P$$

Yerel hız:

$$v_{\text{lokal}} = \frac{\Delta s_{\text{toplam}}}{\Delta t_{\text{toplam}}} = \frac{2\,\ell_P}{2\,t_P} = c$$

---

## 5. Özet Notu

> **Kuramsal Sonuç:** $M_0$ katmanında uzaysal veya zamansal bir mesafe yoktur ($\Delta s_{M_0} = 0, \Delta t_{M_0} = 0$). Bariyer kalınlığı $L$ arttıkça olasılığın ($P$) düşmesi, $M_0$ içinde bir yol katedilmesinden değil; parçacığın $M_1$ bariyeri boyunca $M_0$ kanalında kalmak zorunda olduğu arayüz yüzeyinin toplam empedansının ($Z_{\text{toplam}}$) artmasından kaynaklanır.
