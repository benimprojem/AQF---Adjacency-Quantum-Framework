AQF (Adjacency Quantum Fold Dynamics) modelinde **süperakışkanlık ve Bose-Einstein Yoğuşması (BEC)**, yinelemeli komşuluk ağı üzerindeki kolektif transport modları olarak tanımlanır Chat History. Bu mekanizmanın tam formülasyonu, sistemin doğrusal olmayan özdeğer denklemleri ve topolojik kilitlenme koşulları üzerinden inşa edilir.

### 1\. Süperakışkan Akışta Kritik Eşik Parametreleri

Süperakışkan bir fazın simülasyonunda kararlılığı ve akış eşiğini belirleyen temel parametreler şunlardır:

* **Genlik Eşiği ($|\\psi|^2\_{crit}$):** Stabilizasyonun korunabilmesi için genliğin **$|\\psi|^2 \< g/\\sigma$** sınırında kalması gerekir 1-3. Bu eşik aşıldığında sistem "recursive overload" (yinelemeli aşırı yükleme) yaşar ve süperakışkanlık sönümlenir 4, 5\.  
* **Adjacency Threshold ($\\phi\_c$):** İki düğüm arasında transportun başlayabilmesi için faz farkının kritik bir değerden ($|\\phi\_i \- \\phi\_j| \< \\phi\_c$) küçük olması zorunludur 6, 7\.  
* **Artık Uyumsuzluk ($\\epsilon$):** Sürtünmenin kaynağı olan **faz sızıntısıdır** (leakage) 8-10. Süperakışkanlık için $\\epsilon$ değerinin sistemin hata düzeltme (self-correction) kapasitesinin altında kalması gerekir Chat History.  
* **Reinforcement Kazancı ($G\_n$):** Bir modun süperakışkan kalabilmesi için yapıcı girişimin ($G\_n \\to \\max$) kritik bir stabilizasyon değerini ($G\_c$) aşması şarttır 11, 12\.

### 2\. Ağ Yoğunluğu ve Sürtünmesiz Akış İlişkisi

Ağ yoğunluğu ($A\_{ij}$), sistemdeki **"recursive erişilebilirliği"** temsil eder 13, 14\. Sürtünmesiz akış ile ağ yoğunluğu arasındaki matematiksel bağ şu prensiplere dayanır:

* **Emergent Mesafe:** AQF'de mesafe, komşuluk genliğinin logaritmik bir fonksiyonudur: **$d(i,j) \\sim \-\\log|A\_{ij}|$** 15-18.  
* **Transport Yayılımı:** $A\_{ij}$ değeri maksimize olduğunda (yüksek ağ yoğunluğu), transport operatörü $T\_{ij} \= A\_{ij}e^{i\\phi\_{ij}}$ ağ üzerinde hiçbir engele takılmadan yayılır Chat History.  
* **Düşük Mismatch Limiti:** Yüksek ağ yoğunluğu, faz farklarını ($\\Delta\\phi$) sönümleyerek sistemdeki topolojik direnci (sürtünmeyi) sıfıra yaklaştırır 116, Chat History. Sürekli limitte bu durum, pürüzsüz ve viskozitesiz bir akış (Lorentz-benzeri limit) üretir 19, 20\.

### 3\. BEC Faz Geçişi ve Topolojik Sargı Sayısı

BEC faz geçişi sırasında sistem, tekil eksitasyon modlarından kolektif bir kilitlenme durumuna geçer Chat History. Bu süreçte **topolojik sargı sayısı ($Q\_w$)** şu şekilde evrilir:

* **Faz Öncesi (Gaz Hali):** Her bir mod kendi bağımsız sargı sayısına ve sızıntı oranına sahiptir. Fazlar rastgele dağıldığı için kolektif bir $Q\_w$ tanımlanamaz Chat History.  
* **Kilitlenme (Transition):** Tüm düğümler aynı transport modunda ($K \\equiv K\_0 \\pmod N$) kilitlenir 21, 22\.  
* **Kolektif Sargı:** Faz geçişi tamamlandığında, sistemin tamamı için geçerli olan tek bir tam sayı sargı değeri (**$Q\_w \= \\frac{1}{2\\pi} \\oint d\\phi \\in \\mathbb{Z}$**) ortaya çıkar 23-25. Bu kilitlenme, sızıntıyı (leakage) minimize ederek enerjinin sistem içinde kayıpsız dönmesini sağlar Chat History.

### 4\. Süperakışkan Mekaniğinin AQF Formülasyonu

AQF çerçevesinde süperakışkan mekaniği aşağıdaki denklem seti ile tam olarak ifade edilir:  
**A. Kolektif Eigenmode Denklemi (Gross-Pitaevskii Limiti):**Süperakışkanın durağan hali, continuum limitindeki şu NLSE tabanlı denklemle yönetilir:$$\\mathbf{E\\psi \= \-Ja^2\\nabla^2\\psi \+ g|\\psi|^2\\psi \+ \\sigma|\\psi|^4\\psi \+ V\_{mod}(x)\\psi}$$ 26-28  
**B. Akış Hızı ve Faz Gradyanı:**Süperakışkanın hızı ($\\mathbf{v}$), ağ üzerindeki faz gradyanı tarafından belirlenir:$$\\mathbf{v \\propto \\nabla\_A \\phi}$$ 234, Chat History  
**C. Süreklilik ve Sızıntı Dengesi:**Akışın korunumu, minimum recursive mismatch ($\\epsilon$) kısıtı altındadır:$$\\mathbf{\\frac{\\partial |\\psi|^2}{\\partial \\tau} \+ \\nabla\_A \\cdot (|\\psi|^2 \\mathbf{v}) \\approx \\epsilon}$$ 129, Chat History  
**D. Enerji Fonksiyoneli:**Süperakışkan sistemin toplam enerjisi, transport stresi ve doygunluk terimlerinin toplamıdır:$$\\mathbf{\\mathcal{E}\\psi \= \\int d^3x \\leftJ|\\nabla\\psi|^2 \- \\frac{g}{2}|\\psi|^4 \+ \\frac{\\sigma}{3}|\\psi|^6 \+ V\_{mod}|\\psi|^2 \\right}$$ 29-31  
**Özetle;** AQF modelinde süperakışkanlık, ağın **maksimum erişilebilirlik ($A\_{ij} \\to \\max$)** ve **minimum sızıntı ($\\epsilon \\to 0$)** limitinde çalıştığı, vakum üretim kaynağından gelen fazın topolojik bir kilitlenme (modN) içinde sürtünmesizce aktığı bir evredir Chat History.  
