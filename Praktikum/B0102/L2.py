from L1 import (
    str_nilai_algoritma,
    str_nilai_basis_data,
    str_nilai_pemrograman_web,
    sks_per_matkul,
    is_aktif,
)

nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n--- HASIL EVALUASI AVAL ---")
print("Total Nilai      :", total_nilai)
print("Rata-Rata Nilai  :", round(rata_rata_nilai, 2))
print("Total SKS        :", total_sks_diambil)
print("Status Lulus     :", is_lulus_semester)
