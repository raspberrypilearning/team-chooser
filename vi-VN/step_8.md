## Người chơi lẻ

Hãy cải thiện chương trình của bạn để làm việc với số lượng người chơi lẻ.

+ Thêm một tên khác vào danh sách `players.txt` của bạn để bạn có số lượng người chơi lẻ.
    
    ![ảnh chụp màn hình](images/team-luna.png)

+ Nếu bạn kiểm tra mã của mình, bạn sẽ thấy rằng bạn nhận được thông báo lỗi.
    
    ![ảnh chụp màn hình](images/team-error.png)

+ Lỗi là vì chương trình của bạn tiếp tục chọn người chơi ngẫu nhiên cho đội A và sau đó là đội B. Tuy nhiên, nếu có số lượng người chơi lẻ thì sau khi chọn cầu thủ cho đội A, không còn cầu thủ nào để chọn cho đội B.
    
    Để khắc phục lỗi này, bạn có thể nói chương trình của bạn để `nghỉ` ra khỏi bạn `trong khi` vòng lặp nếu bạn `người chơi` danh sách rỗng.
    
    ![ảnh chụp màn hình](images/team-fix.png)

+ Nếu bạn kiểm tra mã của bạn một lần nữa, bạn sẽ thấy rằng nó bây giờ làm việc với một số lẻ của người chơi.
    
    ![ảnh chụp màn hình](images/team-fix-test.png)