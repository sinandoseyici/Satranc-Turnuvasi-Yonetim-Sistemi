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

![image](https://user-images.githubusercontent.com/57726183/156373469-720c4af6-4fea-46f7-b1c1-2930c1708c9a.png)

Daha sonra, turnuvadaki tur sayısı ve başlangıç sıralamasına göre ilk oyuncunun ilk turdaki rengi
(b/s) programa girilir. İlk turda, BSNo’su tek olanlar bu rengi, çift olanlar diğer rengi alır. Tur
sayısı; oyuncu sayısının 2 tabanına göre logaritmasının, yukarıya doğru en yakın tamsayıya
yuvarlanması ile bulunan sayıdan daha az ve oyuncu sayısının 1 eksiğinden daha çok olamaz.

İsviçre Sistemi’nin genel kuralları aşağıdaki şekildedir:
- Elenme yoktur, tüm oyuncular, tüm turlarda oynarlar.
- İki oyuncu birbirleriyle sadece bir defa oynayabilir.
- Birbirleriyle eşleştirilen iki oyuncu, eşit puanlı veya aralarındaki puan farkı olabildiğince az olmalıdır.
- Oyuncu sayısı tek ise, tur öncesi yapılan sıralamada en alttaki oyuncu o turda eşleştirilmez, tur atlar (o turu BYE geçer), rengi yoktur ve 1 puan alır.
- İster rakibi gelmediği için, ister tur atladığı için daha önceki turlarda oynamadan puan almış bir oyuncu, o turda tur atlatılamaz.
- Olanaklı ise, oyuncular bir önceki turdaki renklerinin karşıt rengini alırlar. Olanaklı ise, oyuncular siyah ve beyaz renkleri eşit sayıda alırlar.
- Hiç bir oyuncu arka arkaya üç kez aynı rengi alamaz. Bir oyuncu bir rengi diğerinden en çok 2 kez fazla alabilir.
- Tur atlamalar renk hesabında dikkate alınmaz.

Her tur öncesinde, oyuncular daha önce belirtilen şekilde sıralanır ve ilk oyuncudan başlanarak sırayla, eşleştirilmemiş her oyuncuya uygun bir rakip bulunarak masalara yerleştirilir (masa numaraları (MNo) 1’den başlar). Bunun için, yukarıdaki genel kurallar çerçevesinde, aşağıdaki yöntem izlenir:
1. Rakip aranan oyuncuyla aynı puana sahip oyuncu grubu içerisinde aşağıdaki öncelik sırasına göre rakip ara:
2. Rakip aranan oyuncuya bir önceki turda aldığı rengin karşıt rengi verilerek, önceki turda aldığı rengin karşıt rengini alacak, sıralamada en yakın oyuncu
3. Rakip aranan oyuncuya bir önceki turda aldığı rengin karşıt rengi verilerek, önceki turda aldığı renkle aynı rengi alacak (renk kurallarına aykırı değilse), sıralamada en yakın oyuncu
4. Rakip aranan oyuncuya bir önceki turda aldığı renkle aynı renk verilerek (renk kurallarına aykırı değilse), önceki turda aldığı rengin karşıt rengini alacak, sıralamada en yakın oyuncu
5. Uygun bir rakip bulunamadıysa, bir alt puana sahip oyuncu grubu üzerinde 1.1, 1.2 ve 1.3 adımlarını sırayla tekrarla
6. Uygun bir rakip bulununcaya kadar 2. adımı tekrarla

Bütün eşleştirmeler tamamlandıktan sonra, o turdaki eşleştirme listesi aşağıdaki şekilde
görüntülenir (Tur atlayan oyuncu varsa, en sonda belirtilir ve karşısına BYE yazılır):

![image](https://user-images.githubusercontent.com/57726183/156373692-2672f95b-5328-419a-90ab-21e40f8bfe74.png)

Daha sonra bu turda oynanan her maçın sonucu, aşağıdaki sayılar (0-5) ile programa girilir:
- 0: beraberlik, yani maç sonucu ½ - ½
- 1: beyaz galip, yani maç sonucu 1 - 0
- 2: siyah galip, yani maç sonucu 0 - 1
- 3: siyah maça gelmemiş, yani maç sonucu + - -
- 4: beyaz maça gelmemiş, yani maç sonucu - - +
- 5: her iki oyuncu da maça gelmemiş, yani maç sonucu - - -


# Outputs:

![image](https://user-images.githubusercontent.com/57726183/156457255-cd11c748-6a20-489a-adfa-2d15e7ad5cce.png)
![image](https://user-images.githubusercontent.com/57726183/156457304-c0921f3a-1f1e-46f1-a57f-c2941f00978d.png)
![image](https://user-images.githubusercontent.com/57726183/156457348-76829264-0682-4290-834d-698724f13d14.png)
![image](https://user-images.githubusercontent.com/57726183/156457379-4bea9cea-9b4d-4815-a186-1328aff00e1a.png)
![image](https://user-images.githubusercontent.com/57726183/156457405-c429a04f-c4d0-4523-b7d5-df278e6e2327.png)
![image](https://user-images.githubusercontent.com/57726183/156457423-761ab9b8-ac76-49c5-b51b-39cb09ec1afc.png)



