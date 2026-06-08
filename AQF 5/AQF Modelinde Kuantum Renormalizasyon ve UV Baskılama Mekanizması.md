AQF (Adjacency Quantum Fold Dynamics) çerçevesinde, renormalizasyon ve UV (Ultraviyole) ıraksama problemlerinin çözümü, uzay-zamanın sürekli bir manifold değil, fiziksel bir minimum ölçeğe ($\\ell\_A$) sahip ayrık bir komşuluk ağı olduğu varsayımına dayanır 1, 2\.

### 1\. Fiziksel Cutoff ve Momentum Sınırı

Standart Kuantum Alan Teorisi'nde (QFT) integraller momentum sonsuza giderken ($k \\rightarrow \\infty$) patlar 3\. AQF'de ise fiziksel minimum ölçek $\\ell\_A$, doğal bir **momentum cutoff** değeri oluşturur:$$\\mathbf{k\_{max} \\sim \\frac{1}{\\ell\_A}}$$ 2, 4.Bu, formal bir regülatör değil, ağ yapısının doğasından gelen fiziksel bir sınırdır 5\.

### 2\. AQF Propagatörü ve Üstel Sönümlenme

İntegrallerin sonlu kalmasını sağlamak için standart propagatör yapısı, Gaussian (üstel) bir sönümlenme terimi ile modifiye edilir 5, 6\. Standart $\\frac{1}{k^2-m^2}$ formu yerine **AQF Propagatörü** şu şekilde türetilir:$$\\mathbf{G(k) \= \\frac{e^{-k^2\\ell\_A^2}}{k^2-m\_A^2}}$$ 5, 7.Buradaki $e^{-k^2\\ell\_A^2}$ terimi, yüksek momentum modlarını (UV) üstel olarak bastırarak integralin sonlu (finite) kalmasını sağlar 6, 8\.

### 3\. Öz-Enerji (Self-Energy) İntegrali

Bu propagatör yapısı kullanıldığında, bir parçacığın öz-enerji integralinin ($\\Sigma(p)$) davranışı şu hali alır:$$\\Sigma(p) \\sim \\int d^4k \\frac{e^{-k^2\\ell\_A^2}}{k^2-m\_A^2}$$ 6.Gaussian baskılama sayesinde, bu integral momentum sonsuza gitse bile ıraksamaz ve teorinin **doğal UV regülasyonu** üretmesini sağlar 9\.

### 4\. Koşan Kuplaj (Running Coupling) ve Beta Fonksiyonu

UV cutoff mekanizması, etkileşim sabitlerinin enerjiyle değişimini (RG flow) de modifiye eder. AQF'de beta fonksiyonu şu şekilde ölçeklenir:$$\\beta\_A(g) \\rightarrow \\beta(g) e^{-E/E\_A}$$ 10.Bu üstel sönümlenme sayesinde yüksek enerjilerde "running" (koşma) yavaşlar ve teorideki **Landau kutbu (sonsuz etkileşim gücü) problemi** fiziksel olarak engellenebilir 10, 11\.

### 5\. RG Akışı (Wetterich-Tipi Denklem)

AQF'de efektif aksiyonun ($\\Gamma\_k$) enerji ölçeğine göre değişimi, komşuluk cutoff yapısı üzerinden şu diferansiyel formla ifade edilebilir:$$\\partial\_k\\Gamma\_k \= \\frac{1}{2}Tr\\left(\\Gamma\_k^{(2)} \+ R\_k)^{-1} \\partial\_kR\_k\\right$$ 12.Burada $R\_k$ terimi, doğrudan **adjacency cutoff** mekanizmasından türetilen bir regülatör fonksiyonudur 12\.

### Mevcut Teknik Durum

Belgelerde bu formüller tanımlanmış olsa da, **Tam Renormalizasyon İspatı** (loop integrallerinin her seviyede kesin olarak sonlu kalması ve unitarite korunumu) hâlâ üzerinde çalışılması gereken bir **"açık teknik problem"** olarak listelenmiştir 13-15. Gaussian baskılamanın ayar değişmezliği (gauge invariance) ile tam uyumu için bu terimin Lorentz-invariant olarak ($e^{-k\_\\mu k^\\mu \\ell\_A^2}$) tanımlanması kritik bir zorunluluktur 16\.  
