

class PlanAhorro:
    #estas dos ultimas al no tener decoradores y estar inicializada, SON ESTATICAS
    cantCuotas = 60
    cuotasParaLicitar = 10
    __codigoPlan = 0
    __modeloAuto = ""
    __versionAuto = ""
    __precioAuto = 0.0
    

    def __init__(self, codigoPlan=0, modeloAuto= "", versionAuto = "", precioAuto = 0):
        self.__codigoPlan = codigoPlan
        self.__modeloAuto = modeloAuto
        self.__versionAuto = versionAuto
        self.__precioAuto = precioAuto

    def ingresoDatos(self, fila):
        self.__codigoPlan = int(fila[0])
        self.__modeloAuto = fila[1]
        self.__versionAuto = fila[2]
        self.__precioAuto = float(fila[3])

    def __str__(self):
        #Precio: {self.__precioAuto}|| Cuotas: {self.cantCuotas}|| Cant cuotas pagas para licitar: {self.cuotasParaLicitar}
        return f"Codigo: {self.__codigoPlan}|| Modelo: {self.__modeloAuto}|| Version: {self.__versionAuto}|| Precio: {self.__precioAuto}|| Cuotas: {self.cantCuotas}|| Cant cuotas pagas para licitar: {self.cuotasParaLicitar}"
    
    def modificarPrecio(self):
        self.__precioAuto = float(input("Ingrese nuevo precio del vehiculo: "))


    def mostrarDatos(self):
        print(f"Codigo: {self.__codigoPlan}|| Modelo: {self.__modeloAuto}|| Version: {self.__versionAuto}||")

    def getPrecio(self):
        return float(self.__precioAuto)
    
    def getCantCuotas(cls):
        return cls.cantCuotas
    
    def getCodigo(self):
        return self.__codigoPlan
    
    def getCantCuotas(cls):
        return cls.cantCuotas
    
