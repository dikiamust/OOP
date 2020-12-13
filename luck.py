# MENGGUNAKAN OOP
print( 'hope' )

from geometri.persegi import PersegiPanjang

p1 = PersegiPanjang(10, 3)
print( p1.info() )
print( p1.hitung_luas() )

from geometri.segitiga import SegiTiga

z1 = SegiTiga(10, 5)
print( z1.info() )
print( z1.hitung_luas() )
