AQF (Adjacency Quantum Fold Dynamics) modelinin temel yapı taşlarından biri olan **Adjacency Laplacian ($\\Delta\_A$)**, malzemenin iç yapısı ile sınırları arasındaki transport farkını topolojik kısıtlar üzerinden hesaplamak için mükemmel bir araçtır 1, 2\. Topolojik yalıtkanlar ve iletken kenar modları, AQF çerçevesinde **"faz sızıntısı" (leakage)** ve **"topolojik kapanma" (closure)** arasındaki mekansal dengenin bir sonucu olarak şu şekilde hesaplanabilir:

### 1\. Adjacency Laplacian ($\\Delta\_A$) ve Sınır Koşulları

AQF'de transportun yayılımını ve lokalizasyonunu yöneten operatör $\\Delta\_A \= D \- A$ matrisidir 3, 4\. Bu matrisin sınır düğümlerindeki (boundary nodes) davranışı, malzemenin dış ortamla (vakum veya başka bir faz) olan etkileşimini belirler.

* **İç Yapı (Yalıtkan Hali):** Malzemenin iç düğümlerinde faz uyumu tam sayı katlarında kilitlenmişse ($\\oint d\\phi \\approx 2\\pi n$), sistem **"perfect closure"** durumundadır 5, 6\. Bu bölgede faz sızıntısı ($\\epsilon$) sıfıra yakınsar, bu da Adjacency Laplacian'ın o düğümlerde enerji iletimine direnç göstermesi, yani yalıtkan (insulator) bir davranış sergilemesi anlamına gelir 7, 8\.  
* **Sınır Düğümleri (Kenar Modları):** Sınırda, komşuluk ağı ($A\_{ij}$) aniden kesintiye uğrar veya dış ortamın fazıyla ($M0$ vakum potansiyeli) etkileşime girer 9, 10\. Bu topolojik süreksizlik, iç yapıda sönümlenen fazın sınırda tam olarak kapanamamasına neden olur.

### 2\. Faz Sızıntısı (Leakage) Olarak İletkenlik

AQF'de etkileşimlerin ve akışın kaynağı **faz uyumsuzluğudur ($\\Delta\\phi \\neq 0$)** 11, 12\.

* Topolojik yalıtkanlarda iletken kenar modları, bu **"residual mismatch" ($\\epsilon$)** parametresinin sınır düğümlerinde stabilize olmuş halidir 13, 14\.  
* $\\Delta\_A$ matrisinin sınır koşulları çözüldüğünde, sınır düğümlerindeki özdeğerlerin (eigenvalues) iç bölgelerden farklı olarak **"leakage mode"** ürettiği görülür 15, 16\. Bu modlar, fazın ağ üzerinde kayıpsız (veya düşük dirençli) bir şekilde akmasına izin veren "iletken kanalları" temsil eder.

### 3\. Matematiksel Hesaplama Mekanizması

Sızıntı modlarının oluşumu, merkezi spektrum denkleminin sınır düğümlerindeki yerel çözümüyle belirlenir:$$\\mathbf{E\\psi\_i \= \-J\\sum\_{j \\in boundary} A\_{ij}(\\psi\_j \- \\psi\_i) \+ V\_{mod}(S)\\psi\_i}$$

* **Sınır Koşulu:** Sınırda komşuluk genliği ($A\_{boundary}$) vakumun temel üretim seviyesine ($\\Lambda\_{M0}$) bağlanır 17, 18\.  
* **Topolojik Koruma:** Kenar modları, malzemenin sahip olduğu mod yapısına (örneğin mod6 veya mod8) bağlı bir **"topolojik sargı sayısı" (winding number)** ile korunur 19, 20\. İçerideki kilitlenme ne kadar güçlüyse, sınırda oluşan faz gradyanı o kadar keskin ve iletken olur.

### 4\. Özet Analiz

Bölge,Topolojik Durum,AQF Parametresi,Fiziksel Karşılık  
İç Bölge,Tam Kapanma (Perfect Closure),"$\\Delta\\phi \\to 0, \\epsilon \\to 0$",Topolojik Yalıtkan  
Sınır,Eksik Kapanma (Leakage),"$\\Delta\\phi \\neq 0, \\epsilon \\neq 0$",İletken Kenar Modu  
**Sonuç olarak;** Adjacency Laplacian matrisinin sınır koşulları, fazın nerede hapsolacağını (insulator) ve nerede serbestçe "sızacağını" (conductor) doğrudan belirleyen geometrik operatördür 1, 2\. Bu durum, topolojik yalıtkanları AQF modelinin sunduğu **"geometrik transport optimizasyonu"** prensibinin makroskopik bir uygulaması haline getirir 21, 22\.  
