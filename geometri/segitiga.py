class SegiTiga() :
    def __init__(self, a,t ):
        # ini adalah fungsi yang pertama kali dipanggil saat object diciptakan
        self.a = a
        self.t = t

    def info (self) :
        return f'ini adalah object dari segitiga dengan alas = {self.a} dan tinggi = {self.t}, luas = '

    def hitung_luas (self) :
        return self.a * self.t / 2