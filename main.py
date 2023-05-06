from clase import PlanAhorro
import csv


#---------PUNTO 1---------
def leoArchivo():
    archi = open("planes.csv")
    reader = csv.reader(archi, delimiter=";")
    for fila in reader:
        #print(fila)
        unPlan = PlanAhorro()
        unPlan.ingresoDatos(fila)
        print(unPlan)
        lista.append(unPlan)


def menu():
    opcion = -1
    while opcion != 0:
        opcion = listaOpciones()
        match(opcion):
            case 1:
                ##---------PUNTO 2.a---------
                print("----Actualizar precios----")
                actualizarPrecios()
            case 2:
                ##---------PUNTO 2.b---------
                print("----Buscar planes----")
                valorDeCuota = float(input("Ingrese un valor de cuota: "))
                buscoPlanes(valorDeCuota)
            case 3:
                ##---------PUNTO 2.c---------
                print("----Verificar monto pagado para licitar el vehiculo----")
                codigoDelPlan = int(input("Ingrese el codigo del plan del vehiculo: "))
                mostrarMonto(codigoDelPlan)
            case 4:
                ##---------PUNTO 2.d---------
                print("----Modificar cuotas----")
                PlanAhorro.cuotasParaLicitar = int(input("Ingrese la cantidad de cuotas que desea: "))
                for i in range(len(lista)):
                    print(lista[i])
            case 0:
                print("Saliendo...")
        
def listaOpciones():
    print("\n--------MENÚ DE OPCIONES--------")
    print("-1- Actualizar precio del vehiculo para cada plan ")
    print("-2- Buscar planes con valor de cuota inferior a uno ingresado ")
    print("-3- Mostrar monto para licitar vehiculo")
    print("-4- Modificar cuotas")
    print("-0- Salir")
    return int(input("Ingrese opcion: "))


def actualizarPrecios():
    for i in range(len(lista)):
        lista[i].mostrarDatos()
        lista[i].modificarPrecio()

def buscoPlanes(valorDeCuota):
    for i in range(len(lista)):
        precioAuto = lista[i].getPrecio()
        cuotaAuto = ((precioAuto / lista[i].getCantCuotas()) + precioAuto * 0.10)
        if  valorDeCuota < cuotaAuto :
            lista[i].mostrarDatos()
    
def mostrarMonto(codigoDelPlan):
    i=0
    while i < len(lista) and codigoDelPlan != lista[i].getCodigo():
        i +=1
    if i==len(lista):
        print("Codigo ingresado incorrecto")
    elif codigoDelPlan == lista[i].getCodigo():
        precioAuto = lista[i].getPrecio()
        print(f"Debe de haber pagado un total de {lista[i].getCantCuotas()*((precioAuto / lista[i].getCantCuotas()) + precioAuto * 0.10)} pesos")

if __name__ == "__main__":
    lista = []
    leoArchivo()
    #---------PUNTO 2---------
    menu()
        