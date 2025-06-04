---
title: 我的windows电脑设置
date: 2024-04-07 18:34
modify: 2025-05-15 14:53
author: Jun Gu
aliases: 
type: 
tags: []
---
## 1 从硬件开始点亮
1. 定位到主板问题所在 ![[../Notes/2024/WeeklyNotes/2024-W15#2.1 周一]]
1. 学习硬件茶谈的视频装机
	1. 主板CPU安装
	2. 内存条安装
	3. 固态硬盘安装
	4. CPU散热器安装
	5. 主板安装
	6. SATA硬盘安装
	7. 机箱风扇安装，需要了解机箱风道 [硬核科普|机箱风扇怎么安装，如何科学的布置机箱风道？](https://www.bilibili.com/video/BV1Mi4y1M7Mz?vd_source=6883557c36a63a7aa490280d2d56db0e)
	8. 电源的安装
	9. 电源接线
	10. 显卡安装

此时硬件安装完毕！


## 2 如何重装系统
使用移动硬盘结合微PE工具，参考该视频进行重装系统！移动硬盘需要格式化！
[微PE辅助安装_硬件茶谈](https://www.bilibili.com/video/BV1DJ411D79y?p=2)

中间可能会遇到一些问题，比如需要设置原先的系统盘格式化，不能分区。这样安装到新的固态硬盘时，才可以成功。主要是参考了视频的弹幕和评论！

选择专业版（从科大的正版软件下载，校外可以使用[该网址](https://wvpn.ustc.edu.cn/)）之后，需要激活哦！使用KMS工具（科大提供的）


## 3 下载驱动程序
[驱动程序是什么东西？为什么要安装驱动程序？如何正确官方的安装纯净版驱动?](https://www.bilibili.com/video/BV1v7411e7AE?vd_source=6883557c36a63a7aa490280d2d56db0e)

1. Nvidia 驱动程序下载 [NVIDIA GeForce 驱动程序 - N 卡驱动 | NVIDIA](https://www.nvidia.cn/geforce/drivers/)
2. Intel  驱动程序与支持助理 [英特尔® 驱动程序和支持助理 (intel.cn)](https://www.intel.cn/content/www/cn/zh/support/detect.html)  **可以选择不用**
3. 主板 驱动程序，网卡、无线网卡、声卡、蓝牙、核显、SATA、芯片组等等 [下载中心 | 官方支持 | ASUS 中国](https://www.asus.com.cn/support/download-center/)

4. Logitech GHUB
罗技鼠标驱动，可以使用板载内存模式 (将设置装入硬件中)， 即配置好可以不用启动GHUB，甚至卸载GHUB。
需要修改默认配置，调正DPI以及给其他的按键分配宏等！
1. 换用迈从A7 Pro鼠标，轻盈顺畅。使用网页驱动程序修改侧键

## 4 UI 调整
1. 首先针对带鱼屏设置: **缩放提高到125%，然后文本大小设置为110%**
2. 默认壁纸调整
3. 字体安装，霞鹜文楷、得意黑、Fira Code 均存放在`OneDrive/Others` 下
4. 从Microsoft Store 下载 TranslucentTB
5. 从Microsoft Store 下载 EarTrumpet
6. 下载F.lux 护眼工具
7. Wallpaper Engine 壁纸, 根据Python Clock自制的时钟壁纸
![[../Notes/2024/WeeklyNotes/attachments/Pasted image 20240408212225.png|500]]
8.  系统设置-个性化-主题 中修改鼠标光标为大； 桌面图标设置 不显示回收站。使得桌面为全空； 任务栏 中取消显示小组件与搜索框；
9. 系统设置-辅助功能-视觉效果-动画效果。**关闭** 和windows系统版本有关。
10. 系统设置-个性化-任务栏 调整自己适应的任务栏配置
![[../Notes/2024/WeeklyNotes/attachments/Pasted image 20240410124651.png|500]]
11. Runcat 显示CPU占比


## 5 综合软件
** 1. 图吧工具箱 **

包含针对各个硬件的不同应用集合，包括HWiNFO等个人之前使用的，也有各个硬件的温度检测器以及烤鸡工具，硬盘的健康信息检查。

以及Geek 卸载软件工具! 以及包括DiskGenius 更好的磁盘分区工具

** 2. 压缩工具 **

7-Zip Vs Bandizip

7-Zip 体积小巧，免费开源

Bandizip UI界面清晰、功能较全但是新版本付费、且包含广告！
使用的最后一个无广告的免费版本6.29，如何取消自动更新弹窗呢？
```ad-seealso
title: Disable Update
collapse: closed
删除软件路径下的Update程序即可
[Bandzip6.29 最后的无广告免费版（非破解） - 『精品软件区』 - 吾爱破解 - LCG - LSG |安卓破解|病毒分析|www.52pojie.cn](https://www.52pojie.cn/thread-1609663-1-1.html)
```



** 3 本地视频播放 PotPlayer **


** 4 Alist Desktop  ** 挂载软件

[AList Desktop (nn.ci)](https://ad.nn.ci/zh) 
我已经花50元钱购买3个激活机会。
激活码也即面包多订单号:
```ad-done
title: Key
collapse: closed
d1d49404da0927b5c6c9bd230a9f4e86
```

 ** 5 Bilibili 客户端 **
 注意在开始菜单中复制粘贴新的启动项为bilibili。方便快速查找

** 6 QQ 音乐**

** 7 ~~Eleve Clock~~**
可以使用Wallpaper中的一个桌面代替

** 8 Tai  **
统计各app使用时间

**9 Shion ** 
[shion-app/shion: Time tracker | 时间追踪 🍂 (github.com)](https://github.com/shion-app/shion)
 >[!Note]
 >Free alternative of ManicTime

** 9. QQ NT**

** 10. Wechat ** 
 
 探索其他可以优化微信的工具，我记得Github上有开源项目，可以使用

** 11. LocalSend **
 跨设备传输文件


## 6 游戏软件

1. Steam 
2. EPIC
3. WeGame 
4. 雷神加速器，还有1000余小时加速时长！

## 7 VPN代理软件
通常可以参考机场官网推荐的代理软件，比如Clash for windows, Hiddify for Windows 以及由于Clash删库跑路的问题，可以使用Clash.verge 继承Clash for windows.
**跟随官网推荐使用即可，跨平台均可使用，比如Hiddify或者按照提示继续使用Clash for Windows**


## 8 生产力软件
** 1. VS Code **

使用Github 账号登陆 同步设置

** 2 会议软件 **
1. 腾讯会议
2. Zoom

** 3. 剪切板工具 **
1. Ditto 
将Ditto的数据库文件放至OneDrive中`O:\OneDrive\Software\Ditto`，在不同机器上设置路径，类似Zotero。即可实现跨设备剪切板同步
![image.png|300](https://s2.loli.net/2024/07/15/3xL4sYCNjVDotyE.png)


1. 配合powertoys 使用 [教程 | 为 PowerToys 添加“剪贴板管理器”功能 - WinDiscover](https://windiscover.com/posts/add-clipboard-manager-to-powertoys.html)   
 - [CoreyHayward/PowerToys-Run-ClipboardManager](https://github.com/CoreyHayward/PowerToys-Run-ClipboardManager)

2. [EcoPaste](https://github.com/ayangweb/EcoPaste) 支持Mac和Win

** 4. 福昕高级PDF编辑器 **

使用科大正版认证

** 5.  Listary **

[Listary – Free File Search Tool & App Launcher](https://www.listary.com/) 
~~使用  <kbd>Alt</kbd> + <kbd>Space</kbd> 代替原先两个<kbd>Ctrl </kbd>~~
两个<kbd>Ctrl </kbd>~~
~~可以下载Everything 全局文件搜索工具使用~~ 升级到6.3后，UI更改，搜索引擎更换，可以使用默认。

** 6. PowerToys **
使用  <kbd>Alt</kbd> + <kbd>Space</kbd> 
有配置备份

** 7. 截屏工具 ** 

1. Snippaste
2. PixPin 

Snippaste 更常用，但是Pixpin功能更丰富，比如OCR、长截图以及GIF动图。

*如无必要，勿增实体！* 所以选择顺手的，有需求再学习新的。注意学习和时间成本！

**  8. 文献管理软件 **
1. Endnote20 插入Word文档较好使用。注意备份自己的Library与Endnote output Style.


** 9. 翻译软件 **
1. Copytranslator
2. 欧陆词典
3. 网易有道云词典

应该整理单词本，在上面两个词典二选一

** 10. RDP 远程桌面**

#windows
[[Windows Remote Desktop]]
1. [更改远程桌面的侦听端口 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/clients/change-listening-port)
2.  由于使用的是内网，需要做内网穿透。可以参考[远程桌面 - 允许从你的网络外部访问你的电脑 | Microsoft Learn](https://learn.microsoft.com/zh-cn/windows-server/remote/remote-desktop-services/clients/remote-desktop-allow-outside-access) 这篇文章中谈到的如何设置端口转发。也可以参考这个[Windows10/11远程桌面设置教程 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/429984367)。
3. 由于更改了默认的远程桌面侦听端口，需要查看防火墙是否放开该端口，如果没有需要新添一个入站规则，针对你所修改后的侦听端口。
4. 使用微软账户登录的电脑，允许该微软账户登录，但是使用其他设备的RDP连接时，会出现该账户无效等报错。有两个解决方法，下策是创建一个本地账户，使用该本地账户登录。上策是需要在管理员模式下的命令行界面，运行该命令
```cmd
runas /u:MicrosoftAccount\jungulove@outlook.com winver
```
即可。

5. 需要测试一下开启双重验证、无密码保护下的账号能否远程连接成功; 可以使用之前的密码登录(在开启双重验证、无密码保护情况下)；在新的电脑上，可以先取消这些保护措施，设置密码用于登录，之后再开启这些安全保证。

** 11. Ubuntu WSL2 **

#wsl 
需要在新电脑上安装WSL, 注意应该是WSL2。可以参考windows的官方指示。
一般在新的电脑上，需要在控制面板-程序与功能-开启windows功能， 开启HyperV、WSL、虚拟机等。然后在Powershell 用命令行安装。 
有两种方法可以将旧的ubuntu系统移植到新的电脑上:
1. 一个是使用之前的从C盘移植到其他盘，打包的方式.
[[../../3. Computer/如何将WSL从C盘移植到其他盘|如何将WSL从C盘移植到其他盘]]
2. 另外一个方式是找到ubuntu存储路径，比如`C:\Users\jungu\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu22.04LTS_79rhkp1fndgsc\LocalState` 在这里，替换ext4.即可。通常最好保证用户名和机器名一致。

** 12 终端模拟器 **
1. Windows Terminal
JSON文件备份 
2. WezTerm 
使用我的Github仓库中的配置，同步即可；注意配置好字体

** 13 EndNote **

从学校正版软件里下载即可；注意登录账号同步，Library存在OneDrive里；且需要配置OpenURL.

** 14 iSlide **

PPT制作工具

** 15 xftp8 **

sftp数据传输软件 


** 16 微软拼音输入法 **

1. 词库和自学习。注意词库可以导出，放在以下路径
> [!note]+ Path
> 
O:\OneDrive\Config\lexicon

2. 开启专业词典，比如大气科学等
3. 外观，选择字体 微软雅黑、字体大小 中、以及灰色的文本输入主题。
4.  <kbd>win </kbd> + <kbd>; </kbd> 开启emoji
5. U V 模式; 简体中文下输入 <kbd>u</kbd>或者<kbd>v</kbd>即可
![[attachments/Pasted image 20240508203417.png|700]]

References:
1. [当前Windows系统上最好用的输入法是什么? ](https://www.zhihu.com/question/22182413)

** 2. Typora **

Typora做为Markdown编辑预览器，其在v1.0版本后开始收费，我使用的是v0.9.93版本，已经上传到Rec网盘里。链接：https://rec.ustc.edu.cn/share/196093b0-f4da-11ee-87d3-f3d68a6e7490。其他系统诸如Mac或者Linux的版本，可以在百度网盘中找到！

** 16. 等等贴 **

** 17. Hibit uninstaller **

** 18. DevToys **
From Microsoft Store


### 8.1 SSHFS 
SSHFS挂载远程文件系统到本地，参考[[../../3. Computer/How To Use SSHFS to Mount Remote File Systems on Windows|How To Use SSHFS to Mount Remote File Systems on Windows]]





### 8.2 Mathpix Snipping Tools 


### 8.3 Git 
1. Gitkaren
2. VS code 里的插件Gitlens

### 8.4 GPT 工具 
1. Perplexity 
2. ChatGPT 
3. Claude 
4. Poe
5. 桌面客户端NextChat，使用学生自用的copilot的服务转换为GPT4.
```ad-note
title: Token
collapse: open
41C5-DB09 device code 

ghu_xxx
```


### 8.5 X11 windows的服务端
VcXsrv
Xming

选择一个即可

### 8.6 iThoughts 思维导图

### 8.7 DevTools 


### 8.8 Mulming Viewer 
多文件看图，适合比对。也可以拼接图片！适合科研图片看图


### 8.9 Win-vind 
支持使用vim的方式操控windows


### 8.10 IDM 
[IDM下载器 Internet Download Manager v6.42 Build 10 - 『精品软件区』 - 吾爱破解 - LCG - LSG |安卓破解|病毒分析|www.52pojie.cn](https://www.52pojie.cn/thread-1929729-1-1.html)
`打开PowerShell，输入“irm massgrave.dev/ias \| iex”|`

[下载利器IDM v6.42.12绿色版 - 哔哩哔哩 (bilibili.com)](https://www.bilibili.com/read/cv35705140/)


### 8.11 Edge 

![[../Notes/2024/WeeklyNotes/attachments/Pasted image 20240407231130.png]]

1. Tampermonkey
![[../Notes/2024/WeeklyNotes/attachments/Pasted image 20240407231207.png]]


1. 修改默认搜索引擎为 https://www.searchforjohn.com/; 修改方法如下
	1. ![[../Notes/2024/WeeklyNotes/attachments/Pasted image 20240427001820.png|500]] 修改浏览器的搜索框
	2. 修改使用主页插件的搜索框 ![[../Notes/2024/WeeklyNotes/attachments/Pasted image 20240427010319.png|500]]
2. 修改bing, 因为使用梯子之后，地址栏搜索使用国内的bing 会很慢。修改默认的搜索引擎，这样用梯子的时候是国外的bing、不用梯子的时候是国内的bing。不影响相应速度 


### 8.12 网页监测插件
1. Check 酱
2. 网页更新提醒

## 9 Windows 开机自动启动项

一般针对一些小软件，没有设置开机自启，需要手动设置。
1. 复制软件的快捷方式
2. <kbd>win</kbd>  + <kbd>r<kbd></kbd> 打开运行，输入`shell:startup` 打开自启动目录。
3. 粘贴快捷方式
4. 最后开启任务管理器-> 启动应用 查看git 

## 10 蓝牙设备
Airpords 连接蓝牙设备，显示有配对，但是无法连接以及无法删除。通过设备管理器删除后，刷新又会出现该设备。经过搜索互联网无相关内容，询问蓝牙设备器绿联的客服，发现可能是电脑自身（新装机后）的蓝牙设备已经连接过Airpords设备，切换至自身蓝牙后发现可以连接，所以在自身蓝牙设备器上卸载该设备，然后禁用自身蓝牙。使用蓝牙接收器，重新连接Airpords(*注意此时不应该在手机旁，或者在手机上忽略该耳机设备*)即可



## 11 修图工具
1. [Sanster/IOPaint: Image inpainting tool powered by SOTA AI Model. Remove any unwanted object, defect, people from your pictures or erase and replace(powered by stable diffusion) any thing on your pictures. (github.com)](https://github.com/Sanster/IOPaint) 
2. photopea 
3. GIMP 
4. Inkspace



## 12 音量修改软件 
steelseries
