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

BSNo   LNo   Ad-Soyad      ELO   UKD

xxxx xxxxx   XXXXXXXXXXX  xxxx  xxxx   

Daha sonra, turnuvadaki tur sayısı ve başlangıç sıralamasına göre ilk oyuncunun ilk turdaki rengi
(b/s) programa girilir. İlk turda, BSNo’su tek olanlar bu rengi, çift olanlar diğer rengi alır. Tur
sayısı; oyuncu sayısının 2 tabanına göre logaritmasının, yukarıya doğru en yakın tamsayıya
yuvarlanması ile bulunan sayıdan daha az ve oyuncu sayısının 1 eksiğinden daha çok olamaz.

İsviçre Sistemi’nin genel kuralları aşağıdaki şekildedir:
- Elenme yoktur, tüm oyuncular, tüm turlarda oynarlar.
- İki oyuncu birbirleriyle sadece bir defa oynayabilir.
- Birbirleriyle eşleştirilen iki oyuncu, eşit puanlı veya aralarındaki puan farkı olabildiğince
az olmalıdır.
- Oyuncu sayısı tek ise, tur öncesi yapılan sıralamada en alttaki oyuncu o turda eşleştirilmez,
tur atlar (o turu BYE geçer), rengi yoktur ve 1 puan alır.
- İster rakibi gelmediği için, ister tur atladığı için daha önceki turlarda oynamadan puan
almış bir oyuncu, o turda tur atlatılamaz.
- Olanaklı ise, oyuncular bir önceki turdaki renklerinin karşıt rengini alırlar. Olanaklı ise,
oyuncular siyah ve beyaz renkleri eşit sayıda alırlar.
- Hiç bir oyuncu arka arkaya üç kez aynı rengi alamaz. Bir oyuncu bir rengi diğerinden en
çok 2 kez fazla alabilir.
- Tur atlamalar renk hesabında dikkate alınmaz.
