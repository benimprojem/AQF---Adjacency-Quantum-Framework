# AQF Teknik Dokümantasyonu: $M_0$ Faz Geçişi ve Dinamik Vakum Enjeksiyon Mekanizması

**Doküman Kodu:** `AQF-THEORY-2026-M0-PHASE-002`

**Konu:** Metriksiz Kök Katmandan ($M_0$) Topolojik Izgaraya ($M_1$) Madde/Vakum Akışı, Faz Geçiş Potansiyeli ve Zaman Bağımlı Durum Denklemi Formülasyonu

**Statü:** Resmi Kuramsal Notasyon

---

## 1. Giriş ve Faz Geçişi Mantığı

AQF kozmolojisinde, evrenin genişlemesi ve evrimi $M_0$ katmanındaki faz durumuna bağımlıdır. $M_0$ katmanı, iki temel faz rejimine sahiptir:

1. **Erken Dönem Rejimi ($t < t_{\text{kritik}}$):** Hem kütle/madde enjeksiyonu ($\Gamma_m > 0$) hem de saf vakum üretimi ($\Gamma_\Lambda > 0$) aktiftir.
2. **Geç Dönem Rejimi ($t \ge t_{\text{kritik}}$ - Doygunluk Fazı):** Madde üretimi durur ($\Gamma_m = 0$), sadece metrik genleşmesini yönlendiren saf Planck hacmi/vakum enjeksiyonu ($\Gamma_\Lambda = \text{sabit}$) devam eder.

Bu dönüşüm, $M_0$ katmanının **Topolojik Sipariş Parametresi (Order Parameter)** $\Phi(t)$ ile tanımlanan sürekli bir faz geçişidir.

---

## 2. $M_0$ Faz Alanı ve Potansiyel Fonksiyonu

$M_0$ katmanındaki faz durumu, simetri kırılmasını yöneten bir Landau-Ginzburg serisi şeklinde $\Phi(t)$ skaler alanı ile ifade edilir.

### 2.1 Faz Potansiyeli $\mathcal{V}(\Phi)$

$$\mathcal{V}(\Phi) = \mathcal{V}_0 + \lambda_2 \Big( \Phi(t) - \Phi_c \Big)^2 + \lambda_4 \Big( \Phi(t) - \Phi_c \Big)^4$$

Burada:

* $\Phi(t)$, $M_0$ katmanının anlık doygunluk/faz değeridir.
* $\Phi_c$, faz geçişinin tamamlandığı Kritik Doygunluk Eşiğidir (günümüzden yaklaşık 5.0 milyar yıl önceki denge noktasına denk gelir).
* $\lambda_2, \lambda_4$, $M_0 \to M_1$ topolojik aktarım katsayılarıdır.

---

## 3. Dinamik Vakum ve Madde Enjeksiyon Hızları

$M_0$ katmanından $M_1$ ızgarasına birim zamanda aktarılan madde ve hacim miktarı, faz alanının türevine ($\dot{\Phi}$) kilitlidir.

### 3.1 Kütle Enjeksiyon Hızı ($\Gamma_m$)

$$\Gamma_m(t) = \Gamma_0 \cdot \Theta\big(\Phi_c - \Phi(t)\big) \cdot \exp\left(-\frac{t}{\tau_{\text{doygunluk}}}\right)$$

Burada:

* $\Theta(x)$, Heaviside basamak fonksiyonudur ($x \ge 0$ için $1$, $x < 0$ için $0$).
* $\tau_{\text{doygunluk}}$, $M_0$ madde üretim alanının sönümlenme zaman sabitidir.
* $\Phi(t) \ge \Phi_c$ olduğunda $\Theta = 0$ olur ve madde üretimi tam olarak durur ($\Gamma_m = 0$).

### 3.2 Vakum/Planck Hacmi Enjeksiyon Hızı ($\Gamma_\Lambda$)

$M_0$ katmanının $M_1$ manifolduna sürekli eklediği saf vakum hacmi akısı:

$$\Gamma_\Lambda(t) = \Lambda_0 \cdot \left[ 1 + \tanh\left( \frac{t - t_{\text{faz}}}{\Delta t_{\text{geçiş}}} \right) \right]$$

Burada:

* $\Lambda_0$, doygunluk sonrası sabit vakum üretim genliğidir.
* $t_{\text{faz}}$, faz geçişinin tepe noktasıdır (Kozmik Denge Noktası).
* $\Delta t_{\text{geçiş}}$, $M_0$ faz geçişinin genişleme aralığıdır.

---

## 4. Zaman Bağımlı Durum Denklemi $w_{M0}(z)$

$M_0$ faz geçişi nedeniyle, evrenin toplam enerji-stres tensörüne etki eden efektif durum denklemi parametresi $w(z)$ sabit bir $-1$ değildir. Kırmızıya kaymaya ($z$) bağlı olarak şu şekilde türetilir:

$$w_{M0}(z) = w_0 + w_a \left( \frac{z}{1+z} \right) \cdot \left[ 1 + \Phi(z) \right]$$

* **Erken Evren ($z \gg 1$):** Madde üretimi aktif olduğu için $w_{M0} \to 0$ (Madde dominansı / $M_0$ madde rejiminde).
* **Geç Evren ($z \to 0$):** Madde üretimi kapalı, saf vakum aktiftir:

$$\lim_{z \to -1} w_{M0}(z) = -1$$

Bu dinamik yapı, Standart $\Lambda\text{CDM}$ modelinde tespit edilen DESI 2024 $w(z)$ sapmalarını doğrudan açıklar.

---

## 5. Ölçek Faktörü Evrim Denklemi

$M_0$ enjeksiyon terimleri eklendiğinde Friedmann-AQF modifiye genleşme denklemi şu hali alır:

$$\left( \frac{\dot{a}}{a} \right)^2 = \frac{8\pi G}{3} \left[ \rho_m^{(0)} a^{-3} + \int_0^t \Gamma_m(t') a^{-3}(t') \, dt' \right] + \frac{c^2}{3} \int_0^t \Gamma_\Lambda(t') \, dt'$$

Denklemin sağ tarafındaki integraller, $M_0$ katmanının $M_1$ ızgarasına geçmişten bugüne birikimli (cumulative) olarak eklediği toplam kütle ve vakum bütçesini ifade eder.

---

## 6. Özet Notu

> **Kuramsal Sonuç:** $M_0$ faz geçişi, evrenin genişlemesini sabit bir kozmolojik sabit ($\Lambda$) ile değil, $M_0 \to M_1$ katmanları arasındaki sürekli ve doygunluğa ulaşan bir topolojik aktarım potansiyeli ($\mathcal{V}(\Phi)$) ile açıklar. Erken evrendeki hızlı galaksi oluşumları ($\Gamma_m > 0$) ve geç evrendeki $H_0$ gerilimi, bu faz geçişi denklemlerinin doğal sınır koşullarıdır.
