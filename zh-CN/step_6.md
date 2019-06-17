## 选择很多队员

接下来，你要确保每一个队员都被选入某个队中。

+ 突出选中为A队和B队选择队员的代码，然后按tab键缩进代码。
    
    ![截图](images/team-loop-tab.png)

+ 添加一个**while**循环来继续选择队员直到`players`列表的长度为0。
    
    ![截图](images/team-loop-while.png)

+ 运行你的代码进行测试。 你应该看到队员们被选入A队或B队，直到没有余下队员为止。
    
    ![截图](images/team-loop-test.png)

+ 在你的`while`循环**后面**添加代码以显示`teamA`列表（确保它没有缩进）。
    
    这意味着只有在所有的队员都被选择之后，`teamA`才被输出一次。
    
    ![截图](images/team-teamA-paste.png)

+ 因为它们仅用于测试你的代码，因此您可以对 `teamB` 执行相同的操作，也可以删除其他输出命令。
    
    现在你的代码应如图所示：
    
    ![截图](images/team-loop-finished.png)

+ 再次测试你的代码，你应该只看到你的队员名单以及最终团队的名单。
    
    ![截图](images/team-loop-finished-test.png)