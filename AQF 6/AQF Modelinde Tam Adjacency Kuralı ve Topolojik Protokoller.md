AQF (Adjacency Quantum Fold Dynamics) modelinde **Tam Adjacency Kuralı (Exact Adjacency Rule)**, yinelemeli komşuluk ağındaki ($A\_{ij}$) düğümlerin rastgele değil, belirli bir topolojik protokole göre nasıl bağlandığını belirleyen temel yasadır 1, 2\. Bu kural, sistemdeki tüm parçacık spektrumu, kabuk yapısı ve etkileşimlerin temelini oluşturur 2\.  
Tam Adjacency Kuralı şu bileşenlerle formüle edilir:

### 1\. Yerel Yinelemeli Erişilebilirlik (Threshold)

İki düğümün (node) birbirine bağlanabilmesi için aralarında **faz uyumu** olması gerekir 2\. Eğer iki düğüm arasındaki faz farkı belirli bir eşik değerin ($\\phi\_c$) üzerindeyse, bu düğümler arasında bir bağlantı kurulamaz 2\. Bu durum **Adjacency Threshold** denklemi ile ifade edilir:  
$$\\mathbf{A\_{ij} \= \\Theta(\\phi\_c \- |\\phi\_i \- \\phi\_j|)}$$ 3  
Burada:

* **$\\Theta$:** Adjacency aktivasyon fonksiyonudur (Heaviside basamak fonksiyonu benzeri) 3\.  
* **$\\phi\_c$:** Kapanma eşiğidir (closure threshold) 3\.

### 2\. Topolojik Uyumluluk ($C\_{ij}$)

Sadece faz farkının düşük olması yeterli değildir; bağlantının aynı zamanda ilgili sektörün (lepton, kuark vb.) **geometrik kapanma kuralına** da uygun olması gerekir 4\. Bu uyumluluk şu formülle hesaplanır:  
$$\\mathbf{C\_{ij} \= \\cos \\left( \\frac{2\\pi d\_{ij}}{N} \\right)}$$ 4  
Burada:

* **$N$:** Sektörel kapanma geometrisidir (Nötrino için 2/4, Kuark için 3, Lepton için 5\) 4\.  
* **$d\_{ij}$:** Yinelemeli ayrışma/mesafedir 4\.

### 3\. Nihai "Exact Adjacency" Formülü

Bu iki bileşenin birleşimiyle **Tam Adjacency Kuralı** şu şekilde sabitlenir:  
$$\\mathbf{\\boxed{A\_{ij} \= \\Theta(\\phi\_c \- |\\phi\_i \- \\phi\_j|) \\cdot C\_{ij}}}$$ 5

### Kuralın Fiziksel Sonuçları ve Önemi

* **Süreksizlik:** Bu kural sayesinde uzay artık sürekli bir manifold değil, **faza duyarlı yinelemeli bir bağlantı ağı** (phase-compatible recursive connectivity network) haline gelir 3\.  
* **Shell Yapısının Kökeni:** Parçacıkların shell (kabuk) koordinatları, bu kuralın dikte ettiği geometrik kısıtlar üzerinden doğal olarak türetilir 6\.  
* **Kusursuz Kapanma Yasağı:** AQF'de mükemmel kapanma ($\\epsilon \= 0$) yasaktır; çünkü bu durum etkileşimlerin (interaction) kaybolmasına neden olur 7\. Gerçek fizik, her zaman küçük bir **artık uyumsuzluk (residual mismatch \- $\\epsilon$)** gerektirir ki bu da ince yapı sabitinin ($\\alpha$) temelidir 7, 8\.  
* **Parçacık Kararlılığı:** Bir modun (parçacığın) stabilize olabilmesi için, bu kurala uygun olarak kapalı bir yinelemeli yol (loop) oluşturması zorunludur 7, 9\.

