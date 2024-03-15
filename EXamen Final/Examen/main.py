from Interfaz import realizar_venta, reportes_ventas
from Ventas import GestorVentas

def menu_principal():
    print("Menu principal.")
    print("1. Realizar una venta")
    print("2. Reportes de ventas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def main():
    gestor_ventas = GestorVentas()
    while True:
        opcion = menu_principal()
        if opcion == "1":
            realizar_venta(gestor_ventas)
        elif opcion == "2":
            reportes_ventas(gestor_ventas)
        elif opcion == "3":
            break
        else:
            print("Opción incorrecta. Por favor, seleccione una opción .")

if __name__ == "__main__":
    main()