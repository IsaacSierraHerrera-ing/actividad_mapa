class Usuario:
    def __init__(self, nombre, nickname, clave, tipo, fecha_creacion):
        self.datos = {
       'nombre': nombre,
       'nickname': nickname,
       'clave': clave,
        'tipo': tipo,
       'fecha_creacion': fecha_creacion }


    def imprimir_datos(self):
        return ', '.join([f"{key} = {value}" for key, value in self.datos.items()])

    def buscar(self, valorbuscar):
        for key, value in self.datos.items():
            if value == valorbuscar:
                return key, value
        return None, None

    def eliminar(self, valoreliminar):
        for key, value in self.datos.items():
            if value == valoreliminar:
                del self.datos[key]  
                return key, value
        return None, None


usuarios = {}

def agregar_usuario():
    print("Agregar Usuario")
    nombre = input("Nombre completo: ")
    nickname = input("Nickname: ")
    clave = input("Clave: ")
    tipo = input("Tipo: ")
    fecha_creacion = input("Fecha de creación: ")

    usuario = Usuario(nombre, nickname, clave, tipo, fecha_creacion)
    usuarios[nickname] = usuario
    print(f"Usuario '{nickname}' agregado")

def buscar_usuario():
    print("Buscar Usuario")
    valorbuscar = input("Ingrese el nickname, el tipo, la clave o el nombre para eliminar el usuario: ")
    
    for usuario in usuarios.values():
        key, value = usuario.buscar(valorbuscar)
        if value is not None:
            print(f"Usuario encontrado:\n{usuario.imprimir_datos()}")
            return
    print("Usuario no existe")

def eliminar_usuario():
    print("Eliminar Usuario")
    valorbuscar = input("Ingrese el nickname, el tipo, la clave o el nombre para eliminar el usuario: ")

    for nickname, usuario in list(usuarios.items()): 
        key, value = usuario.eliminar(valorbuscar)
        if value is not None:
            del usuarios[nickname]
            print(f"Usuario con {key} '{value}' eliminado.")
            return
    print("Usuario no existe")

def menu():
    while True:
        print("     Menú   ")
        print("1. Agregar Usuario")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_usuario()
        elif opcion == '2':
            buscar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            print("Fin :)")
            break

menu()


