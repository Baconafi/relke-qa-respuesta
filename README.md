# 🧪 QA Playwright Challenge – Respuesta

Primero que todo, realicé mis test en Python ya que es el lenguaje que manejo, todavía no se JavaScript (¡pero estoy trabajando en ello!).
Para este desafío realicé mis hojas en POM, trabajando en constructores (donde identifiqué los objetos de la página) y luego haciendo las validaciones de acciones (click, relleno).
Agregué un archivo conftest que corre antes de la ejecución de las pruebas para inicializar una instancia de Playwright y el browser.

Para ejecutar el código hay que instalar requirements.txt donde están las versiones de pytest, playwright y otras liberías que utilicé. Luego se ejecuta en la consola -> pytest -v tests\test_cases\e2e_test.py

Por tiempo solo alcancé a hacer un test validando lo básico solicitado. Este test inicia sesión, navega hacia crear una nueva nota de venta, crea una orden de compra de cajón de manzanas por $595.
En este test se valida que al crear una nota de datos el valor neto + valor IVA sea igual al monto total y este sea mayor a cero. Se valida que el envío de la nota de venta sea exitoso mediante
la verificación de URL de la página siguiente y con el mensaje de éxito "Nota de venta creada correctamente". 
Finalmente se verifica que en el listado de nota de ventas, en la primera fila de la tabla esté el nombre del cliente y el monto total. Luego se cierra la sesión.


Me faltó tiempo para hacer las validaciones negativas y por cada página, por ejemplo ingresar credenciales incorrectas/faltantes, por lo que el mayor desafío fue el tiempo y además no poder entregar
el código en JS.
