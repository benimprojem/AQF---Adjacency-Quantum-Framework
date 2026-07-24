# AQF Teknik Dokümantasyonu: Topolojik Kara Delik Yaşam Döngüsü, Vakum Sıkıştırma ve $c$ Sabitinin Mekanik Tanımı

**Doküman Kodu:** `AQF-THEORY-2026-M0-BH-005`

**Konu:** $M_1$ İzgarasında Maksimum İletim Sınırı Olarak $c$, Tampon Bölge Dekonstrüksiyonu, Sıkıştırılmış Çekirdek Büyümesi, Tersine Vakum Salınımı ve Gözlemsel Öngörüler

**Statü:** Resmi Kuramsal Notasyon ve Tam Sürüm Dokümantasyonu

---

## 1. Giriş ve Temel Tanım

AQF mimarisinde evren, alt katman olan $M_0$ mutlak kök zemini ile bunun üzerinde yükselen $M_1$ metrik ızgarasından ($M_1$ manifold) oluşur. Bu mimaride klasik fizikteki "tekillik" (sonsuz yoğunluk ve sıfır hacim) kavramı geçersizdir. Kara delikler, uzay-zamanı delen noktalar değil; $M_1$ ağının esnetildiği, maddenin temel vakuma indirgendiği ve merkezde sıkıştırıldığı dinamik topolojik reaktörlerdir.

---

## 2. $c$ Sabitinin AQF Tanımı: Vakumun Maksimum İletim Sınırı

Klasik fizikte $c$ sembolü "ışık hızı" olarak anılırken, AQF modelinde bu sabitin fiziksel kökeni ızgaranın mekanik sınırına dayanır:

* **Topolojik İletim (Faz Kayması) Hızı:** $M_1$ ızgarası, bir bilgi veya enerji fazını bir düğümden diğerine iletirken sonsuz hızla çalışamaz. Ağın kendi topolojik esnekliğinden kaynaklanan bir gecikme süresi vardır. Bu nedenle $c$, ışığa ait bir özellik değil; $M_1$ ızgarasının vakum yenileme ve iletim hızının mutlak üst sınırıdır ($v_{\text{vac(max)}}$).

$$c \equiv v_{\text{vac(max)}} = \frac{1}{\sqrt{\mu_{\text{top}} \epsilon_{\text{top}}}}$$

* **Fotonun Durumu:** Işık (fotonlar) kütlesiz, yani topolojik sürtünmesiz olduğu için ızgaranın izin verdiği bu en yüksek hız limitinde ($c$) hareket eder.

---

## 3. Olay Ufku Esnemesi (Max Fold) ve Tampon Bölge Dinamiği

Kara deliğin dış çeperi ve içi, zıt fiziksel mekanizmaların aynı anda çalıştığı iki ana bölgeye ayrılır:

### 3.1 Max Fold ve Ağ Esnemesi

Olay ufku ($R_s$), maddeyi yutan bir duvar değil, $M_1$ ağının kırma eşiğine kadar radyal yönde maksimum düzeyde esnetildiği topolojik bir zardır. Bu bölgedeki topolojik esneme gerilimi ($\mathcal{T}_{\mu\nu}^{\text{esneme}}$), ışığın bile dışarı çıkmasına izin vermez.

### 3.2 Tampon Bölge ve Kesintisiz Zaman Akışı ($T \neq 0$)

Olay ufku ($R_s$) ile merkez çekirdek ($R_{\text{core}}$) arasındaki boşluk aktif bir dekonstrüksiyon (öğütme) bölgesidir. Ufuktan içeri giren karmaşık kuantum bilgileri ve parçacıklar bu tampon bölgede katman katman soyulur ve temel vakuma indirgenir.

* Bu süreçte zaman genişlemesi aşırı derecede artsa da, $M_1$ ızgarası kopmadığı için zaman akışı asimptotik olarak yavaşlar ancak **asla sıfıra ulaşmaz**:

$$\lim_{r \to R_{\text{core}}} \left( \frac{dt_{\text{iç}}}{dt_{\text{dış}}} \right) \to \epsilon \quad (\text{burada } \epsilon > 0)$$

Zamanın sıfır olamaması ($T \neq 0$), içerideki mekanik sıkıştırma ve öğütme sürecinin kesintisiz olarak devam ettiğini garanti eder.

---

## 4. Sıkıştırılmış Topolojik Çekirdek ve Hacimsel Büyüme

Tampon bölgede temel vakuma dönüştürülen malzeme, merkeze doğru preslenerek katı bir sıkışma sınırı olan $\rho_{\text{max}}$ değerinde tutulur.

### 4.0 Çekirdeğin Volumetrik Büyümesi

Madde $M_0$ zeminine sızıp kaybolmadığı için, sisteme eklenen her yeni kütle ($M$), merkezdeki doygunluğa ulaşan çekirdeğin fiziksel hacmini ($V_{\text{core}}$) mecburen büyütür:

$$V_{\text{core}} = \int \frac{dM_{\text{giren}}}{\rho_{\text{max}}} \implies R_{\text{core}} \propto M^{1/3}$$

Buna karşın olay ufkunun yarıçapı ($R_s$) kütle ile doğrusal olarak büyür ($R_s \propto M$). Bu geometri, süpermasif kara deliklerin merkezinde devasa bir tampon bölge oluşmasını, mikro kara deliklerin ise dengesiz olmasını açıklar.

---


## 4.1. Çekirdek Büyümesi Formülleri (Core Growth Equations)

AQF modelinde, olay ufkunu geçerek temel vakuma indirgenen madde $M_0$'a sızmaz; merkezde $\rho_{\text{max}}$ (maksimum sıkışma yoğunluğu) sınırında sıkıştırılır. $\rho_{\text{max}}$ sabit bir evrensel üst sınır olduğu için, eklenen her kütle ($M$) doğrudan merkezin hacmini büyütür.

### 4.1.1 Hacimsel Büyüme Denklemi

Merkezdeki sıkıştırılmış çekirdeğin hacmi ($V_{\text{core}}$), toplam karadelik kütlesi $M$ ile doğrudan orantılıdır:

$$V_{\text{core}}(M) = \frac{M}{\rho_{\text{max}}}$$

### 4.1.2 Çekirdek Yarıçapının Kütleye Göre Büyüme Denklemi

Çekirdeğin küresel bir geometriyle büyüdüğünü varsayarsak ($V_{\text{core}} = \frac{4}{3}\pi R_{\text{core}}^3$), çekirdek yarıçapı ($R_{\text{core}}$) kütlenin küpkökü ile büyür:

$$\frac{4}{3}\pi R_{\text{core}}^3 = \frac{M}{\rho_{\text{max}}}$$

$$R_{\text{core}}(M) = \left( \frac{3}{4\pi \rho_{\text{max}}} \right)^{1/3} M^{1/3}$$

### 4.1.3 Çekirdek Büyüme Hızı (Türev)

Karadeliğe birim zamanda eklenen kütle akış hızı $\dot{M} = \frac{dM}{dt}$ iken, çekirdek yarıçapının zamana göre büyüme hızı şu formülle ifade edilir:

$$\frac{dR_{\text{core}}}{dt} = \frac{1}{4\pi \rho_{\text{max}} R_{\text{core}}^2} \cdot \dot{M}$$

---

## 4.2. Çekirdek / Ufuk Boyut Oran Formülü (Core-to-Horizon Ratio Formula)

Olay ufkumun yarıçapı ($R_s$) ile iç çekirdeğin yarıçapı ($R_{\text{core}}$) arasındaki oran, karadeliğin kütlesine ($M$) bağlı olarak değişkendir.

### 4.2.1 Olay Ufku Denklemi (Schwarzschild / AQF Ufuk Sınırı)

Olay ufkumun yarıçapı kütle ile doğrusal ($M^1$) büyür:

$$R_s(M) = \frac{2GM}{c^2}$$

*(Not: Burada $c$, vakumun maksimum iletim hızı sınırını temsil eder.)*

### 4.2.2 Boyut Oranı Denklemi ($\eta$)

Çekirdek yarıçapının ($R_{\text{core}}$) olay ufku yarıçapına ($R_s$) oranını ($\eta$) bulmak için iki denklemi birbirine oranlarız:

$$\eta(M) = \frac{R_{\text{core}}(M)}{R_s(M)} = \frac{\left( \frac{3}{4\pi \rho_{\text{max}}} \right)^{1/3} M^{1/3}}{\frac{2G}{c^2} M}$$

Sabit terimleri tek bir katsayıda birleştirip üsleri sadeleştirdiğimizde, **Nihai Oran Formülü** elde edilir:

$$\eta(M) = \left( \frac{3 c^6}{32 \pi G^3 \rho_{\text{max}}} \right)^{1/3} M^{-2/3}$$

---

## 4.3. Formülün Fiziksel Karşılığı ve Analizi

Bu oran formülü ($M^{-2/3}$ bağımlılığı), karadeliklerin ölçeklerine göre neden tamamen farklı davrandığını matematiksel olarak kanıtlar:

* **Mikro Karadelikler ($M \to 0$):** $M$ değeri küçüldükçe $M^{-2/3}$ terimi patlar; yani $\eta \to 1$'e yaklaşır. Çekirdek, olay ufkuna dayanır. Tampon bölge kalmaz, aşırı basınç ufk patlatır (Hawking ışıması/kararsızlık).
* **Süpermasif Karadelikler ($M \to \text{Çok Büyük}$):** $M$ büyüdükçe $M^{-2/3}$ terimi sıfıra yaklaşır ($\eta \to 0$). Ufuk devasa boyutlara ulaşırken, merkezdeki çekirdek oransal olarak çok küçük kalır. Arada devasa bir **Tampon Bölge** oluşur; bu yüzden süpermasif karadelikler son derece kararlıdır.

---



## 5. Kara Delik Ölümü: Tersine Vakum Dekompresyonu

Kara deliğe dışarıdan beslenme kesildiğinde ve rotasyonel dinamikler azaldığında dış ufuk gerilimi zayıflar.

* **Basınç Boşalması:** Olay ufkundaki gerilim eşiğin altına indiğinde, merkezde $\rho_{\text{max}}$ sınırında preslenmiş halde bekleyen devasa temel vakum kütlesi serbest kalır. Bu durum, $M_1$ ızgarasında dışa doğru yayılan şiddetli bir vakum basıncı dalgası ($\mathcal{P}_{\text{vac}}$) yaratır:

$$\mathcal{P}_{\text{vac}}(r, t) = -\nabla \Phi_{\text{core}} \cdot \exp\left(-\frac{r}{\lambda_{\text{salınım}}}\right)$$

---

## 6. Astronomik Gözlem Öngörüsü: Merkezi Vakum Boşlukları (Core Cavities)

Tersine vakum salınımı, galaktik ölçekte doğrudan gözlemlenebilir fiziksel bir iz bırakır.

* **Yıldızlararası Süpürme:** Merkezden dışarı doğru yayılan bu ani dekompresyon dalgası, merkeze yakın olan yıldızları ve gaz bulutlarını dışarıya doğru iter.
* **Gözlem Kriteri:** Merkezinde bir zamanlar dev kütleli kara delik barındırmış ancak ömrünü tamamlamış (ölmüş) galaksilerin merkezinde ($\lim r \to 0$), yıldız yoğunluğunun aniden düştüğü oyulmuş **Yıldızsız Merkez Boşlukları (Core Depleted / Central Cavities)** tespit edilmelidir:

$$\lim_{r \to 0} \frac{\partial \rho_{\text{yıldız}}}{\partial t} < 0$$

Bu boşluklar, AQF modelinin galaktik ölçekteki en net ve doğrulanabilir doğrudan imzasını oluşturur.

