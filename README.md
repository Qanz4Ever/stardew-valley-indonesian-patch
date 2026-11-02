# Stardew Valley Mobile 1.6 - Indonesian Translation Patch

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPLv3-blue.svg)](LICENSE)
[![Target: Android](https://img.shields.io/badge/Platform-Android_Mobile-green.svg)](#)
[![Version: 1.6.15.3](https://img.shields.io/badge/Game_Version-1.6.15.3-orange.svg)](#)

[English](README.md) | [Bahasa Indonesia](README_ID.md) | [简体中文](README_ZH.md)

---

## Overview

This repository provides a 100% native asset replacement patch that translates **Stardew Valley Mobile (Android) v1.6.15.3** into **Indonesian (Bahasa Indonesia)** without requiring SMAPI Android or third-party mod loaders.

By compiling the Indonesian translation directly into MonoGame Android XNB binary files (`XNBa\x05@`), the game runs smoothly on vanilla Android APK installations.

## Features

- **Full Coverage**: 184 binary `.xnb` files covering all NPC dialogue, schedule descriptions, system UI, menus, festival dialogues, event cutscenes, items, and quest logs.
- **Mobile Optimized**: Contains translation for all mobile-exclusive options and controls (touch controls, pinch-to-zoom, auto-attack, dynamic toolbars).
- **Format Integrity**: Verified token matching (`{0}`, `{1}`, `#$e#`, `$h`, `@`, `%name`) to prevent runtime crashes.
- **Clean Distribution**: Only contains text and dialogue data (~1 MB total). No unnecessary texture sprites or tilesets are included, preventing visual bugs.

## Quick Installation

Download the ready-to-use zip from the [Releases](https://github.com/Qanz4Ever/stardew-valley-indonesian-patch/releases) section:
- Extract `StardewValley-Indonesian-Patch-v1.6.15.3.zip`.
- Replace the files inside your decompiled APK at `assets/Content/`.
- Recompile & sign the APK.

For detailed instructions using ApkStudio or MT Manager, see **[INSTALL.md](INSTALL.md)**.

## Project Structure

```
.
├── Content/                   # Ready-to-replace compiled .xnb files
│   ├── Characters/Dialogue/   # 52 NPC dialogue XNBs
│   ├── Data/                  # Events, Festivals, TV, Quests, Mail, etc.
│   └── Strings/               # UI, 1.6 Strings, schedules, Objects, etc.
├── scripts/                   # Open-source conversion and packing scripts
├── releases/                  # Prebuilt patch zip archives
├── INSTALL.md                 # Complete installation tutorial
└── LICENSE                    # GNU AGPLv3
```

## Credits & Acknowledgements

- Translation source based on the community translation by **Dan** (*Mod Bahasa Indonesia - Modded*).
- Unpack/Pack tooling powered by **xnbcli** (by LeonBlade).
- Stardew Valley is developed by **ConcernedApe**.

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPLv3)**. See [LICENSE](LICENSE) for full details.
