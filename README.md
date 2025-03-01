# Explicación del Código

Este código es un sistema básico para gestionar servicios. Permite a los trabajadores crear, eliminar y listar servicios, y a los clientes ver la lista de servicios disponibles. Todo se almacena en un archivo de texto (`services.txt`).

## ¿Cómo funciona?

El código funciona a través de varias funciones:

### 1. `load_services()`
Carga los servicios desde el archivo `services.txt`. Cada línea del archivo contiene un servicio con su nombre, teléfono y duración, separados por `|`. Devuelve un diccionario con esta información.

### 2. `save_services(services)`
Guarda los servicios en `services.txt`, escribiendo cada servicio en una línea con el formato `nombre|teléfono|duración`.

### 3. `create_service()`
Solicita al usuario ingresar un nuevo servicio, su teléfono y su duración. Luego, lo añade a la lista y lo guarda en el archivo.

### 4. `del_service()`
Permite al usuario eliminar un servicio de la lista. Si el servicio existe, se borra y se guarda la nueva lista sin ese servicio.

### 5. `list_services()`
Muestra todos los servicios disponibles, leyendo los datos del archivo y formateándolos de manera legible.

### 6. `company_and_client()`
Es el menú principal del programa. Permite al usuario elegir entre:

- **Trabajador:** Puede crear, eliminar o listar servicios.
- **Cliente:** Puede ver la lista de servicios.
- **Salir:** Termina el programa.

## Componentes del grupo
- **Jose Carballeda**
- **Daniele Dettori**