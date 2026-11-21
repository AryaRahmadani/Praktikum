from L2 import total_nilai
from L3 import daftar_matkul, transkip_nilai

matkul_baru = "Jaringan komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5 #nilai B

daftar_matkul.append(matkul_baru)

transkip_nilai[matkul_baru] = mutu_matkul_baru

nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

total_bobot_mutu = sum(transkip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\n--- HASIL REKALUASI SETELAH PENAMBAHAN MATKUL ---")
print("Daftar Mata Kuliah yang Diambil  :", daftar_matkul)
print("Detail Transkrip Mutu            :", jumlah_matkul)
print("Rata-rata Nilai Terbaru          :", round(rata_rata_terbaru, 2))
print("IPK Sementara                    :", round(ipk_sementara, 2))
