AQF (Adjacency Quantum Fold Dynamics) modelinde nükleer bağ enerjisi, standart fizikteki gluon alanları veya potansiyel kuyuları yerine, **yinelemeli komşuluk ağı (adjacency network)** üzerindeki içsel gerilim ve taşıma stresi üzerinden hesaplanır. Özellikle proton ve nötron gibi baryonların kütlesinin %99'unu oluşturan bu enerji, **Adjacency Laplacian ($\\Delta\_A$)** operatörünün yönettiği transport süreçlerinin bir sonucudur 1, 2\.  
Nükleer bağ enerjisinin Adjacency Laplacian üzerinden hesaplanma süreci şu temel adımlara dayanır:

### 1\. Geometrik Sıkışma ve Ortak Kenar Paylaşımı

Baryonlar, üç adet **mod6 (üçgensel)** kuark katlanma yapısının birleşerek dış sınırda bir **5-gen (pentagonal)** kilitlenme oluşturmasıyla meydana gelir 3, 4\. Bu birleşme sırasında üçgenler, en yakın komşuluk adımlarında **iç transport hatlarını (ortak adjacency kenarları)** paylaşırlar 2, 4\.

### 2\. Baryon Bağ Lagrangianı ($\\mathcal{L}\_{Baryon\\\_Bağ}$)

İç kenarlardaki bu yoğunlaşma ve faz sapması, bağ enerjisini üreten temel Lagrangian terimi ile formüle edilir 5:$$\\mathbf{\\mathcal{L}*{Baryon\\\_Bağ} \= J*{iç} \\sum\_{\\langle ij \\rangle\_{iç}} |\\Psi\_i \- \\Psi\_j|^2 \+ \\alpha\_{\\phi\\\_iç} \\sum\_{\\langle ij \\rangle\_{iç}} (\\Delta\\phi\_{ij})^2}$$Burada:

* **$J\_{iç} \\sum |\\Psi\_i \- \\Psi\_j|^2$:** Bu terim, Adjacency Laplacian'ın ($\\Delta\_A \= D \- A$) kuadratik formudur ve iç hatlardaki transport akışının şiddetini belirler 6, 7\.  
* **$\\langle ij \\rangle\_{iç}$:** Üçgenlerin birbirine temas ettiği ve paylaştığı **iç transport hatlarını** temsil eder 5\.  
* **$J\_{iç}$:** Paylaşılan hatlardaki transport katsayısıdır ve vakum değerinden çok daha büyüktür ($J\_{iç} \\gg J\_{vakum}$) 5\.

### 3\. Enerji Özdeğerine Katkı (Kütle Üretimi)

Sistem sürekli limite ($a \\to 0$) geçtiğinde, bu iç kenarlardaki ekstrem yerel gradyanlar ($\\nabla A\_{ij}$), pürüzsüz manifold üzerinde devasa bir **Adjacency Curvature (Transport Eğriliği)** deformasyonu yaratır 5\. Bu durum, durağan durum spektrum denklemine bir bağ potansiyeli ($\\Delta V\_{bağ}$) olarak eklenir 8:$$\\mathbf{E\\psi \= \-Ja^2\\nabla^2\\psi \+ g|\\psi|^2\\psi \+ \\sigma|\\psi|^4\\psi \+ \\left( V\_{mod}(S) \+ \\Delta V\_{bağ} \\right)\\psi}$$

### 4\. Hesaplama Sonucu: %99 Kuralı

Nihai bağ enerjisi, bu yerel **"hiper-gerilim"** alanının integral toplamıdır 8:

* **Çıplak Kütle:** Kuarkların kendi mod6 lokalizasyonları toplam kütlenin sadece **%1'ini** oluşturur 9, 10\.  
* **Bağ Enerjisi:** Adjacency Laplacian üzerinden hesaplanan ortak kenar transport gerilimi, proton/nötron kütlesinin **%99'unu** (yaklaşık 938 MeV) üretir 1, 8\.

**Özetle;** nükleer bağ enerjisi, Adjacency Laplacian'ın iç transport hatları üzerindeki **kuadratik farklar toplamı** olarak hesaplanır. Bu hesaplama, parçacıkların kütlesini dışarıdan atanan bir parametre yerine, ağın geometrik kısıtlarından doğan bir **"durağan gerilim özdeğeri"** olarak tanımlar 11-14.  
