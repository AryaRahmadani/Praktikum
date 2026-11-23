import time

#class PerekamWaktu:
#    def __enter__(self):
#       self.mulai = time.perf_counter()
#        return self

#    def __exit__(self, exc_type, exc_val, exc_tb):
#        self.selesai = time.perf_counter()
#        self.durasi = self.selesai - self.mulai
#        print(f"Blok kode selesai dieksekusi dalam {self.durasi:.6f} detik")

#with PerekamWaktu():
#    daftar_kata = [str(x) for x in range(2_000_000)]
#    teks = ", ".join(daftar_kata)

#from functools import wraps

#def ukur_waktu(func):
#    @wraps(func)
#    def wrapper(*args, **kwargs):
#        mulai = time.perf_counter()
#        hasil = func(*args, **kwargs)
#        selesai = time.perf_counter()
#        durasi = selesai - mulai
#        print(f"Fungsi '[{func.__name__}]' selesai dieksekusi dalam {durasi:.6f} detik")
#        return hasil
#    return wrapper


#@ukur_waktu
#def hitung_kuadrat(n):
#    return [i ** 2 for i in range(n)]

#@ukur_waktu
#def simulasi_proses():
#    time.sleep(1.5) 

#hitung_kuadrat(5_000_000)
#simulasi_proses()

#waktu_mulai = time.perf_counter()

#total = 0
#for i in range(10_000_000):
#    total += i

#waktu_selesai = time.perf_counter()

#lama_eksekusi = waktu_selesai - waktu_mulai

#print(f"Hasil perhitungan: {total}")
#print(f"Lama waktu eksekusi: {lama_eksekusi:.6f} detik")