## لاعبون عشوائيون

دعونا نختار لاعبين عشوائيين!

+ لتكون قادرًا على الحصول على لاعب عشوائي قائمة اللاعبين الخاصة بك, اولاً تحتاج لاستيراد جزئية `الاختيار` من وحدة `random`.
    
    ![لقطة الشاشة](images/team-import-random.png)

+ للحصول على لاعب عشوائي, يمكنك استخدام `choice`. (يمكنك أيضا حذف التعليمات البرمجية لطباعة لاعبين منفردين)
    
    ![لقطة الشاشة](images/team-random-player.png)

+ اختبر تعليمات `choice` البرمجية الخاصة بك بضع مرات، ويجب أن ترى لاعب مختلف يتم اختياره في كل مرة.

+ يمكنك أيضًا إنشاء متغير جديد يسمى `playerA` ، واستخدامه لتخزين لاعب عشوائي.
    
    ![لقطة الشاشة](images/team-random-playerA.png)

+ ستحتاج إلى قائمة جديدة لتخزين جميع اللاعبين في الفريق A. للبدء ، يجب أن تكون هذه القائمة فارغة.
    
    ![لقطة الشاشة](images/team-teamA.png)

+ يمكنك الآن إضافة لاعبك المختار عشوائياً إلى `teamA`. للقيام بذلك ، يمكنك استخدام `teamA.append` (**append** يعني إضافة إلى النهاية).
    
    ![لقطة الشاشة](images/team-teamA-add.png)

+ الآن بعد أن تم اختيار اللاعب الخاص بك ، يمكنك إزالته من قائمة اللاعبين ` الخاصة بك`.
    
    ![لقطة الشاشة](images/team-players-remove.png)

+ اختبر هذا الرمز عن طريق إضافة امر ` طباعة`, لاظهار `اللاعبين` المتبقين للاختيار منهم.
    
    ![لقطة الشاشة](images/team-players-remove-test.png)
    
    في المثال أعلاه ، تم اختيار Hermione لـ `teamA` ، وهكذا تمت إزالته من قائمة اللاعبين ``.