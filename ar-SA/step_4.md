## لاعبون عشوائيون

لنختر لاعبِين عشوائيين!



+ لتتمكن من الحصول على لاعب عشوائي من القائمة `players`، ستحتاج أولًا إلى استيراد الجزء `choice` من الوحدة `random`.

	![screenshot](images/team-import-random.png)

+ للحصول على لاعب عشوائي، يمكنك استخدام `choice`. (ويمكنك أيضًا حذف التعليمة البرمجية لطباعة اللاعبِين بشكل فردي).

	![screenshot](images/team-random-player.png)

+ اختبر تعليمة `choice` البرمجية عدة مرات وسترى اختيار لاعب مختلف في كل مرة.

+ يمكنك أيضًا إنشاء متغير جديد يُسمى `playerA` واستخدامه لتخزين اللاعب العشوائي.

	![screenshot](images/team-random-playerA.png)

+ ستحتاج إلى قائمة جديدة لتخزين كل اللاعبِين في الفريق A. ويجب أن تكون هذه القائمة فارغة لتبدأ بها.

	![screenshot](images/team-teamA.png)

+ يمكنك الآن إضافة اللاعب الذي تم اختياره عشوائيًا إلى `teamA`. ولتفعل ذلك، يمكنك استخدام `teamA.append` (وتعني __append__ الإضافة أو الإلحاق في النهاية).

	![screenshot](images/team-teamA-add.png)

+ بعد أن تم الآن اختيار لاعبك، يمكنك حذفه من قائمة `players`.

	![screenshot](images/team-players-remove.png)

+ اختبر هذه التعليمة البرمجية بإضافة أمر `print` لعرض اللاعبِين المتبقين في القائمة `players` للاختيار منهم.

	![screenshot](images/team-players-remove-test.png)

	في المثال أعلاه، تم اختيار Hermione لـ `teamA`، ولذا تم حذفها من القائمة `players`.



