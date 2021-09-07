# Experiencia 1 - Laboratorio de Control Automático 🏭
Profesor: David Acuña\
Sigla: IEE2683-1\
Fecha: 07-09-2021 (2021-2)

## Integrantes
- Elena Contardo
- Pamela Romero
- Francisco Fonseca

## Tareas Futuras
### TO DO!!
- [ ] Buffer circular con tecla G con RAM.
- [ ] Anti-Wind-up sobre parte integral.
- [ ] Tunear controles.

### Cosas listas!!
- [x] Hilos paralelos de interfaz para aumentar refresco.
- [x] Terminar graficos.

## Correr Código
1) Correr primero [`correr_todo.bat`](correr_todo.bat)
2) Posteriormente correr  el archivo [`experiencia.py`](experiencia.py)

## Estilo de código
Se usó [PEP8](https://www.python.org/dev/peps/pep-0008/) para el estilo. Ambiente de programación en Sublime Text y VSCode Gang. 😎

## Funcionalidad de archivos programados
PD : Click sobre el archivo para redirigirse
- [`experiencia.py`](experiencia.py): Archivo principal. Contiene threads que gatillan refrescos de interfaz y del control
- [`parametros.py`](parametros.py): Parametros que pueden ser de utilidad para cambiar, hasta el momento contiene parametros de refresco.
- [`globals.py`](globals.py): Solamente contiene definición de variables globales. Necesario para uso del handler.
- [`handler.py`](handler.py): Contiene las funciones que reciben información actual del estado de los estanques.
- [`util.py`](util.py): Contiene las funciones :`eventos()` para los eventos en la interfaz y función `obtener()` para forzar una primera recopilación de datos.
- [`interfaz.py`](interfaz.py): Contiene entidades de la interfaz, como los estanques, los gráficos y textBox de constantes.
- [`control.py`](control.py): Tiene por objetivo llevar a cabo el control del sistema completo.

## Librería
- [`cliente.py`](Libreria/cliente.py): Contiene entidad de cliente a conectarse por protocolo OPC. Este se usa en el código propio.

- [`QuadrupleTank.py`](Libreria/QuadrupleTank.py): Contiene entidad y codigo para conectarse al servidor OPC y emular sistema de tanques. *(Este archivo se corre en [`correr_todo.bat`](correr_todo.bat))*

- [`ServidorOPC.py`](Libreria/ServidorOPC.py): Contiene el mismo servidor *(Este archivo se corre en [`correr_todo.bat`](correr_todo.bat))*

- [`TanquesNamespace.py`](Libreria/TanquesNamespace.py): Contiene estructura de datos a ser usado en el servidor OPC.

## Librerias descargables
- `pygame`
- Hasta el momento serían todos.
