nilai = {}
nilai = 79
if 80 <= nilai <= 100:
    print( 'yes nilai Anda bagus, nilainya adalah', nilai )
elif 60 <= nilai < 80:
    print( ' nilai anda cukup bagus', nilai )
else:
    print( ' anda tidak lulus' )

# cara lain
nilaimu = 66

for i in range( 0, 10 ):
    print( i )

    if i is nilaimu:
        print( 'nilai terbesar adaah', i )
        break
else:
    print( 'none' )
# ------------


# -------------
data_dari_server_gokar = {
    'tanggal': '2020-12-2020',
    'driver_list': [
        {'nama': 'eko', 'jarak': 10},
        {'nama': 'dwi', 'jarak': 20},
        {'nama': 'tri', 'jarak': 30},
        {'nama': 'catur', 'jarak': 40, 'warna_rambut': 'hitam'},
        {'nama': 'limo', 'jarak': 50}
    ]
}
print( f" waktu : {data_dari_server_gokar['tanggal']}" )
print( f" driver ke-4 adalah {data_dari_server_gokar['driver_list'][3] ['warna_rambut'] }" )
print( f" jarak driver kedua adalah {data_dari_server_gokar['driver_list'][1]  ['nama']}" )
