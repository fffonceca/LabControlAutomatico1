# Experiencia 1 - Laboratorio de Control Automático 🏭
Profesor: David Acuña\
Sigla: IEE2683-1\
Fecha: 08-09-2021 (2021-2)

## Integrantes
- Elena Contardo
- Pamela Romero
- Francisco Fonseca

## Correr Código
1) Correr primero [`correr_todo.bat`](correr_todo.bat)
2) Posteriormente correr  el archivo [`experiencia.py`](experiencia.py)

## Estilo de código
Se usó [PEP8](https://www.python.org/dev/peps/pep-0008/) para el estilo. Ambiente de programación en Sublime Text y VSCode Gang. 😎

## Funcionalidad de archivos programados
PD : Click sobre el archivo para redirigirse
- [`experiencia.py`](experiencia.py): Archivo principal. Contiene threads que gatillan refrescos de interfaz y actualización de control.
- [`parametros.py`](parametros.py): Parametros que pueden ser de utilidad para cambiar, contiene parametros de refresco de imagen, actualizacion de control y parametros iniciales varios. 
- [`globals.py`](globals.py): Solamente contiene definición de variables globales. Necesario para uso del handler.
- [`handler.py`](handler.py): Contiene las funciones que reciben información actual del estado de los estanques.
- [`util.py`](util.py): Contiene las funciones :`eventos()` para los eventos en la interfaz y función `obtener()` para forzar una primera recopilación de datos. Además, contiene la entidad *BufferCircular* que carga sobre un arreglo circular estructuras tipo *Estructuras* para cargar datos.
- [`interfaz.py`](interfaz.py): Contiene entidades de la interfaz, como los estanques, los gráficos y textBox de constantes.
- [`control.py`](control.py): Tiene por objetivo llevar a cabo el control del sistema completo, además filtra alguno de los inputs del usuario.

## Librería
- [`cliente.py`](Libreria/cliente.py): Contiene entidad de cliente a conectarse por protocolo OPC. Este se usa en el código propio.

- [`QuadrupleTank.py`](Libreria/QuadrupleTank.py): Contiene entidad y codigo para conectarse al servidor OPC y emular sistema de tanques. *(Este archivo se corre en [`correr_todo.bat`](correr_todo.bat))*

- [`ServidorOPC.py`](Libreria/ServidorOPC.py): Contiene el mismo servidor *(Este archivo se corre en [`correr_todo.bat`](correr_todo.bat))*

- [`TanquesNamespace.py`](Libreria/TanquesNamespace.py): Contiene estructura de datos a ser usado en el servidor OPC.

## Librerias descargables
- `pygame`: Correr en consola `pip install pygame`
