## Rastgele oyuncular

Rasgele oyuncu seçelim!

+ `oyuncular` listenizden rastgele oyuncular seçebilmek için ilk önce `random` modülünün `choice` bölümünü kodlamaya dahil etmeniz gerekiyor.
    
    ![ekran görüntüsü](images/team-import-random.png)

+ Rastgele bir oyuncu elde etmek için `choice` komutunu kullanabilirsiniz. (Ayrıca tek tek oyuncuları yazdıran kodu da silebilirsiniz.)
    
    ![ekran görüntüsü](images/team-random-player.png)

+ Bir kaç kez `choice` kodunuzu deneyin, her seferinde farklı bir oyuncunun seçilmiş olduğunu göreceksiniz.

+ Rastgele oyuncunuzu kaydetmek için ayrıca yeni bir `Aoyuncusu` değişkeni oluşturabilirsiniz.
    
    ![ekran görüntüsü](images/team-random-playerA.png)

+ A takımındaki tüm oyuncuları saklamak için yeni bir listeye ihtiyacınız olacak. Başlayabilmek için, bu liste boş olmalıdır.
    
    ![ekran görüntüsü](images/team-teamA.png)

+ Şimdi rastgele seçilmiş oyuncuları `Atakimi`'na ekleyebilirsiniz. Bunu yapmak için `Atakimi.append` komutunu kullanabilirsiniz (**append** sonuna ekle anlamına gelir).
    
    ![ekran görüntüsü](images/team-teamA-add.png)

+ Artık oyuncunuz seçildiğine göre, onları `oyuncular` listenizden kaldırabilirsiniz.
    
    ![ekran görüntüsü](images/team-players-remove.png)

+ `print` komutunu ekleyip, içinden seçim yapmak için `oyuncular` listesindeki kalan oyuncuları göstererek kodunuzu test edin.
    
    ![ekran görüntüsü](images/team-players-remove-test.png)
    
    Yukarıdaki örnekte, Ceyda `Atakimi` için seçilmişti böylece adı `oyuncular` listesinden çıkarılmış oldu.