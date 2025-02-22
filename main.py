OUT_PATH = 'services.txt'

# Cargar servicios desde el archivo
def load_services():
    services = {}
    with open(OUT_PATH, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                name, phone, duration = parts
                services[name] = {
                    'Teléfono Servicio': phone,
                    'Duración Servicio': duration
                }
    return services

# Guardar servicios en el archivo
def save_services(services):
    with open(OUT_PATH, 'w') as file:
        for name, details in services.items():
            file.write(f"{name}|{details['Teléfono Servicio']}|{details['Duración Servicio']}\n")

# CREAR SERVICIO
def create_service():
    services = load_services()
    
    create_arg = input('Escribe el nombre del servicio que quieres crear: ') 
    tel_arg = input('Escribe el número de teléfono del servicio: ')
    duration_arg = input('Escribe la duración del servicio (Formato: horas): ')
    
    services[create_arg] = {
        'Teléfono Servicio': tel_arg,
        'Duración Servicio': duration_arg
    }

    save_services(services)
    print(f'Servicio "{create_arg}" creado exitosamente.')

# ELIMINAR SERVICIO
def del_service():
    services = load_services()

    if not services:
        print("No hay servicios disponibles para eliminar.")
        return

    del_arg = input('Seleccione el nombre del servicio que desea eliminar: ')

    if del_arg in services:
        del services[del_arg]
        save_services(services)
        print(f'Servicio "{del_arg}" eliminado correctamente.')
    else:
        print('Este servicio no existe.')

# LISTAR SERVICIOS
def list_services():
    services = load_services()

    if not services:
        print("No hay servicios disponibles.")
        return

    print("\nLista de servicios disponibles:")
    for name, details in services.items():
        print(f"- {name}: Teléfono: {details['Teléfono Servicio']}, Duración: {details['Duración Servicio']}")

# MENÚ PRINCIPAL
def company_and_client():
    while True:
        print("\nMenú Principal:")
        print("1. Trabajador")
        print("2. Cliente")
        print("3. Salir")
        ask_person = input("Seleccione una opción: ")

        if ask_person == '1':
            while True:
                print("\nMenú Trabajador:")
                print("1. Crear servicio")
                print("2. Eliminar servicio")
                print("3. Listar servicios")
                print("4. Volver al menú principal")
                option = input("Seleccione una opción: ")

                if option == '1':
                    create_service()
                elif option == '2':
                    del_service()
                elif option == '3':
                    list_services()
                elif option == '4':
                    break
                else:
                    print("Opción no válida. Intente nuevamente.")

        elif ask_person == '2':
            list_services()
        
        elif ask_person == '3':
            print("Gracias por su visita. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# EJECUTAR MENÚ
company_and_client()