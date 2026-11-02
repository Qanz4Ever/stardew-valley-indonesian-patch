# Patch Terjemahan Bahasa Indonesia - Stardew Valley Mobile 1.6

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPLv3-blue.svg)](LICENSE)
[![Target: Android](https://img.shields.io/badge/Platform-Android_Mobile-green.svg)](#)
[![Version: 1.6.15.3](https://img.shields.io/badge/Game_Version-1.6.15.3-orange.svg)](#)

[English](README.md) | [Bahasa Indonesia](README_ID.md) | [简体中文](README_ZH.md)

---

## Ringkasan Proyek

Repositori ini menyediakan patch pengganti aset bawaan (native asset replace) yang menerjemahkan **Stardew Valley Mobile (Android) versi 1.6.15.3** ke dalam **Bahasa Indonesia** tanpa memerlukan mod loader pihak ketiga seperti SMAPI Android.

Seluruh data terjemahan telah dikompilasi secara presisi ke dalam format biner MonoGame Android (`XNBa\x05@`), sehingga game dapat langsung dimainkan secara stabil pada APK vanilla Android.

## Fitur Utama

- **Cakupan Penuh**: 184 file `.xnb` biner mencakup seluruh dialog NPC, jadwal kegiatan, menu antarmuka (UI), dialog festival, cutscene event cerita, nama barang, dan catatan misi.
- **Dioptimalkan untuk Android**: Termasuk penerjemahan menu khusus mobile (pengaturan kontrol sentuh, cubit untuk perbesar/zoom, serang otomatis, ukuran bilah alat).
- **Integritas Format Terjamin**: Verifikasi menyeluruh pada placeholder token (`{0}`, `{1}`, `#$e#`, `$h`, `@`, `%name`) guna mencegah crash saat game berjalan.
- **Bersih & Ringan**: Hanya memuat aset teks dan bahasa (~1 MB). Tidak menyertakan spritesheet karakter atau tekstur non-bahasa yang tidak perlu agar terhindar dari konflik grafis.

## Pemasangan Cepat

Unduh arsip patch siap pakai di bagian [Releases](https://github.com/Qanz4Ever/stardew-valley-indonesian-patch/releases):
- Ekstrak file `StardewValley-Indonesian-Patch-v1.6.15.3.zip`.
- Timpa folder `Content` ke dalam folder decompiled APK Anda di `assets/Content/`.
- Rebuild & Sign ulang APK.

Panduan langkah demi langkah menggunakan ApkStudio atau MT Manager dapat dibaca di **[INSTALL.md](INSTALL.md)**.

## Struktur Repositori

```
.
├── Content/                   # File biner .xnb siap replace ke assets/Content
│   ├── Characters/Dialogue/   # 52 file dialog NPC
│   ├── Data/                  # Events, Festival, TV, Quest, Surat/Mail, dll.
│   └── Strings/               # UI, String 1.6, Jadwal, Objek/Item, dll.
├── scripts/                   # Script Python sumber terbuka untuk build & pack
├── releases/                  # File arsip .zip patch rilis
├── INSTALL.md                 # Panduan instalasi lengkap
└── LICENSE                    # Lisensi GNU AGPLv3
```

## Kredit & Ucapan Terima Kasih

- Basis data terjemahan mengadaptasi terjemahan komunitas oleh **Dan** (*Mod Bahasa Indonesia - Modded*).
- Tooling unpacking dan packing ditenagai oleh **xnbcli** (karya LeonBlade).
- Stardew Valley diciptakan dan dikembangkan oleh **ConcernedApe**.

## Lisensi

Proyek ini dilisensikan di bawah **GNU Affero General Public License v3.0 (AGPLv3)**. Silakan baca file [LICENSE](LICENSE) untuk ketentuan lengkapnya.
