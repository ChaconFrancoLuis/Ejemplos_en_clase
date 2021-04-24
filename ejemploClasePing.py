from pythonping import ping

class pinging():
    def __init__(self):
        self.ip="atributo x"

    def hacerping(self):
        b=input("Ingrese la IPV4 a hacer ping: ")
        a= ping(b,verbose=True)


ip1=pinging()
ip1.hacerping()
