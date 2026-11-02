# Installation Guide / Panduan Pemasangan

[English](#english) | [Bahasa Indonesia](#bahasa-indonesia)

---

## English

### Prerequisites
- Stardew Valley Mobile APK (v1.6.x, verified on `1.6.15.3`).
- An APK tool on PC (e.g., **ApkStudio**, **APK Easy Tool**, or **apktool**) or on Android (e.g., **MT Manager**, **APK Editor Pro**).

### Method 1: Using ApkStudio / PC Decompiler (Recommended)

1. **Decompile the APK**:
   - Open ApkStudio and decompile your `Stardew Valley` APK.
2. **Copy the Patch Files**:
   - Extract `StardewValley-Indonesian-Patch-v1.6.15.3.zip`.
   - Copy the entire `Content` folder from the patch.
   - Paste and overwrite into:
     `<decompiled_apk_folder>\assets\Content\`
   *(Or if using the project directory on Windows, run `apply_to_apk.bat`)*.
3. **Recompile and Sign**:
   - In ApkStudio, click **Build / Recompile APK**.
   - Sign the newly created APK using your keystore or test key.
4. **Install and Play**:
   - Install the signed APK on your Android device.
   - Launch the game. Since the patch replaces the default language assets, the game will automatically run in Indonesian when the language is set to English/Default!

### Method 2: Direct Zip Replace via MT Manager (Direct on Android Phone)

1. Open **MT Manager** on your Android device.
2. Navigate to your Stardew Valley APK file.
3. Tap the APK and select **View** (do not install yet).
4. Navigate inside the APK to:
   `assets/Content/`
5. On the opposite panel, open the extracted `Content/` folder from this patch.
6. Select all subfolders (`Characters`, `Data`, `Strings`) and tap **Add / Replace** with auto-signing enabled.
7. Install the modified APK.

---

## Bahasa Indonesia

### Persyaratan
- File APK Stardew Valley Mobile versi 1.6 (diuji dan diverifikasi pada `1.6.15.3`).
- Tool pengelola APK di PC (**ApkStudio**, **APK Easy Tool**, atau **apktool**) atau di HP Android (**MT Manager**, **APK Editor Pro**).

### Metode 1: Menggunakan ApkStudio di PC (Sangat Direkomendasikan)

1. **Decompile APK**:
   - Buka ApkStudio dan lakukan decompile pada file APK Stardew Valley Anda.
2. **Timpa File Patch**:
   - Ekstrak file `StardewValley-Indonesian-Patch-v1.6.15.3.zip`.
   - Copy seluruh isi folder `Content` dari patch.
   - Paste dan timpa (overwrite) ke direktori:
     `<folder_hasil_decompile>\assets\Content\`
   *(Jika path folder APK Anda sesuai default, Anda bisa langsung menjalankan file `apply_to_apk.bat`)*.
3. **Recompile dan Sign**:
   - Di ApkStudio, klik **Build / Recompile APK**.
   - Lakukan Sign APK menggunakan test key atau keystore Anda.
4. **Pasang & Mainkan**:
   - Kirim dan pasang file APK hasil recompile ke HP Android Anda.
   - Buka game. Karena patch ini menimpa aset bahasa default, game akan otomatis berbahasa Indonesia saat opsi bahasa berada pada Default/English.

### Metode 2: Menggunakan MT Manager Langsung di HP Android

1. Buka aplikasi **MT Manager** di HP Android Anda.
2. Cari file APK Stardew Valley Anda.
3. Ketuk file APK lalu pilih **View** (Melihat isi APK).
4. Buka folder:
   `assets/Content/`
5. Pada panel sebelah, buka folder `Content/` dari file patch ini yang sudah diekstrak.
6. Pilih folder `Characters`, `Data`, dan `Strings`, lalu pilih **Tambahkan / Add** (centang opsi Auto Sign).
7. Tunggu proses update APK selesai, lalu install APK tersebut.
