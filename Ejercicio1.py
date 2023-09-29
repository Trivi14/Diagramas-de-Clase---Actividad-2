class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Sueldo Bruto: ${self.sueldo_bruto:.2f}"


class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

    def mostrar_informacion(self):
        info_empleado = super().mostrar_informacion()
        subordinados_info = "\n".join(sub.mostrar_informacion() for sub in self.subordinados)
        return f"{info_empleado}\nCategoría: {self.categoria}\nSubordinados:\n{subordinados_info}"


class Cliente(Persona):
    def __init__(self, nombre, edad, telefono_contacto):
        super().__init__(nombre, edad)
        self.telefono_contacto = telefono_contacto

    def mostrar_informacion(self):
        return super().mostrar_informacion() + f", Teléfono de Contacto: {self.telefono_contacto}"


empleados = []
clientes = []

def agregar_persona(tipo):
    nombre = input(f"Nombre del {tipo}: ")
    edad = int(input(f"Edad del {tipo}: "))
    
    if tipo == "empleado":
        sueldo_bruto = float(input("Sueldo bruto del empleado: "))
        persona = Empleado(nombre, edad, sueldo_bruto)
        empleados.append(persona)
        print(f"¡{nombre} ha sido registrado como empleado!")
    elif tipo == "directivo":
        sueldo_bruto = float(input("Sueldo bruto del directivo: "))
        categoria = input("Categoría del directivo: ")
        persona = Directivo(nombre, edad, sueldo_bruto, categoria)
        empleados.append(persona)
        print(f"¡{nombre} ha sido registrado como directivo!")
    elif tipo == "cliente":
        telefono_contacto = input("Teléfono de contacto del cliente: ")
        persona = Cliente(nombre, edad, telefono_contacto)
        clientes.append(persona)
        print(f"¡{nombre} ha sido registrado como cliente!")

def mostrar_personas(tipo):
    print(f"\nInformación de {tipo.capitalize()}s:")
    personas = empleados if tipo == "empleado" or tipo == "directivo" else clientes
    for persona in personas:
        print(persona.mostrar_informacion())

while True:
    print("\nMenú Principal:")
    print("1. Añadir Empleado")
    print("2. Añadir Directivo")
    print("3. Añadir Cliente")
    print("4. Ver Empleados")
    print("5. Ver Clientes")
    print("6. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        agregar_persona("empleado")
    elif opcion == "2":
        agregar_persona("directivo")
    elif opcion == "3":
        agregar_persona("cliente")
    elif opcion == "4":
        mostrar_personas("empleado")
    elif opcion == "5":
        mostrar_personas("cliente")
    elif opcion == "6":
        print("¡Hasta luego! ¡Nos Vemos!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
