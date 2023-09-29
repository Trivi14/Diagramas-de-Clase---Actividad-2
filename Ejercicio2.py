class Garaje:
    def __init__(self, nombre):
        self.nombre = nombre

class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre

class Reserva:
    def __init__(self, cliente, agencia, fecha_inicio, fecha_final):
        self.cliente = cliente
        self.agencia = agencia
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.coches = []
        self.precio_total = 0
        self.entregado = False

    def agregar_coche(self, coche, precio, litros):
        self.coches.append((coche, precio, litros))
        self.precio_total += precio

    def marcar_entregado(self):
        self.entregado = True

class Cliente:
    def __init__(self, codigo, dni, nombre, direccion, telefono):
        self.codigo = codigo
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

def ingresar_coche():
    matricula = input("Matrícula del coche: ")
    modelo = input("Modelo del coche: ")
    color = input("Color del coche: ")
    marca = input("Marca del coche: ")
    nombre_garaje = input("Nombre del garaje del coche: ")
    
    # Crear una instancia de Garaje con el nombre ingresado
    garaje = Garaje(nombre_garaje)
    
    # Crear una instancia de Coche con la instancia de Garaje
    coche = Coche(matricula, modelo, color, marca, garaje)
    
    return coche

# Función para ingresar datos de un cliente
def ingresar_cliente():
    codigo = input("Código del cliente: ")
    dni = input("DNI del cliente: ")
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    return Cliente(codigo, dni, nombre, direccion, telefono)

# Función para ingresar datos de un coche
def ingresar_coche():
    matricula = input("Matrícula del coche: ")
    modelo = input("Modelo del coche: ")
    color = input("Color del coche: ")
    marca = input("Marca del coche: ")
    garaje = input("Nombre del garaje del coche: ")
    return Coche(matricula, modelo, color, marca, Garaje(garaje))

# Función para ingresar datos de una agencia
def ingresar_agencia():
    nombre = input("Nombre de la agencia: ")
    return Agencia(nombre)

# Función para crear una reserva
def crear_reserva(cliente, agencia, fecha_inicio, fecha_final):
    return Reserva(cliente, agencia, fecha_inicio, fecha_final)

# Función para mostrar información de una reserva
def mostrar_reserva(reserva):
    print("Información de la Reserva:")
    print(f"Cliente: {reserva.cliente.nombre}")
    print(f"Agencia: {reserva.agencia.nombre}")
    print(f"Fecha de Inicio: {reserva.fecha_inicio}")
    print(f"Fecha de Finalización: {reserva.fecha_final}")
    print("Coches Reservados:")
    for coche, precio, litros in reserva.coches:
        print(f"- Matrícula: {coche.matricula}, Precio de Alquiler: ${precio}, Litros de Gasolina: {litros}")
    print(f"Precio Total: ${reserva.precio_total}")
    print(f"Entregado: {'Sí' if reserva.entregado else 'No'}")

# Ejemplo de uso:

# Ingresar datos de cliente, coches, agencia y reserva
cliente1 = ingresar_cliente()
coche1 = ingresar_coche()
coche2 = ingresar_coche()
agencia1 = ingresar_agencia()
fecha_inicio = input("Fecha de inicio de la reserva: ")
fecha_final = input("Fecha de finalización de la reserva: ")

# Crear reserva y agregar coches
reserva1 = crear_reserva(cliente1, agencia1, fecha_inicio, fecha_final)
reserva1.agregar_coche(coche1, 400, 20)
reserva1.agregar_coche(coche2, 500, 25)

# Marcar como entregado
reserva1.marcar_entregado()

# Mostrar información de la reserva
mostrar_reserva(reserva1)
