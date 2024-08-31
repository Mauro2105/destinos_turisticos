import random

clientes = [{"id":"123","nombre":"Andres Bermudez","email":"mauro@gmail.com"}]
paquetes = [{"id_paquete": "123","destino":"San Andrés","hotel": "Hotel Decameron Isleño","dias": 3,"aerolinea": "Avianca","precio": 500}]
reservas = []

destinos_hoteles = {
    "Cali": ["Hotel Spiwak Chipichape", "Intercontinental", "Hotel NH Cali Royal"],
    "Medellín": ["Hotel Dann Carlton", "The Charlee Hotel", "Hotel Estelar Milla de Oro"],
    "Bogotá": ["Hotel Tequendama", "W Bogota", "Hotel de la Opera"],
    "San Andrés": ["Hotel Decameron Isleño", "Hotel Casablanca", "Hotel Sol Caribe San Andrés"],
    "Cartagena": ["Hotel Charleston Santa Teresa", "Sofitel Legend Santa Clara", "Hotel Movich"],
    "Santa Marta": ["Hotel Zuana Beach Resort", "Irotama Resort", "Hotel Boutique Don Pepe"],
}

aerolinea = ["Latam", "Avianca", "Viva Air"]

def agregarCliente(id, nombre, mail):        
    cliente = {
        "id": id,
        "nombre": nombre,
        "mail": mail
    }
    for c in clientes:
        if c["id"] == id:
            print("Cliente ya existe.")
            return
    clientes.append(cliente)
    print("Registro realizado correctamente.")
    print(clientes)

def buscarCliente(id):
    for cliente in clientes:
        if cliente["id"] == id:
            print(cliente)
            return cliente
    print("Este cliente no existe")

def mostrarOpciones(lista, tipo):
    print(f"Seleccione su {tipo}: ")
    for indice, valor  in enumerate(lista, 1):
        print(f"{indice}. {valor}")
    opcion = int(input(f"Seleccione una opción (1-{len(lista)}): "))
    return lista[opcion - 1]

def crearDestino(id_paquete):
    destino = mostrarOpciones(list(destinos_hoteles.keys()), "destino")
    hotel = mostrarOpciones(destinos_hoteles[destino], "hotel")
    dia = int(input("Cuantos dias se va hospedar: "))
    aerolineas = mostrarOpciones(aerolinea, "aerolínea")
    precio = random.randint(200, 1000)
    
    paquete = {
        "id_paquete": id_paquete,
        "destino": destino,
        "hotel": hotel,
        "dias": dia,
        "aerolinea": aerolineas,
        "precio": precio
    }
    
    paquetes.append(paquete)
    print("Destino creado correctamente")
    print(paquetes)

def buscarPaquete(id_paquete):
    for paquete in paquetes:
        if paquete["id_paquete"] == id_paquete:
            print(paquete)
            return paquete
    print("Este paquete no existe") 

def eliminarPaquete(id_paquete):
    None

def crearReserva(id_reserva, id_cliente, id_paquete):
    cliente = buscarCliente(id_cliente)
    paquete = buscarPaquete(id_paquete)
    
    if cliente and paquete:
        reserva = {
            "id_reserva": id_reserva,
            "cliente": cliente,
            "paquete": paquete
        }
        reservas.append(reserva)
        print("Reserva creada correctamente")
    else:
        print("Cliente o paquete no encontrado")
        
def buscarReserva(id_reserva):
    for reserva in reservas:
        if reserva["id_reserva"] == id_reserva:
            print(reserva)
            return reserva
    print("Este paquete no existe")
    
def menu():
    print("=========Bienvenidos Aereo Aventuras=========")
    print("======= Viaja a tus destinos favoritos=======")
    while True:
        print("\n1). Registrar Cliente\n2). Buscar Cliente\n3). Crear paquete turistico\n4.) Buscar Paquete\n5). Crear Reserva\n6). Buscar Reserva\n7). Salir")
        opcion = int(input("¿Que deseas hacer?\n Selecciona una opció: "))
        
        if opcion == 1 :
            id = input("Ingrese su cedula: ")
            nombre = input("Ingrese su nombre: ")
            mail = input("Ingrese su correo: ")
            agregarCliente(id, nombre, mail)
            
        elif opcion == 2:
            id = input("Ingrese su cedula: ")
            buscarCliente(id)
            
        elif opcion == 3:
            id_paquete = input("Asigne un número de paquete: ")
            crearDestino(id_paquete)
            
        elif opcion == 4:
            id_paquete = input("Ingrese el número del paquete: ")
            buscarPaquete(id_paquete)
            
        elif opcion == 5:
            id_reserva = input("Asigne un número a su reserva: ")
            id_cliente = input("Ingrese su cedula: ")
            id_paquete = input("Ingrese el número de paquete: ")
            crearReserva(id_reserva, id_cliente, id_paquete)
            
        elif opcion == 6:
            id_reserva = input("Ingrese el número de reserva: ")
            buscarReserva(id_reserva)
        elif opcion == 7:
            print("Gracias por visitarnos, Vuelva pronto.\n¡Hasta luego!")
            break
            
        else:
            print("Opción inválida.")

menu()