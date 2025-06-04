---
title: Zotero configuration
date: 2025-02-27 14:36
modify: 2025-02-27 16:19
author: Jun Gu
aliases: 
type: 
tags:
  - zotero
---

Zotero 自己平时收集文献，阅读文献以及与Obsidian联动。

而且，zotero还可以支持订阅RSS。但是我不经常用，所以使用~~QiReader~~ Follow
> 若寻求中文支持，去中文社区。其他问题可以一概去官方文档和论坛

[tips_and_tricks [Zotero Documentation]](https://www.zotero.org/support/tips_and_tricks)
[plugins [Zotero Documentation]](https://www.zotero.org/support/plugins) 一些可用的插件，但是秉持着不要熵增的原理，非必要勿增加实体。
[Zotero 中文社区 | Zotero 中文维护小组](https://zotero-chinese.com/) 发展蓬勃旺盛的Zotero中文社区


> [!info]+ Account
> 
AccountName : JunGu99

## 1 可用的插件
![Pasted image 20240407223424|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407223424.png)


## 2 General 

### 2.1 Filename format 

![zotero_filename_format|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/zotero_filename_format.png)
[file_renaming [Zotero Documentation]](https://www.zotero.org/support/file_renaming)

1. 当我从Zotero6 升级到 7之后，发现条目下的PDF文档的名字只显示"Full Text PDF" 而不是像之前一样的含有作者，题目的文献名。
**原因:** [kb:attachment_title_vs_filename [Zotero Documentation]](https://www.zotero.org/support/kb/attachment_title_vs_filename) , 首先区分附件名字与文件名，文件名依然是含有作者信息的。但是为了避免在查找时的冲突（比如搜索某个作者和文章名，通常会将附件也列出干扰信息）以及和条目名字重复。全部采用"Full Text PDF"等样式。


## 3 Sync 
1. Zotero 结合zotfile使用onedrive远程同步
```ad-seealso
title: Zotero + Onedrive
collapse: closed
![Pasted image 20240407223822|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407223822.png)
1. Zotfile
![Pasted image 20240407223930|+grid|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407223930.png)
![Pasted image 20240407223952|+grid|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407223952.png)

- File renaming
![Pasted image 20240407224011|+grid|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407224011.png)
![Pasted image 20240407224033|+grid|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407224033.png)

关键步骤：
创建目录硬链接: 链接storage到我的onedrive目录存储文件下。需要各个设备都要同步！
`
mklink /J "C:\Users\jungu\Zotero\storage" "O:\OneDrive\Literature Management\2. Zotero\1. Zotero_storage"
`
```
1. 目前使用Infinicloud作为webDav云存储支持。（升级到Zotero7之后，zotfile不支持适配新版本，所以弃用zotfile.
![zotero_sync|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/zotero_sync.png)

2. 从坚果云换到Infinicloud时，原有的文件并没有同步成功？ 
**原因**：没有重置同步历史，Zotero认为没有必要重新上传未更改的历史。
**解决方案:**  如下图

![](https://s2.loli.net/2025/01/06/l3D7hxTNGI4nR96.png#500)


## 4 Translate for Zotero  
![Pasted image 20240407223551|500|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240407223551.png)
  翻译服务目前使用：
  - DeepL(Free Plan)
> [!info]- Token
> 51e09202-1292-0df3-80cd-4cae6df6d4c0:fx
- 腾讯翻译
> [!info]- Token
> xxxxxxx

- Mistral: small and large 
- qwen: max, plus, turbo 
- Groq: llama3.3-70B 主打一个快速 
- Grok: 充值了5美元，可以有每个月150美元免费额度
- Gemini: Flash, Pro, Flash Thinking and Flash Lite

## 5 Zotero Connector (即浏览器插件)

导入文献，拒绝插入tags
![Pasted image 20240413215614|500|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240413215614.png)

注意，浏览器扩展选项也可以设置 Proxy Setting, 但是这里建议关闭
Follow this suggestion [Zotero Proxy Settings - Zotero Citation Management - LibGuides at Christopher Newport University](https://cnu.libguides.com/zotero/proxysettings) Disable the proxy and google Docs intergration.

## 6 Zotero translator  
>[!WARNING]
>Not language translator

[如何更新 Translator | Zotero 中文社区 (zotero-chinese.com)](https://zotero-chinese.com/user-guide/faqs/update-translators.html#%E6%96%B9%E6%B3%95-2-%E6%89%8B%E5%8A%A8%E6%9B%BF%E6%8D%A2%E6%96%87%E4%BB%B6%E6%9B%B4%E6%96%B0) support chinese and some sites.

Use jasminum(茉莉花插件) plugin to update translator sytles, e.g., sino weibo.

## 7 openURL 
OLD:
~~![Pasted image 20240619005337|500|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/Pasted%20image%2020240619005337.png)~~
NEW:
![OpenURL|500](https://imgbed.kyuinkoo.top/imgbed/2025_02/OpenURL.png)


在科大图书馆这里，可以找到openURL设置。[EndNote 文献管理软件 | 中国科学技术大学图书馆 (ustc.edu.cn)](https://lib.ustc.edu.cn/%e7%94%b5%e5%ad%90%e8%b5%84%e6%ba%90/endnote%e6%96%87%e7%8c%ae%e7%ae%a1%e7%90%86%e8%bd%af%e4%bb%b6/)

openURL的用法：->Library Lookup
![openURL_lookup|200](https://imgbed.kyuinkoo.top/imgbed/2025_02/openURL_lookup.png)

```ad-seealso
title: openURL vs Proxy(conector)
collapse: closed
Zotero Connector 浏览器插件中的代理（Proxy）设置主要用于帮助用户在通过代理服务器访问网络的情况下，仍能顺利连接到图书馆的电子资源。许多高校和研究机构使用代理服务器来控制和监视网络流量，同时也用于认证，以确保只有授权用户能够访问订阅的数据库和期刊。当用户不在校园内部网络时，代理服务器可以用来验证用户身份，使其能够远程访问这些受限资源。

**代理设置的作用：**

- **远程访问资源**：通过配置代理，即使你不在校园内，也可以通过图书馆的代理服务器访问那些通常仅限于校园网络的电子资源。
- **身份验证**：代理服务器通常需要用户名和密码，这些凭据用于验证你是图书馆的合法用户。
- **绕过地域限制**：一些资源可能仅限于特定地理位置的访问，代理服务器可以帮助你绕过这些限制。

**OpenURL与代理设置的区别：**

- **OpenURL** 是一种用于识别和定位文献的协议，它通过包含文献元数据的URL来指向文献的电子版。OpenURL解析器通常由图书馆提供，用于帮助用户从文献引用直接跳转到图书馆订阅的全文资源。
- **代理设置** 则是一个网络配置，它允许你的浏览器通过特定的服务器（通常是图书馆的代理服务器）来访问互联网，以便于身份验证和访问受限资源。

两者结合使用时，OpenURL可以帮助你找到文献的全文链接，而代理设置则确保你能通过图书馆的订阅权限实际访问这些链接。换句话说，OpenURL告诉你文献在哪里，而代理设置让你有权限去那里。

因此，在Zotero Connector中，配置正确的代理设置是确保你能够远程访问图书馆资源的关键，而OpenURL配置则是确保链接解析正确并导向全文资源的重要组成部分。
From QianWen AI
```


## 8 FAQ 

