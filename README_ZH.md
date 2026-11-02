# 星露谷物语移动版 1.6 - 印尼语本地化补丁包 (Indonesian Translation Patch)

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPLv3-blue.svg)](LICENSE)
[![Target: Android](https://img.shields.io/badge/Platform-Android_Mobile-green.svg)](#)
[![Version: 1.6.15.3](https://img.shields.io/badge/Game_Version-1.6.15.3-orange.svg)](#)

[English](README.md) | [Bahasa Indonesia](README_ID.md) | [简体中文](README_ZH.md)

---

## 项目概述

本项目为 **星露谷物语移动版 (Android) v1.6.15.3** 提供原生资源替换补丁，将游戏默认英文语言完整汉化/转换为 **印度尼西亚语 (Bahasa Indonesia)**。无需安装 SMAPI Android 或任何第三方 Mod 加载器。

所有印尼语文本均已编译为标准 Android MonoGame XNB 二进制格式 (`XNBa\x05@`)，在原生 APK 上运行稳定流畅。

## 主要特性

- **完整覆盖**：共 184 个编译好的 `.xnb` 核心语言文件，包含所有 NPC 对话、日程、系统界面、节日对话、剧情事件、物品及任务说明。
- **针对移动端优化**：包含针对 Android 触控专属界面的本地化（点触移动、捏合缩放、自动攻击、工具栏大小调节等）。
- **参数格式校验**：经过严格的代码占位符 (`{0}`, `{1}`, `#$e#`, `$h`, `@`, `%name`) 校验，杜绝运行报错。
- **纯净轻量**：仅包含纯文本及语言数据（总大小约 1 MB），不包含任何无关的人物精灵图或贴图，保证零冲突。

## 快速安装

从 [Releases](https://github.com/Qanz4Ever/stardew-valley-indonesian-patch/releases) 页面下载预打包文件：
- 解压 `StardewValley-Indonesian-Patch-v1.6.15.3.zip`。
- 将解压出的 `Content` 文件夹复制并替换到反编译 APK 的 `assets/Content/` 目录下。
- 重新编译并签名 APK 即可安装游玩。

详细图文操作指南请参见 **[INSTALL.md](INSTALL.md)**。

## 目录结构

```
.
├── Content/                   # 可直接替换到 assets/Content 的 .xnb 二进制文件
│   ├── Characters/Dialogue/   # 52 个 NPC 对话文件
│   ├── Data/                  # 事件、节日、电视、任务、信件等
│   └── Strings/               # UI 界面、1.6 新增文本、日程、物品说明等
├── scripts/                   # 开源构建与封包脚本 (Python)
├── releases/                  # 预编译补丁压缩包
├── INSTALL.md                 # 详细安装步骤说明
└── LICENSE                    # GNU AGPLv3 开源协议
```

## 鸣谢

- 翻译文本基础来源于社区译者 **Dan** (*Mod Bahasa Indonesia - Modded*)。
- XNB 解包与打包工具基于 **xnbcli** (由 LeonBlade 开发)。
- 《星露谷物语》由 **ConcernedApe** 开发制作。

## 许可证

本项目依据 **GNU Affero 通用公共许可证 v3.0 (AGPLv3)** 开源。详情请参阅 [LICENSE](LICENSE)。
