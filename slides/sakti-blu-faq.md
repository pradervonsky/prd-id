# FAQ SAKTI BLU Familiarisasi

---

## 1. Peran & Setting Akses (Role, Validator, Approver)

**Q: Apa role yang harus dimiliki bendahara pengeluaran di SAKTI BLU?**
A: Di SAKTI biasa rolenya Operator, sedangkan di SAKTI BLU rolenya Approver. Keduanya harus didaftarkan terpisah — approver dan operator tidak bisa dirangkap oleh role yang sama pada modul yang sama (konfirmasi dari CSO KPPN & HAI DJPb).

**Q: Setelah setting peran dan setting validasi, kenapa nama user baru tidak muncul di menu "Mapping Operator Pelaksanaan dan PPK"?**
A: Cek dulu di modul Admin SAKTI biasa apakah user tersebut sudah terdaftar dan role apa saja yang sudah dimiliki. Menu mapping tersebut butuh user dengan role **Admin SAKTI biasa**, bukan Admin BLU.

**Q: Kenapa menu Validasi SPP / Validasi Pembayaran BLU tidak muncul atau tidak bisa diklik untuk user dengan role Validator?**
A: Langkah penanganan: (1) cek ulang Setting Validasi di modul admin, (2) informasikan NIK dan nama user ke tim informasi Dit. PPKBBLU untuk dicek dari sisi Dit. SITP, (3) coba logout–login ulang, ini terkadang menyelesaikan masalah. Apabila masih gagal, diperlukan tiket lanjutan ke tim SITP untuk dilakukan investigasi.

**Q: Untuk akses menu approval/validasi supplier, kenapa daftar supplier tidak muncul di menu Validasi meski muncul di menu Approver?**
A: Indikasi setting validasi kurang tepat. Agar dapat melihat kembali juknis untuk setting validasi atau dapat dibantu setting ulang oleh tim familiarisasi (bisa lewat sesi Teams Meeting bila perlu ditelusuri detil).

---

## 2. Pendaftaran & Pembaruan User ke KPPN

**Q: Bagaimana proses pendaftaran/perubahan role user SAKTI BLU ke KPPN?**
A: Upload/kirim ulang pendaftaran melalui MyIntress. Jika role yang diajukan ditolak KPPN, satker perlu bertiket ke HAI DJPb, lalu hasil jawaban HAI dikomunikasikan kembali ke CSO KPPN mitra untuk ditindaklanjuti.

**Q: Satker piloting belum muncul menunya, kenapa?**
A: Kemungkinan satker tersebut belum di-setup sebagai Satker Piloting di Server Production oleh SITP. Konfirmasi terlebih dahulu ke tim Informasi Dit. PPKBLU apakah satker sudah waktunya piloting, agar bisa diminta setup ke SITP.

---

## 3. Supplier (Rekanan)

**Q: Supplier tipe 2 (rekening tunggal) apakah bisa ditambah nomor rekening baru?**
A: Tidak — supplier tipe 2 hanya boleh punya 1 rekening. Kalau butuh rekening lain, harus dibuat sebagai supplier baru (record baru), bukan mengedit rekening yang lama.

**Q: BAST Non Kontraktual boleh memilih berapa supplier?**
A: Hanya boleh 1 supplier per BAST Non Kontraktual / 1 BAST per SPP Non Kontraktual.

**Q: Data supplier sudah dipakai di BAST, tapi datanya salah (misal mata uang belum dipilih) — apakah harus dihapus dan dibuat ulang?**
A: Jangan dihapus jika sudah dipakai BAST (berisiko BAST ikut hilang) — sebaiknya buat data supplier baru saja untuk data yang benar.

---

## 4. BAST (Berita Acara Serah Terima) & Persediaan

**Q: Perekaman BAST dengan akun 525174/525173 kenapa bermasalah / tidak lanjut ke SPP?**
A: Akun tersebut belum di-setup di SAKTI Production, sehingga BAST tidak membentuk jurnal. Perekaman dengan akun ini harus dipending sampai ada pemberitahuan lanjutan; BAST yang terlanjur direkam akan dihapus terpusat oleh tim dan harus direkam ulang setelah akun disetup.

**Q: Kapan tanggal transaksi yang boleh dipakai saat mencatat BAST — harus sesuai tanggal saat ini atau boleh mundur (backdate)?**
A: Dicatat sesuai tanggal dokumen sumber (kwitansi/bukti transaksi asli). Perekaman backdate diperbolehkan selama periode buku terkait belum tutup buku.

**Q: BAST Kontraktual tidak bisa diubah/dihapus (loading terus / "muter-muter")?**
A: Laporkan nomor BAST-nya ke tim familiarisasi untuk ditelusuri — ini kendala teknis yang butuh penanganan manual dari sisi backend/SITP.

**Q: Pendetilan Persediaan/BMN dari BAST yang direkam via Komitmen BLU, apakah sudah bisa?**
A: Pada periode chat ini statusnya masih kendala di beberapa satker dan sedang diteruskan ke SITP — belum ada solusi permanen yang dikonfirmasi tuntas dalam chat.

---

## 5. SPP, SPM, dan Posting Rule

**Q: Transaksi apa saja yang sudah bisa direkam di SAKTI BLU selama posting rule belum selesai disetup?**
A: Selama posting rule (untuk pengesahan/BAST) belum selesai, transaksi yang bisa direkam baru pembuatan **supplier** dan **kontrak**. Setelah setup posting rule selesai (diumumkan 9 Sept 2026), perekaman BAST, SPP, SPM, SP2R, SP3B, dan RTPH sudah bisa dilakukan.

**Q: Kenapa nominal di lampiran cetak SPP berbeda dengan total SPP yang diinput?**
A: Biasanya terjadi setelah ada perubahan data penerima (hapus/upload ulang file CSV). Solusi: minta tim membandingkan ADK SPP (dikirim via chat pribadi/Japri), lalu coba proses ulang setelah dicek.

**Q: SPP yang dibuat sebelum posting rule selesai kenapa tidak bisa divalidasi?**
A: SPP yang dibuat sebelum setup posting rule selesai harus **dihapus** dan dibuat ulang, karena saat itu posting rule-nya belum tersedia.

**Q: Tampilan daftar SPP hanya menampilkan 10 data terakhir — bagaimana melihat semua?**
A: Ubah tampilan tabel ke opsi "s.d. 100" agar semua data (bukan hanya 10 SPP terakhir) ditampilkan.

**Q: Apakah tanggal SPP bisa diedit setelah dibuat?**
A: Tidak — tanggal SPP tidak bisa diedit setelah tersimpan.

---

## 6. Pembayaran Honor/Remunerasi & BPJS

**Q: Potongan BPJS untuk pegawai BLU (non-PNS) dicatat di komponen apa saat membuat SPP 237F?**
A: Gunakan komponen **N** untuk iuran BPJS yang dibayar oleh pemberi kerja (BLU). Potongan gaji pegawai BLU sendiri hanya PPh21 — porsi 1% BPJS yang dipotong dari honor pegawai tidak tercatat terpisah di SAKTI BLU karena bukan bagian yang disahkan.

**Q: BPJS yang dipotong dari PNS dicatat lewat mana?**
A: Potongan BPJS untuk pegawai berstatus PNS dicatat di SPM yang bersumber dari RM (Rupiah Murni), bukan di SAKTI BLU.

**Q: Karena tagihan BPJS jadi satu (1% potongan pegawai + 4% dari pemberi kerja, total 5% dalam 1 Virtual Account), bagaimana cara mencatatnya di SAKTI BLU agar sesuai?**
A: Remunerasi dicatat **net** (sudah dipotong 1%) — misal remun 1000 dipotong 1% jadi yang disahkan sebagai belanja gaji adalah 990. Sisanya 1% + 4% (total 5%) digabung dan disahkan sebagai belanja gaji BLU komponen BPJS, sehingga SPP pembayaran ke BPJS dibuat utuh sebesar 5%.

---

## 7. RTPH (Rekam Transaksi Penerimaan/Pencatatan Penerimaan PNBP BLU)

**Q: Saat mencatat RTPH, kenapa daftar "Data Wajib Pajak" pada popup pencarian identitas tetap kosong meski referensi Wajib Pajak/Wajib Bayar sudah diisi lewat menu Bendahara → Referensi?**
A: Isu ini masih dalam penelusuran tim/SITP — referensi yang sudah diisi belum terbaca otomatis oleh menu RTPH.

---

## 8. Lain-lain (Kontrak, Notifikasi, OTP)

**Q: Notifikasi tertentu muncul saat transaksi — apakah itu error atau normal?**
A: Tidak semua notifikasi berarti error; beberapa hanya notifikasi informasi dan transaksi tetap bisa dilanjutkan. Jika ragu, screenshot notifikasinya dan tanyakan ke tim untuk dipastikan.

**Q: Belanja UP (keperluan kantor, snack rapat, materai, bensin, dll.) dicatat lewat mekanisme apa?**
A: Boleh menggunakan SPP LS-Banyak Penerima, **sepanjang tidak menghasilkan aset/persediaan**. Jika menghasilkan aset/persediaan, harus lewat Pencatatan BAST Non Kontraktual.

**Q: Pembayaran ke 1 penerima saja (misal listrik ke PLN), apakah tetap boleh pakai SPP LS-Banyak Penerima?**
A: Ini dibahas sebagai alternatif sementara ketika BAST Non Kontraktual masih ada kendala, namun jawaban resmi tim menyebut Validasi SPP juga sempat belum bisa karena kendala posting rule.

**Q: OTP belum bisa digunakan, solusinya?**
A: Akan menggunakan nomor baru, detil teknisnya masih ditindaklanjuti.

---

*Sumber: ekspor chat WhatsApp grup "SAKTI BLU Familiarisasi" (15 Jun – 22 Sep 2026).*
