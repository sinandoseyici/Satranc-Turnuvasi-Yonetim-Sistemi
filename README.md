# Satranç Turnuvası Yönetim Sistemi

Bireysel satranç turnuvalarında kullanılmak üzere, Uluslararası Satranç Federasyonu’nun (FIDE)
belirlediği İsviçre Sistemi eşleştirme kurallarına benzer kurallara dayalı olarak her turdaki
eşleştirmeleri yapmak ve turnuva sonunda başarı sıralamasının listelenmesi istenmektedir.

- Lisans numarası (LNo): 0’dan büyük tekil (unique) tam sayı (0 ya da negatif bir değer girilmesi, başka oyuncu olmadığını belirtecektir.)
- Ad-soyad: programda hepsi büyük harfe çevrilerek ve Türkçe ile uyumlu olarak kullanılmalıdır.
- Uluslararası (FIDE) kuvvet puanı (ELO): 0, 1000 veya daha büyük tam sayı (ELO puanı yoksa 0)
- Ulusal kuvvet puanı (UKD): 0, 1000 veya daha büyük tam sayı (UKD puanı yoksa 0)

Turnuva başlangıcında, tüm oyuncuların turnuva puanları (bundan sonra Puan diye
bahsedilecektir) 0’dır. Oyuncular, başlangıçta ve her tur öncesinde eşleştirme amacıyla aşağıdaki
ölçütlere göre sıralanırlar (ölçütlerin önceliği aşağı doğru azalmaktadır):

- 1. Puan (büyükten küçüğe doğru)
- 2. ELO (büyükten küçüğe doğru)
- 3. UKD (büyükten küçüğe doğru)
- 4. Ad-soyad (Türkçe ile uyumlu alfabetik sıra)
- 5. LNo (küçükten büyüğe doğru)

Başlangıçta, tüm oyuncular yukarıda belirtildiği şekilde sıralanarak bir başlangıç sıralama listesi
oluşturulur ve bu listeye göre, eşleştirmelerde kullanılmak üzere oyunculara 1’den başlayarak
birer başlangıç sıra numarası (BSNo) verilir. Oluşturulan başlangıç sıralama listesi aşağıdaki
şekilde görüntülenir:

BSNo LNo   Ad-Soyad     ELO  UKD
---- ----- ------------ ---- ----
