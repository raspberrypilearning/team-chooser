## عدد فردي من اللاعبِين

دعنا نحسن برنامجك للعمل مع عدد فردي من اللاعبين.

\--- task \---

+ أضف اسمًا آخر إلى ** players.txt الخاص بك </code> قائمة ، بحيث يكون لديك عدد فردي من اللاعبين.</li> </ul> 
    
    ## \--- code \---
    
    language: python filename: players.txt line_numbers: true line_number_start: 1
    
    ## line_highlights: 5
    
    Harry Hermione Neville Ginny Luna
    
    \--- /code \---
    
    \--- /task \---
    
    \--- task \---
    
    إذا اختبرت تعليماتك البرمجية، سترى أنك تتلقى رسالة خطأ.
    
    ![لقطة الشاشة](images/error.png)
    
    \--- /task \---
    
    الخطأ لأن برنامجك يواصل اختيار لاعبين عشوائيين للفريق A ثم الفريق B. ومع ذلك ، إذا كان هناك عدد فردي من اللاعبين ، فبعد اختيار لاعب للفريق A لن يكون هناك لاعبون ليتم اختيارهم للفريق B.
    
    \--- task \---
    
    لإصلاح هذا الخطأ ، يمكنك إخبار البرنامج بـ `الخروج` من حلقة `while` اذا كانت قائمة `اللاعبين` فارغة.
    
    ## \--- code \---
    
    language: python filename: main.py line_numbers: true line_number_start: 10
    
    ## line_highlights: 15-16
    
    while len(players) > 0: player_A = choice(players) team_A.append(player_A) players.remove(player_A)
    
        if players == []:
            break
        
        player_B = choice(players)
        team_B.append(player_B)
        players.remove(player_B)
        
    
    \--- /code \---
    
    \--- /task \---
    
    \--- task \---
    
    إذا قمت باختبار التعليمات البرمجية مرة أخرى ، يبغي أن تشاهد أنها تعمل الآن مع عدد فردي من اللاعبين.
    
    ## \--- code \---
    
    language: python filename: main.py line_numbers: false line_number_start:
    
    ## line_highlights:
    
    Team A ['Harry', 'Ginny', 'Luna'] Team B ['Hermione', 'Neville']
    
    \--- /code \---
    
    \--- /task \---