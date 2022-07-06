class ser_humano(object):

    def __init__(self):

        self._peso = 0
        self._edad = 0

    @property
    def Peso(self):
        print("getter method called Weight")
        return self._peso

    @property
    def Edad(self):
        print("getter method called for Age")
        return  self._edad

    @Peso.setter
    def Peso(self, a):
        print("setter method called Weight")
        self._peso = a - 1

    @Edad.setter
    def Edad(self, b):
        print("Setter method called Age")
        self._edad = b -1

x = ser_humano()
x.Peso= 4
x.Edad = 5
print("\n")
print(x.Peso)
print(x.Edad)
