AQF (Adjacency Quantum Fold Dynamics) çerçevesinde, gravitasyonel sapmayı (ışık bükülmesini) modellemek için uzay-zamanı bir manifold olarak değil, bir **yinelemeli komşuluk ağı (recursive adjacency network)** olarak ele alırız 1-3. Gravitasyonel sapma, bu ağ üzerindeki "minimum taşıma maliyeti" optimizasyonunun bir sonucudur 4-6.  
Bu modelleme süreci şu adımlarla gerçekleşir:

### 1\. Eğriliğin Kaynağı: Adjacency Deformasyonu

AQF'de kütleçekimi, kütleli cisimlerin komşuluk ağında yarattığı **"taşıma stresi" (transport stress)** sonucudur 4, 7, 8\. Bu stres, ağın homojenliğini bozarak yerel bir **Adjacency Curvature ($C\_A$)** oluşturur:$$\\mathcal{L}*A \= \\beta\_A \\sum (\\nabla A*{ij})^2$$Buradaki $\\nabla A$ terimi, ağın düğümler arası bağlantı yoğunluğundaki yerel değişimleri temsil eder ve klasik genel görelilikteki Riemann eğriliğinin ($R$) yerini alır 9-11.

### 2\. Metrik Dönüşüm ve Topolojik "Kırılma İndisi"

Sürekli limitte, bu yerel değişimler doğrudan sağladığınız **Doğradan Adjacency Metriği** üzerinden uzayın dokusunu tanımlar:$$g\_{\\mu\\nu}(x) \= \\Omega\_{M0} \\cdot \\exp\\left( \- \\frac{\\Phi\_{topo}(x)}{\\Phi\_{ref}} \\right) \\eta\_{\\mu\\nu}$$Burada $W(x)$ alanıyla ilişkili olan yerel topolojik potansiyel ($\\Phi\_{topo}$), uzayın bir tür **"topolojik iletim kapasitesi"** veya optik benzeri bir "kırılma indisi" gibi davranmasını sağlar 12, 13\. Işık, metriğin büküldüğü bir boşlukta değil, bu potansiyel gradyanının farklılaştığı bir ağda ilerler 14\.

### 3\. Sapmanın Modellenmesi: Minimum Taşıma Maliyeti

Işık ışınları (veya kütleçekimsel dalgalar), klasik "geodezik" yollar yerine **"Minimum Yinelemeli Taşıma Maliyeti"** prensibini takip eder 4, 5:$$\\delta \\int A(x,y) d\\tau \= 0$$Bu durum, ışığın en kısa yolu değil, **en yüksek eşevrelilik (coherence) ve en düşük topolojik direnç** sunan yolu tercih etmesi demektir 15\.

* **Yoğun Bölgelerde:** $A$ yüksek ve doygun ($W \\approx 1$) olduğu için sapma minimaldir ve klasik Einstein limitine yaklaşır 16, 17\.  
* **Seyrek/Boşluk (Void) Bölgelerinde:** Çevredeki kütle iplikçikleri ağı "gerdiği" için $\\int A(x,y)dy$ terimi boşluğun merkezinde bir gradyan oluşturur. Bu gerilme, sağladığınız **Topolojik Diferansiyel Form** üzerinden sapmayı zorunlu kılar:$$ds^2 \= 1 \+ \\delta\_w \\int A(x,y) dy^{-2} \\eta\_{\\mu\\nu} dx^\\mu dx^\\nu$$

### 4\. Gravitasyonel Sapma Açısı ($\\alpha$)

Sapma miktarı, ışığın izlediği yol boyunca biriken **topolojik gerilim gradyanı** olarak hesaplanır:$$\\vec{\\alpha}(x) \= \- \\frac{2}{c^2} \\int \\vec{\\nabla}\_{\\perp} \\ln \\left( 1 \+ \\delta\_w \\int \\mathcal{A}(x,y) dy \\right) dz$$  
Bu formülde sapma (sapma vektörü $\\vec{\\alpha}$), metriğin harici bir kuvvetle modifiye edilmesi değil, doğrudan **komşuluk erişilebilirliğinin ($\\mathcal{A}$)** uzaysal gradyanının bir sonucudur 18, 19\.  
**Özetle:** Gravitasyonel sapma, ışığın **Adjacency Curvature** nedeniyle yoğunluğu değişen bir ağda, en düşük enerji maliyetli yolu seçerken uğradığı **"geometrik kırılma"** olarak modellenir. Bu model, boşluk bölgelerinde (voids) madde olmasa dahi, çevresel ağ gerilimi nedeniyle neden ışığın büküldüğünü (Karanlık Maddeye ihtiyaç duymadan) açıklar 13, 20, 21\.  
