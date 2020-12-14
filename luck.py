# MENGGUNAKAN OOP
from geometri.bangunruang import BangunRuang

print( 'hope' )
from geometri.persegi import PersegiPanjang

p1 = PersegiPanjang(10, 3)
print( p1.info() )
print( p1.hitung_luas() )

from geometri.segitiga import SegiTiga

z1 = SegiTiga(10, 5)
print( z1.info() )
print( z1.hitung_luas() )

#MEMBUAT OBJECT DARI KELAS BANGUN RUANG

b1 = BangunRuang ()
print(b1.info())
print(b1.hitung_luas())

#POLIMERPHISME : KEMAMPUAN OBJECT UNTUK MERESPON BERBEDA,THD PEMANGGILAN METHOD YG SAMA
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(z1)

print('polimorphisme')
for bangun_ruang in daftar_bangun_ruang :
    print(bangun_ruang.info())