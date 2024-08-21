class Humano:
    def __init__(self, edad, estatura, peso):
        self.edad = edad
        self.estatura = estatura 
        self.peso = peso 

yeison = Humano(21,1.74, 70)
andres = Humano(15,1.63,64)

print(type(yeison))
print(type(andres))

print('edad de yeison: ',yeison.edad)
print('peso de yeison:',yeison.peso)
print('estatura de yeison:',yeison.estatura)
print('edad de andres:',andres.edad)
print('peso de andres: ',andres.peso)
print('estatura de andres: ',andres.estatura)
