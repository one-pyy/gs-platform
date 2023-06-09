# 选手常见问题

## 关于计分

排名按照选手获得的总分计算，如有总分相同的情况，最后一次成功提交的时间更早的选手排名更靠前。

竞赛采用动态分值机制，**第一阶段解出的选手数量越多，该题分数越少。**

具体来说，如果一个基础分值为 `x` 的 Flag 在第一阶段结束时有 `n` 名校内选手解出， 则所有在第一阶段解出的选手实际获得 `x * (0.4 + 0.6 * 0.98n)` 分（向下取整到整数）。

在第二阶段解出放出提示或降低难度后的题目将获得上述计算结果乘以 33% 的分数。选手可以在比赛平台的排行榜和提交历史记录页面确认自己实际获得的分数。

*本届竞赛将公式的指数部分从 max(n-1, 0) 调整为了 n，以解决第一阶段解出人数为 0 或 1 时第二阶段得分相同的 bug。*

## 关于终端交互

带有终端交互的题目会在服务器上运行一个特定的程序。每次通过终端连接到题目时，会启动该程序，允许你向它输入内容，并读取输出。 你需要根据题目所给信息找出程序中的漏洞，并与服务器上的程序交互获得 Flag。

除了使用网页终端以外，你也可以使用命令行工具 netcat (`nc <hostname> <port>`) 来连接到服务器，或者使用任意编程语言带 socket 通信功能的库。 在 CTF 比赛中常用的是 Python 的 [pwntools](https://pypi.org/project/pwntools/)，[这里是它的文档](http://docs.pwntools.com/en/latest/intro.html)。

**终端交互题目的连接频率限制是 30 秒内 3 次。**

除 XSS Bot 以外的题目环境可能没有外网，因此无法反弹 Shell。

**请注意网页终端和 tty 有每行最多 4096 字符的限制，**如果需要一行输入很多内容建议利用输入重定向或使用 pwntools。 参见 [这篇文章](https://lug.ustc.edu.cn/planet/2019/09/how-to-use-nc/#注意事项)。

## 关于 Web 题目环境

为了避免选手之间互相干扰，部分 Web 题目为每个选手分配一个独立的后端环境。

点击 “访问题目网页” 时，将会访问启动器（网址形如 `prob**-manager.geekgame.pku.edu.cn/docker-manager/start?...`）， 此时将启动一个该题的后端环境（域名形如 `prob**-xxxxxxxx.geekgame.pku.edu.cn`），并将选手重定向到这个域名。

**持续 15 分钟没有人访问时，后端环境将自动关闭。**下次点击 “访问题目网页” 时会重新启动一个新的环境。

如果环境出现问题，选手可以点击比赛平台的 “关闭环境” 按钮。关闭后等待 10 秒可以重新启动新的后端环境。

Web 题目环境可能没有外网，因此无法反弹 Shell。

## 常用工具

下面列举了一些解决题目可能需要用到的工具，供选手参考。有些软件是收费的商业软件。

- 好用的编程语言，例如 Python
- 好用的搜索引擎，例如 Google 和 Bing
- 好用的领域特定搜索引擎，例如 [CVE 漏洞条目](https://cve.mitre.org/cve/search_cve_list.html) 和 [RFC 文档](https://datatracker.ietf.org/)
- 好用的开发环境，例如 VSCode 和 JetBrains 旗下 IDE
- 虚拟化软件，例如 VMWare Workstation、WSL 2 和 Docker
- 处理多媒体文件的工具，例如 Adobe 系列软件、Audacity、ffmpeg
- 分析二进制文件的工具，例如 010 Editor
- Web 流量分析和调试工具，例如 WireShark、Fiddler Classic 和现代浏览器的开发者工具
- HTTP 请求库，例如 requests
- 调试器，例如 gdb、IDA、pwndbg 和 x64dbg
- x86 反编译工具，例如 IDA (Hex-Rays Decompiler)、Ghidra 和 Binary Ninja
- 其他平台反编译工具，例如 JADX（对于 Java）和 dotPeek（对于 C#）
- 科学计算和密码学算法库，例如 gmpy2、sympy 和 pycryptodome