# 🧪 QA Playwright Challenge – Relke

¡Bienvenido/a! Este es el desafío técnico para el proceso de selección de **QA Engineer Junior** en Relke 🚀

---

## 🤔 ¿Qué buscamos?

En Relke creemos en el crecimiento desde el aprendizaje. Este desafío no busca medir cuántos años de experiencia tienes, sino **cómo aplicas tus conocimientos actuales, tu motivación por aprender y tu capacidad para enfrentar un flujo real de automatización**.

> 🧩 **No es excluyente si tienes menos de 1 año de experiencia.** Si estás recién egresado/a o en tus primeras experiencias laborales, ¡también puedes participar!

Lo importante es que, con tu formación académica y dedicación, **puedas resolver este reto en un tiempo realista (48 horas)** y mostrar cómo piensas como QA.

---

## 🎯 Desafío

Tu misión es automatizar con Playwright el flujo de **creación de una Nota de Venta** en nuestro sistema demo:

- 🌐 URL: [https://demo.relbase.cl](https://demo.relbase.cl)
- 👤 Usuario: `qa_junior@relke.cl`
- 🔐 Contraseña: `Demo123456!`

### Pasos mínimos esperados

1. Iniciar sesión
2. Ir a **Ventas > Notas de Venta**
3. Hacer clic en **Crear nueva nota**
4. Completar los datos mínimos:
   - Seleccionar sucursal (Casa matriz)
   - Seleccionar bodega (Principal)
   - Seleccionar un cliente (⚠️ puede variar el nombre)
   - Seleccionar moneda (Pesos)
   - Agregar al menos un producto
   - Validar que se calcula un total
5. Guardar y verificar que aparece en el listado con el total correcto

---

## 💡 Reglas y condiciones especiales

- El total debe ser **mayor a $0** y reflejar el precio del producto agregado.
- Evita usar esperas estáticas (`waitForTimeout`). Usa selectores confiables y `await expect(...)`.
- Puedes usar Page Object Model si lo prefieres, pero no es obligatorio.

---

## 📤 ¿Cómo entregar tu prueba en GitHub?

Como el repositorio original de Relke en Bitbucket es público pero de solo lectura, te pedimos que:

1. Clones este repo:
   ```bash
   git clone https://bitbucket.org/relke/relke-qa-challenge.git
   cd relke-qa-challenge
   ```

2. Crees un nuevo repositorio en **tu cuenta personal de GitHub** (puede ser público o privado).

3. Cambies el origen remoto en tu entorno local:
   ```bash
   git remote remove origin
   git remote add origin https://github.com/tu_usuario/relke-qa-respuesta.git
   git push -u origin main
   ```
4. Agrega tus pruebas automatizadas dentro de la carpeta `tests/`

5. Crea un `README` dentro de tu repositorio explicando:
   - Cómo ejecutar tu test
   - Qué validaciones hiciste
   - Qué desafíos tuviste o decisiones tomaste

6. Haz commit y push 

7. Comparte el link del repositorio (y acceso si es privado) por mensaje de Get on board de la postulación

> Si no tienes cuenta en GitHub, puedes crear una gratuita en https://github.com

---

## 📽️ Opcional: muestra tu forma de trabajar

Si quieres destacarte, puedes grabar un video (máx 10 min) mostrando cómo trabajaste el desafío: tus pasos, pruebas, validaciones o errores encontrados.

---

## 🧩 Bonus (opcional)

Puedes agregar validaciones extra como:

- Prueba negativa: ¿qué pasa si no agrego productos?
- Validación de error de campo requerido
- Automatización de logout o expiración de sesión

---

## ⏱️ Tiempo estimado

Tienes **48 horas** desde que recibes esta pauta.

---

## 🧠 Consejos

- Usa `npx playwright codegen` si necesitas inspiración, pero asegúrate de entender y limpiar el código generado.
- Lee los selectores con cuidado. A veces un texto cambia según el estado.
- Escribe como si tu test fuera a mantenerse en producción.
- No estamos buscando perfección, sino **compromiso, criterio y capacidad de automatizar flujos funcionales reales**.

---

¡Mucho éxito! 💥  
Relke QA Team

# relke-qa-respuesta