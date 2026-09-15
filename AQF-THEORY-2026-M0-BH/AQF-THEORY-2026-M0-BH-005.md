# AQF Teknik Dokümantasyonu: Topolojik Kara Delik Yaşam Döngüsü, Vakum Sıkıştırma ve (c) Sabitinin Mekanik Tanımı

**Doküman Kodu:** `AQF-THEORY-2026-M0-BH-005`
**Konu:** (M_1) Izgarasında Maksimum İletim Sınırı Olarak (c), Tampon Bölge Dekonstrüksiyonu, Sıkıştırılmış Çekirdek Büyümesi, Tersine Vakum Salınımı ve Gözlemsel Öngörüler
**Statü:** Resmi Kuramsal Notasyon

---

## 1. Giriş ve Temel Tanım

AQF mimarisinde evren, alt katman olan (M_0) mutlak kök zemini ile bunun üzerinde yükselen (M_1) metrik ızgarasından ((M_1) manifold) oluşur. Bu mimaride klasik fizikteki “tekillik” kavramı —yani sonsuz yoğunluk ve sıfır hacim— geçersizdir. Kara delikler, uzay-zamanı delen noktalar değil; (M_1) ağının esnetildiği, maddenin temel vakuma indirgenerek merkezde sıkıştırıldığı dinamik topolojik reaktörlerdir.

---

## 2. (c) Sabitinin AQF Tanımı: Vakumun Maksimum İletim Sınırı

Klasik fizikte (c) sembolü “ışık hızı” olarak anılırken, AQF modelinde bu sabitin fiziksel kökeni ızgaranın mekanik sınırına dayanır.

* **Topolojik iletim (faz kayması) hızı:**
  (M_1) ızgarası, bir bilgi veya enerji fazını bir düğümden diğerine iletirken sonsuz hızla çalışamaz. Ağın kendi topolojik esnekliğinden kaynaklanan bir gecikme süresi vardır. Bu nedenle (c), ışığa ait bir özellik değil; (M_1) ızgarasının vakum yenileme ve iletim hızının mutlak üst sınırıdır:

[
c \equiv v_{\text{vac(max)}} = \frac{1}{\sqrt{\mu_{\text{top}}\epsilon_{\text{top}}}}
]

* **Fotonun durumu:**
  Işık (fotonlar) kütlesiz, yani topolojik sürtünmesiz olduğu için ızgaranın izin verdiği bu en yüksek hız limitinde ((c)) hareket eder.

---

## 3. Olay Ufku Esnemesi (Max Fold) ve Tampon Bölge Dinamiği

Kara deliğin dış çeperi ve içi, zıt fiziksel mekanizmaların aynı anda çalıştığı iki ana bölgeye ayrılır.

### 3.1 Max Fold ve ağ esnemesi

Olay ufku ((R_s)), maddeyi yutan bir duvar değil, (M_1) ağının kırma eşiğine kadar radyal yönde maksimum düzeyde esnetildiği topolojik bir zardır. Bu bölgedeki topolojik esneme gerilimi ((\mathcal{T}_{\mu\nu}^{\text{esneme}})), ışığın bile dışarı çıkmasına izin vermez.

### 3.2 Tampon bölge ve kesintisiz zaman akışı ((T \neq 0))

Olay ufku ((R_s)) ile merkez çekirdek ((R_{\text{core}})) arasındaki boşluk aktif bir dekonstrüksiyon bölgesidir. Ufuktan içeri giren karmaşık kuantum bilgileri ve parçacıklar bu tampon bölgede katman katman soyulur ve temel vakuma indirgenir.

Bu süreçte zaman genişlemesi aşırı derecede artsa da, (M_1) ızgarası kopmadığı için zaman akışı asimptotik olarak yavaşlar ancak **asla sıfıra ulaşmaz**:

[
\lim_{r \to R_{\text{core}}}\left(\frac{dt_{\text{iç}}}{dt_{\text{dış}}}\right)\to \epsilon \quad (\text{burada } \epsilon>0)
]

Zamanın sıfır olamaması ((T \neq 0)), içerideki mekanik sıkıştırma ve öğütme sürecinin kesintisiz olarak devam ettiğini garanti eder.

---

## 4. Sıkıştırılmış Topolojik Çekirdek ve Hacimsel Büyüme

Tampon bölgede temel vakuma dönüştürülen malzeme, merkeze doğru preslenerek katı bir sıkışma sınırı olan (\rho_{\text{max}}) değerinde tutulur.

### 4.0 Çekirdeğin volumetrik büyümesi

Madde (M_0) zeminine sızıp kaybolmadığı için, sisteme eklenen her yeni kütle ((M)), merkezde doygunluğa ulaşan çekirdeğin fiziksel hacmini ((V_{\text{core}})) mecburen büyütür:

[
V_{\text{core}} = \int \frac{dM_{\text{giren}}}{\rho_{\text{max}}}
\quad \Rightarrow \quad
R_{\text{core}} \propto M^{1/3}
]

Buna karşın olay ufkunun yarıçapı ((R_s)) kütle ile doğrusal olarak büyür ((R_s \propto M)). Bu geometri, süpermasif kara deliklerin merkezinde devasa bir tampon bölge oluşmasını, mikro kara deliklerin ise dengesiz olmasını açıklar.

---

## 4.1 Çekirdek büyümesi formülleri

AQF modelinde, olay ufkunu geçerek temel vakuma indirgenen madde (M_0)’a sızmaz; merkezde (\rho_{\text{max}}) sınırında sıkıştırılır. (\rho_{\text{max}}) sabit bir evrensel üst sınır olduğu için, eklenen her kütle ((M)) doğrudan merkezdeki hacmi büyütür.

### 4.1.1 Hacimsel büyüme denklemi

Merkezdeki sıkıştırılmış çekirdeğin hacmi ((V_{\text{core}})), toplam kara delik kütlesi (M) ile doğrudan orantılıdır:

[
V_{\text{core}}(M)=\frac{M}{\rho_{\text{max}}}
]

### 4.1.2 Çekirdek yarıçapının kütleye göre büyüme denklemi

Çekirdeğin küresel bir geometriyle büyüdüğünü varsayarsak ((V_{\text{core}}=\frac{4}{3}\pi R_{\text{core}}^3)), çekirdek yarıçapı kütlenin küpkökü ile büyür:

[
\frac{4}{3}\pi R_{\text{core}}^3=\frac{M}{\rho_{\text{max}}}
]

[
R_{\text{core}}(M)=\left(\frac{3}{4\pi\rho_{\text{max}}}\right)^{1/3}M^{1/3}
]

### 4.1.3 Çekirdek büyüme hızı

Karadeliğe birim zamanda eklenen kütle akış hızı (\dot{M}=\frac{dM}{dt}) iken, çekirdek yarıçapının zamana göre büyüme hızı şu formülle ifade edilir:

[
\frac{dR_{\text{core}}}{dt}
===========================

\frac{1}{4\pi\rho_{\text{max}}R_{\text{core}}^2}\cdot\dot{M}
]

---

## 4.2 Çekirdek / ufuk boyut oranı

Olay ufku yarıçapı ((R_s)) ile iç çekirdeğin yarıçapı ((R_{\text{core}})) arasındaki oran, karadeliğin kütlesine ((M)) bağlı olarak değişkendir.

### 4.2.1 Olay ufku denklemi (Schwarzschild / AQF ufuk sınırı)

Olay ufkunun yarıçapı kütle ile doğrusal büyür:

[
R_s(M)=\frac{2GM}{c^2}
]

Burada (c), AQF tanımında vakumun maksimum iletim hızı sınırını temsil eder. Bu ifade, kullanılan ufuk yaklaşımının **Schwarzschild sınırı** için yazıldığını gösterir. Dönme ve yük etkileri hesaba katıldığında ufuk yapısı ek terimlerle genişletilmelidir.

### 4.2.2 Boyut oranı denklemi ((\eta))

Çekirdek yarıçapının ((R_{\text{core}})) olay ufku yarıçapına ((R_s)) oranını ((\eta)) bulmak için iki denklemi oranlarız:

[
\eta(M)=\frac{R_{\text{core}}(M)}{R_s(M)}
=========================================

\frac{\left(\frac{3}{4\pi\rho_{\text{max}}}\right)^{1/3}M^{1/3}}{\frac{2G}{c^2}M}
]

Sabit terimleri tek bir katsayıda birleştirip üsleri sadeleştirdiğimizde nihai oran formülü elde edilir:

[
\eta(M)=\left(\frac{3c^6}{32\pi G^3\rho_{\text{max}}}\right)^{1/3}M^{-2/3}
]

Burada (c), vakumun maksimum iletim hızı sınırını temsil eder ve şu şekilde tanımlanır:

[
c \equiv v_{\text{vac(max)}} = \frac{1}{\sqrt{\mu_{\text{top}}\epsilon_{\text{top}}}}
]

### 4.2.3 Boyut oranının fiziksel karşılığı

Bu oran formülü, (M^{-2/3}) bağımlılığı sayesinde kara deliklerin ölçeklerine göre neden farklı davrandığını açıklar:

* **Küçük kütleli kara delikler ((M \to 0))**:
  (M) küçüldükçe (M^{-2/3}) terimi büyür, dolayısıyla (\eta) hızla artar. Bu, çekirdeğin ufka göre göreli etkisinin büyüdüğü ve tampon bölgenin giderek kaybolduğu bir rejime karşılık gelir. Bu sınırda modelin kararlılığı zayıflar ve ufuk yapısı kırılgan hale gelir.

* **Büyük kütleli kara delikler ((M \to \text{çok büyük}))**:
  (M) arttıkça (M^{-2/3}) terimi sıfıra yaklaşır, yani (\eta \to 0). Bu durumda ufuk hacimsel olarak çok hızlı büyürken çekirdek oransal olarak küçük kalır. Sonuç olarak arada geniş bir **tampon bölge** oluşur ve sistem daha kararlı bir geometriye yaklaşır.

Bu sonuç, süpermasif kara deliklerde merkez çevresindeki yapı ile mikro ölçekli kara deliklerdeki davranışın neden aynı olmadığını doğrudan gösterir.

---

## 5. Kara Delik Ölümü: Tersine Vakum Dekompresyonu

Kara delik ölümü, sisteme dışarıdan madde beslenmesinin kesilmesi ve dönüş hareketinin zayıflamasıyla tetiklenir. Beslenme ve dönme dinamikleri kritik eşiğin altına indiğinde, tampon bölgede (\rho_{\text{max}}) sınırında sıkıştırılmış halde tutulan temel vakum artık kararlı biçimde muhafaza edilemez. Bu durumda vakum, merkezde sarılmış halde bulunan topolojik çekirdekten çözülerek geri salınır.

Bu geri salım, olay ufkundan içeriye doğru çöken bir hareket değil; olay ufkuna komşu bölgede gerilim boşalması oluşturan, dışa doğru gevşeyen bir yeniden açılma sürecidir. Böylece (M_1) ızgarasında daha önce sıkışmış olan bölge çözülür ve onun yerini yeni bir vakum boşluğu alır. Bu nedenle kara delik ölümü, kaotik bir dağılma yerine, merkezden itibaren açılan dairesel veya eliptik simetrili bir boşluk geometrisi üretir.

Olay ufkunu geçen her madde, tampon bölgede katman katman soyularak en temel vakuma dönüştürülür. Bu vakum, merkezde sarılarak topolojik çekirdeği oluşturur. Çekirdek, vakumun pasif depolanma hali değil; sıkıştırılmış ve örgülenmiş vakumun geometrik olarak kararlı bir topolojik bütünleşme formudur. Dolayısıyla kara delik iç yapısı, boşlukla dolu bir yokluk değil, vakumun yoğunlaştırılmış topolojik düzenidir.

### 5.1 Ölüm Tetikleyici ve Geometrik İmza

Bu mekanizmada tetikleyici, doğrudan iki koşulun birlikte zayıflamasıdır:

[
\dot{M}*{\text{beslenme}} \to 0
\qquad \text{ve} \qquad
\Omega*{\text{dönme}} \to 0
]

Bu iki dinamik çöktüğünde, tampon bölgedeki sıkıştırılmış vakum geri bırakılır. Geri bırakılan vakum, merkezden dışarıya doğru yeni bir boş alan açar ve böylece gözlemsel olarak daha düzenli, daha homojen ve daha simetrik bir merkezi oyulma profili oluşur. Bu nedenle AQF modelinde kara delik ölümü, rastgele bir savrulma değil, merkezden başlayan kontrollü bir vakum boşalması olarak tanımlanır.

### 5.2 Gözlemsel Sonuç

Bu süreç sonucunda galaksi merkezinde yıldız yoğunluğu, gaz dağılımı ve parlaklık profili simetrik bir şekilde azalmalıdır. Beklenen imza, yönlü bir fırlatma izi değil; dairesel sınırları belirgin, merkezi boşaltılmış ve homojen gevşeme gösteren bir çekirdek boşluğudur. Bu yapı, tersine vakum dekompresyonunun doğrudan geometrik karşılığıdır.

---

## 6. Astronomik gözlem öngörüsü: merkezi vakum boşlukları (\textit{Core Cavities})

Tersine vakum salınımı, galaktik ölçekte doğrudan gözlemlenebilir bir iz bırakmalıdır.

* **Yıldızlararası süpürme:**
  Merkezden dışarı doğru yayılan dekompresyon dalgası, merkeze yakın yıldızları ve gaz bulutlarını dışarı iter.

* **Gözlem kriteri:**
  Merkezinde bir zamanlar dev kütleli kara delik barındırmış, ancak aktif beslenme evresi sona ermiş galaksilerin çekirdek bölgelerinde yıldız yoğunluğunun belirgin biçimde azaldığı oyulmuş boşluklar beklenmelidir:

[
\lim_{r \to 0}\frac{\partial \rho_{\text{yıldız}}}{\partial t}<0
]

Bu boşluklar, AQF modelinin galaktik ölçekteki en ayırt edici doğrudan imzasını oluşturur.

---

## 6.1. Sapan etkisi ile AQF vakum salınımının ayrımı

Klasik astrofizikteki sapan etkisi (\textit{gravitational slingshot}), dinamik ve iki cisimli bir etkileşime dayanır. İki kara deliğin birleşmesi veya yakın etkileşimi sırasında yörüngeler kaotik hale gelir; bu nedenle çevreye savrulan yıldızlar düzensiz, yönlü ve asimetrik izler bırakır.

AQF modelinin öngördüğü tersine vakum salınımı ise farklı bir geometrik karakter taşır.

### 6.1.1 İzotropik vakum dekompresyonu

Merkezdeki sıkıştırılmış temel vakum serbest kaldığında, bu olay yönlü bir fırlatma değil, (M_1) metrik ızgarasının her yöne eşit biçimde gevşemesiyle oluşan **izotropik basınç dalgası**dır.

### 6.1.2 Gözlemsel imza farkı

Bu nedenle iki mekanizma gözlemsel olarak ayrıştırılabilir:

* **Sapan etkisi:** düzensiz, asimetrik, kenarları kırık ve yönlü savrulma izleri.
* **AQF vakum salınımı:** daha düzgün sınırlı, dairesel ya da eliptik geometriyle uyumlu, homojen ve simetrik bir merkezi boşluk.

### 6.1.3 Doğrulanabilir gözlem kriteri

Yüksek çözünürlüklü gözlemlerle galaksi merkezlerindeki yıldız yoğunluğu profilleri incelendiğinde bu iki mekanizma ayrı ayrı tanınabilir. Eğer boşluk kaotik bir savrulma izi taşıyorsa sapan etkisine işaret eder; eğer boşluk düzenli, simetrik ve oyulmuş bir profil gösteriyorsa bu, AQF’nin merkezî vakum dekompresyonuna karşılık gelir.
