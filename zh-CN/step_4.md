## 随机玩家

让我们来选择随机玩家！



+ 为从 `players`（玩家）列表获得一名随机玩家，首先你需要导入 `random`（随机）模块的 `choice`（选择）部分。

	![screenshot](images/team-import-random.png)

+ 要获得一名随机玩家，你可以使用 `choice`（选择）。（你还可以删除打印出单独玩家的代码。）

	![screenshot](images/team-random-player.png)

+ 多次测试你的 `choice`（选择）代码，你会看到每次都会选择一名不同的玩家。

+ 你还可以创建一个名为 `playerA`（玩家 A）的新变量，并使用它来储存你的随机玩家。

	![screenshot](images/team-random-playerA.png)

+ 你将需要一个新列表来储存 A 队中的所有玩家。首先，此列表中应无任何内容。

	![screenshot](images/team-teamA.png)

+ 你现在可以向 `teamA`（A 队）添加你随机选择的玩家。为此，你可以使用 `teamA.append`（__append__ 指添加到末尾）。

	![screenshot](images/team-teamA-add.png)

+ 现在已经选择了你的玩家，你可以将其从你的 `players`（玩家）列表移除。

	![screenshot](images/team-players-remove.png)

+ 添加一个 `print`（打印）命令来测试此代码，从而显示出剩余可供选择的 `players`（玩家）。

	![screenshot](images/team-players-remove-test.png)

	在上文的示例中，Hermione 被选入 `teamA`（A 队），因此已被移出 `players`（玩家）列表。



