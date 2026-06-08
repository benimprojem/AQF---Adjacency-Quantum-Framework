# BÖLÜM 49: AQF Dalga Fonksiyonu ve Faz-Ağ Yayılımı

### 49.1 Metriksiz Kaynak ($M0$) ve Metrikli Katmanlar ($M1-M7$)

AQF modelinde $M0$, zamansız ve metriksiz bir üretim kaynağıdır. Dalga fonksiyonu, $M0$ katmanından $M1-M7$ katmanlarına aktarılan faz bilgisinin, sistemin topolojik düğüm ağındaki yayılımı olarak tanımlanır. $M0$ katmanında uzay veya zaman metriği bulunmadığı için, bu kaynaktan çıkan faz paketi henüz yerel koordinatlara sahip değildir.

### 49.2 Matematiksel Tanım

Dalga fonksiyonu operatörü ($\hat{\Psi}_{AQF}$), düğüm yoğunluğu ($d\sigma$) ve faz gradyanı ($\nabla \phi$) üzerinden ifade edilir:

$$\hat{\Psi}_{AQF} (\phi) = \oint_{\text{düğümler}} \exp\left( i \cdot \int_{M0}^{M1} \nabla \phi \, d\sigma \right)$$

Bu denklemde:

* $\nabla \phi$: Faz imza hattının gradyanı (değişim oranı).
* $d\sigma$: $M1-M7$ katmanlarındaki düğüm yoğunluğunu temsil eden metrik değer.
* $\oint$: Sistemin topolojik bütünlüğü üzerindeki integrasyon.

### 49.3 Faz-Ağ Yayılım Mekanizması

Dalga fonksiyonunun "dalga" özelliği, sistemin düğüm  ve boşluk yapısından kaynaklanır. $M0$ katmanından yayılan faz, $M1-M7$ katmanlarındaki düğüm hatlarında rezonansa girerken, boşluklarda serbest yayılım gösterir. Girişim (interference) desenleri, bu topolojik dokunun fazı bükme biçimiyle oluşur. "Dalga" olarak adlandırılan yapı, kaynağın enerjisi değil, sistemin topolojik dokusu üzerindeki faz yayılımıdır.

### 49.4 Faz Sabitleme (Dalga Fonksiyonu Çökmesi)

Gözlem veya müdahale anında gerçekleşen "dalga fonksiyonu çökmesi", sistemin bir noktada lokalize olmasıdır. AQF terminolojisinde bu, zamansız $M0$ fazının, $M1-M7$ katmanlarının metrikli yapısına (uzay-zaman koordinatlarına) sabitlenmesi operasyonudur. Ölçüm işlemi, $M1-M7$ geometrisinde yayılmakta olan fazı, belirli bir düğüm koordinatında ($A_{ij}$ bağlantısı) dondurarak noktalar.

---

**Özet:** Dalga fonksiyonu, metriksiz $M0$ fazının, metrikli $M1-M7$ katmanlarındaki geometrik yansıması ve bu katmanların düğüm ağı üzerindeki yayılımıdır.