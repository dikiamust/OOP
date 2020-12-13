class PersegiPanjang() :
    def __init__(self, p,l ):
        # ini adalah fungsi yang pertama kali dipanggil saat object diciptakan
        self.p = p
        self.l = l

    def info (self) :
        return f'ini adalah object dari persegi panjang dengan panjang = {self.p} dan lebar = {self.l} '

    def hitung_luas (self) :
        return self.p * self.l
