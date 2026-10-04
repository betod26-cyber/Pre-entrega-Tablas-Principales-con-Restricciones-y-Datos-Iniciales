# Sistema de Gestión de Blog - Arquitectura Orientada a Objetos y Persistencia JSON

Este proyecto representa una evolución del sistema de blog por consola, migrando de un diseño estructurado hacia el paradigma de **Programación Orientada a Objetos (POO)** e integrando persistencia real de datos mediante archivos planos de texto en formato JSON.

## 🚀 Arquitectura de Clases e Interacción Lógica
El diseño interno de la lógica en `blog/modelos.py` se compone por tres entidades fundamentales:
1. **`Autor`**: Modela al creador del post mediante atributos de identidad y biografía.
2. **`Post`**: Representa la estructura de una publicación, la cual recibe de forma obligatoria una instancia del objeto `Autor` para establecer una relación de composición anidada.
3. **`Blog`**: Objeto centralizador que almacena una lista dinámica de objetos `Post`. Expone los métodos de negocio encargados de listar, buscar y filtrar elementos aplicando conversión a minúsculas (`.lower()`) para garantizar consultas estables (insensibles a mayúsculas).

## 💾 Mecanismo de Persistencia y Serialización JSON
Para evitar la pérdida de información al cerrar el programa, el sistema se comunica de manera bidireccional con el archivo físico `posts.json` mediante las siguientes operaciones en `blog/datos.py`:
- **Carga inicial**: Al arrancar `main.py`, el sistema lee los diccionarios de `posts.json` y mapea sus claves para reconstruirlos en instancias de objetos vivas dentro de la memoria de Python.
- **Guardado**: Al dar de alta una nueva entrada (Opción 4), los métodos internos de las clases ejecutan `.to_dict()` convirtiendo los objetos y sus dependencias anidadas de vuelta en diccionarios estándar, permitiendo que el módulo `json` los grabe físicamente en el disco.
- **Manejo de Errores**: El código implementa control preventivo ante archivos corruptos, ausencias de documentos o problemas de permisos de sistema a través de bloques estructurados de captura `try-except`.

## 🏃‍♂️ Instrucciones de Uso
Para ejecutar y probar la persistencia del sistema, abre una terminal en la carpeta raíz y corre:
```bash
python main.py
```





## 🗄️ Módulo Base de Datos: Proyecto Retail (SQL)

Se incorporó el diseño relacional para el ecosistema del proyecto bajo la base de datos `retail_project`.

### Estructura del Script (`script_retail.sql`):
- **DDL (Estructura)**: Creación de tablas integradas (`clientes`, `productos`, `ventas`) utilizando restricciones de clave primaria y claves foráneas (`FOREIGN KEY`) para resguardar la consistencia de los datos.
- **Restricciones CHECK**:
  1. `chk_edad_cliente`: Garantiza que los compradores tengan entre 18 y 120 años.
  2. `chk_precio_positivo`: Evita que existan productos con precios en cero o negativos.
  3. `chk_cantidad_vendida`: Asegura que toda transacción registre al menos una unidad.
- **Transaccionalidad (ACID)**: El proceso de carga masiva de datos está protegido mediante un bloque `BEGIN; ... COMMIT;` para mitigar cargas incompletas en caso de fallas.
- **Sentencias DML**: Aplicación de actualizaciones masivas por categorías (`UPDATE`) y remoción de registros individuales (`DELETE`) mediante el uso preciso de cláusulas `WHERE`.
