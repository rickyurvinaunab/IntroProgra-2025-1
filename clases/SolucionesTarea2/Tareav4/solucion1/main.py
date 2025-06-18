from utilidades import pedir_entero
from gestion.gestion_libros import registrar_prestamo, mostrar_libros_disponibles, mostrar_libros_prestados, \
    registrar_nuevo_libro, registrar_devolucion, mostrar_libros_prestados_por_rut
from gestion.gestion_personas import mostrar_personas, registrar_pago, agregar_o_actualizar_persona
import gestion.deudas as grafico_deudas
from gestion.grafico import mostrar_grafico_montos
from gestion.autenticacion import registrar_usuario, login_usuario

usuario_logueado = None # Variable global para almacenar el usuario que ha iniciado sesion


def mostrar_menu_principal():
    """
    Muestra el menu inicial de Login o Registro para el usuario.
    """
    print("\n===== BIBLIOTECA - INICIO =====")
    print("1. Iniciar Sesion")
    print("2. Registrarse como nuevo usuario")
    print("3. Salir del programa")


def mostrar_menu_usuario():
    """
    Muestra el menu de opciones disponibles para un usuario normal (cliente).
    """
    print("\n===== MENU DE USUARIO =====")
    print("1. Pedir prestamo de libro")
    print("2. Ver libros disponibles")
    print("3. Ver libros prestados (mis prestamos)")
    print("4. Ver mi perfil")
    print("5. Devolver un libro")
    print("6. Registrar pago de deuda")
    print("7. Ver mi estado de deuda y pagos (grafico)")
    print("8. Cerrar Sesion")


def mostrar_menu_administrador():
    """
    Muestra el menu de opciones disponibles para un administrador.
    """
    print("\n===== MENU DE ADMINISTRADOR =====")
    print("1. Registrar un nuevo libro")
    print("2. Registrar un prestamo (para cualquier usuario)")
    print("3. Ver libros disponibles")
    print("4. Ver libros prestados (todos)")
    print("5. Ver personas registradas (todos los usuarios)")
    print("6. Ver grafico de montos pagados acumulados (general)")
    print("7. Devolver un libro (de cualquier usuario)")
    print("8. Registrar pago de deuda (de cualquier usuario)")
    print("9. Ver grafico de deudas pendientes (general)")
    print("10. Gestionar usuarios/roles (agregar/actualizar persona)")
    print("11. Ver estado de deuda y pagos (grafico de persona)")
    print("12. Cerrar Sesion")


def main():
    """
    Funcion principal del programa de gestion de biblioteca.

    Maneja el flujo de la aplicacion, incluyendo el login de usuarios,
    el registro y la presentacion de menus diferenciados para usuarios
    normales y administradores, asi como la ejecucion de las funciones
    correspondientes a cada opcion.
    """
    global usuario_logueado # Declara que se usara la variable global usuario_logueado

    while True: # Bucle principal del programa
        if usuario_logueado is None: # Si no hay ningun usuario logueado
            mostrar_menu_principal() # Muestra el menu de inicio de sesion/registro
            opcion_inicio = pedir_entero("Elige una opcion: ") # Solicita la opcion al usuario

            if opcion_inicio == 1: # Opcion "Iniciar Sesion"
                usuario_logueado = login_usuario() # Intenta loguear al usuario
            elif opcion_inicio == 2: # Opcion "Registrarse"
                registrar_usuario() # Llama a la funcion de registro de usuario
            elif opcion_inicio == 3: # Opcion "Salir"
                print("Saliendo del programa...")
                break # Sale del bucle y termina el programa
            else: # Opcion invalida
                print("Opcion no valida. Intenta nuevamente.")

        else: # Si hay un usuario logueado
            if usuario_logueado.es_admin: # Si el usuario logueado es administrador
                mostrar_menu_administrador() # Muestra el menu de administrador
                opcion = pedir_entero("Elige una opcion de administrador: ") # Solicita la opcion

                if opcion == 1: # Registrar nuevo libro
                    registrar_nuevo_libro()
                elif opcion == 2: # Registrar prestamo (para cualquier usuario)
                    registrar_prestamo()
                elif opcion == 3: # Ver libros disponibles
                    mostrar_libros_disponibles()
                elif opcion == 4: # Ver libros prestados (todos)
                    mostrar_libros_prestados()
                elif opcion == 5: # Ver personas registradas (todos)
                    mostrar_personas()
                elif opcion == 6: # Ver grafico de montos pagados (general)
                    mostrar_grafico_montos()
                elif opcion == 7: # Devolver un libro (de cualquier usuario)
                    registrar_devolucion()
                elif opcion == 8: # Registrar pago de deuda (de cualquier usuario)
                    registrar_pago()
                elif opcion == 9: # Ver grafico de deudas pendientes (general)
                    grafico_deudas.mostrar_grafico_deudas()
                elif opcion == 10: # Gestionar usuarios/roles (agregar/actualizar persona)
                    agregar_o_actualizar_persona()
                elif opcion == 11: # Ver estado de deuda y pagos (grafico de persona)
                    grafico_deudas.mostrar_grafico_deuda_pagado_por_usuario() # Admin puede ver de cualquiera, pedira RUT
                elif opcion == 12: # Cerrar sesion
                    print("Cerrando sesion de " + usuario_logueado.username + "...")
                    usuario_logueado = None # Restablece la variable de usuario logueado a None
                else: # Opcion invalida
                    print("Opcion no valida. Intenta nuevamente.")

            else:  # Si es un usuario normal (no administrador)
                mostrar_menu_usuario() # Muestra el menu de usuario normal
                opcion = pedir_entero("Elige una opcion de usuario: ") # Solicita la opcion

                if opcion == 1: # Pedir prestamo de libro
                    registrar_prestamo(rut_logueado_opcional=usuario_logueado.rut) # Pasa el RUT del usuario logueado
                elif opcion == 2: # Ver libros disponibles
                    mostrar_libros_disponibles()
                elif opcion == 3: # Ver mis libros prestados
                    mostrar_libros_prestados_por_rut(usuario_logueado.rut)
                elif opcion == 4: # Ver mi perfil
                    print("\n--- Mi Perfil ---")
                    usuario_logueado.mostrar_info() # Muestra la informacion del perfil del usuario logueado
                elif opcion == 5: # Devolver un libro
                    registrar_devolucion()
                elif opcion == 6: # Registrar pago de deuda
                    registrar_pago()
                elif opcion == 7: # Ver mi estado de deuda y pagos (grafico)
                    grafico_deudas.mostrar_grafico_deuda_pagado_por_usuario(rut_a_graficar=usuario_logueado.rut) # Muestra el grafico para el usuario logueado
                elif opcion == 8: # Cerrar sesion
                    print("Cerrando sesion de " + usuario_logueado.username + "...")
                    usuario_logueado = None # Restablece la variable de usuario logueado a None
                else: # Opcion invalida
                    print("Opcion no valida. Intenta nuevamente.")


main() # Llama a la funcion principal para iniciar el programa