AQF (Adjacency Quantum Fold Dynamics) modelinde **Tam Adjacency Kuralı (Exact Adjacency Rule)** ile $A\_{ij}$ matrisini numerik olarak simüle etmek, uzay-zamanın süreksiz, faza duyarlı ve yinelemeli bir bağlantı ağı (graph) olarak inşa edilmesini içerir 1, 2\. Bu matris, sistemin tüm spektrumunu, kabuk yapısını ve kütle hiyerarşisini belirleyen temel operatördür 3, 4\.  
$A\_{ij}$ matrisinin numerik simülasyonu şu adımlarla gerçekleştirilir:

### 1\. Düğüm ve Faz Tanımlama

Simülasyonun başında, bir düğüm kümesi ($V$) tanımlanır ve her düğüme ($i, j$) bir başlangıç transport fazı ($\\phi$) atanır 5, 6\. Düğümler arası transport operatörü $T\_{ij} \= A\_{ij}e^{i\\phi\_{ij}}$ olarak kurgulanır 7, 8\.

### 2\. Tam Adjacency Kuralının Uygulanması

Matrisin her bir elemanı ($A\_{ij}$), aşağıdaki iki ana kısıtın çarpımı olarak hesaplanır 9:$$\\mathbf{A\_{ij} \= \\Theta(\\phi\_c \- |\\phi\_i \- \\phi\_j|) \\cdot C\_{ij}}$$

* **Eşik Fonksiyonu (Adjacency Threshold):** İki düğüm arasında bağlantı kurulabilmesi için faz farkının kritik bir eşikten ($\\phi\_c$) küçük olması gerekir 5\. $\\Theta$ basamak fonksiyonu, faz uyumu olmayan bağlantıları sıfıra indirger 2\.  
* **Topolojik Uyumluluk ($C\_{ij}$):** Bağlantının gücü, ilgili sektörün geometrik kapanma kuralına göre belirlenir 9, 10:$$\\mathbf{C\_{ij} \= \\cos \\left( \\frac{2\\pi d\_{ij}}{N} \\right)}$$Burada $N$ değeri sektöre göre seçilir (Nötrino için 2/4, Kuark için 3, Lepton için 5\) ve $d\_{ij}$ düğümler arası yinelemeli mesafeyi temsil eder 10\.

### 3\. Adjacency Laplacian Matrisinin İnşası

Oluşturulan $A\_{ij}$ matrisi kullanılarak, transportun yayılımını yöneten **Adjacency Laplacian ($\\Delta\_A$)** matrisi kurulur 11, 12:$$\\mathbf{\\Delta\_A \= D \- A}$$Burada $D$, düğüm derecelerini içeren köşegen matristir ($D\_{ii} \= \\sum\_j A\_{ij}$) 11, 12\.

### 4\. Nonlinear Özdeğer Çözümü

$A\_{ij}$ matrisi üzerine bina edilen sistem, merkezi **AQF Spektrum Denklemi** üzerinden iteratif olarak çözülür 13, 14:$$\\mathbf{E\\psi \= \-J\\Delta\_A\\psi \+ g|\\psi|^2\\psi \+ \\sigma|\\psi|^4\\psi \+ V\_{mod}(S)\\psi}$$

* **Numerik Stabilite:** Simülasyonda sonsuz kütle birikimini (runaway) engellemek için **Sextic Saturation ($\\sigma \> 0$)** terimi zorunludur 15, 16\.  
* **Sektörel Shell Kısıtı:** Çözüm sırasında, düğümlerin modüler rezonans potansiyeline ($V\_{mod}$) uyumu kontrol edilir; bu durum numerik olarak belirli "shell" noktalarında ($S=13, 21, 29$ gibi) kararlı eigenmode'ların (parçacıkların) belirmesini sağlar 17-19.

### 5\. Simülasyonun Çıktıları

Bu numerik süreç tamamlandığında, $A\_{ij}$ matrisi şu sonuçları üretir:

* **Parçacık Kütleleri:** Çıkan $E\_n$ özdeğerleri, logaritmik kütle spektrumunu ($m \\sim E$) verir 20, 21\.  
* **Confinement (Hapis):** Kuark sektörü için yapılan simülasyonlarda, tekil düğümlerin (mod6) tam kapanma sağlayamadığı ve ancak birleşik yapılarda (baryon) sızıntısız hale geldiği gözlemlenir 22, 23\.  
* **Emergent Mesafe:** Düğümler arası fiziksel uzaklık, simüle edilen $A\_{ij}$ genliğinin logaritmik fonksiyonu ($d \\sim \-\\log|A\_{ij}|$) olarak elde edilir 24, 25\.

**Özetle;** $A\_{ij}$ matrisi rastgele bir matris değil, faz uyumu ve geometrik kapanma kısıtları altında düğümlerin birbirini "tanıdığı" topolojik bir protokoldür 1, 5\.  
