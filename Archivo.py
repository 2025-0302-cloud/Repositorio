print("Validacion de contraseña")

Contraseñacorrecta = "20250302"
Nombredeusuario = input("Introduce tu nombre de usuario: ")
Contraseña = input("Introduce la contraseña: ")

if Contraseña == Contraseñacorrecta:
    print("Bienvenido, ", Nombredeusuario)

else:
    print("Contraseña incorrecta, intente de nuevo")