# Git速通(以及其他）

<【南京大学-计算机系统基础实验课-W4Git相关】 https://www.bilibili.com/video/BV1Bu4y1K7yr/?share_source=copy_web&vd_source=453c1bc52c8d263e53c12e7186717532>

<【改变了世界的软件！程序员的基本功，Git 应该如何使用？】 https://www.bilibili.com/video/BV1u94y1n73L/?share_source=copy_web&vd_source=453c1bc52c8d263e53c12e7186717532>

# Git是什么

Git 是一个版本控制系统，用于跟踪计算机文件的更改并协调多人之间的这些文件的工作。它是开源的，并且被广泛用于源代码管理。Git 可以在多种操作系统上运行，如 Windows、Linux 和 macOS。

### Git Bash:

Git Bash 是一个应用程序，它为 Windows 用户提供了一个 Bash（Bourne Again SHell）环境。Bash 是一种流行的 Unix shell，Git Bash 允许 Windows 用户访问一系列在 Unix 和 Linux 环境中常见的命令行工具和功能，这些在 Windows 的标准命令行界面中不可用。Git Bash 通常作为 Git for Windows 的一部分安装，提供了一个类似于 Unix 的接口来运行 Git 命令。

> G老师：
>
> - 总的来说，Git 是一个工具，用于版本控制，而 Git Bash 是一个提供 Unix 风格命令行环境的 Windows 应用程序，它使得 Windows 用户能够更方便地使用 Git。

# git 部分

![Untitled (1)](C:\Users\12396\Downloads\Untitled (1).png)

stage：暂存区

working directory：工作区

.gitignore:隐藏生成的文件（.o, Makefile, …)

## 常用命令

- git clone：从远端把仓库拉下来
- git commite： 将暂存区的更改保存到本地仓库的历史记录中
- **git push/pull：把当前版本存档到远端/把代码拉下来**
- git merge：仓库多人管理时，将多线代码合并为一个版本
- git reset：恢复到先前版本

### 推荐练习网站

[visualizing git concepts in D3](https://onlywei.github.io/explain-git-with-d3/)

[Explain Git with D3](https://onlywei.github.io/explain-git-with-d3/)

## 全命令

- git branch

  ```cpp
   git branch <name>
   git branch -d <name>//delete
  ```

- git checkout

```cpp
//switch between branches.
git checkout branchname
```

- git checkout -b

```cpp
//the cobination of git commit and git branch.
git checkout -b branchname
```

- git reset

```cpp
//move head and current branches to your specified locations.
//the number of '^' represent how many steps backwards.
e.g. git reset HEAD^
```

- git revert

```cpp
//undo commits that have already been pushed and shared with the team
//instead of git reset
//create a new commit that will undo all of the work that was done in the commit you want to revert.
git revert branchname
```

- git merge

```cpp
//create a new commit with two parents
git merge branchname
```





- git rebase

```cpp
//把分支变成你指定节点的接下来的主流
git rebase <目标节点名>
```

- git fetch

```cpp
//update all of the "remote tracking branches" in your local repository
git fetch
```

- git pull

```cpp
//git fetch + git merge
git pull
//git fetch + git rebase
git pull --rebase
//set upon to be a default behavior
git config branch.BRANCHNAME.rebase true
```

- git push

```cpp
//If there is any divergence between your local branch and the remote branch, 
//your push will be rejected.
//instead, pull first
```

- git tag

```cpp
//create a tag for a point
git tag <name>
//delete
git tag -d <name>
```

# 终端写代码

## 能用上的命令

l进入编辑，Esc键进入命令模式

:wq保存并退出 :q退出 :q!不保存并退出

# Vim

## 是什么？

- 基于命令行的文本编辑器

## 好处？

- 可以在终端直接运行，方便调试
- 摆脱鼠标
- 命令之间相互结合

### 插件

- nerdtree：文件浏览器
- themes：颜色
- ctags：代码跳转

## 如果用vscode不想报错呢？

- 配置compile_commands.json(bear — make)
- cout大法（printf）