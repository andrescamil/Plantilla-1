class persona():
    def __init__(self, name):
        self.nombre = name
        
    def caminar (self):
        print("estoy caminando",self.nombre)
        
    def comer(self,comida):
        print("estoy comiendo",comida)
    def saltar(self):
        print(self.nombre ,"esta saltando")
    def correr(self):
        print(self.nombre ,"esta corriendo")
        
        
admin = persona("Lorena")
estudiante01 = persona("Carlos")
profesorMat = persona("Francisco")

profesorMat.caminar()
estudiante01.comer("pescado")
admin.caminar()

admin.saltar()
admin.comer("arroz")
estudiante01.correr()


