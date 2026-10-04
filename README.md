# Sistema de Gestión de Blog Modularizado

Este proyecto implementa una solución de consola interactiva para la gestión interna de publicaciones, autores y estados de un blog personal, refactorizada bajo una arquitectura orientada a paquetes modulares.

## 📁 Distribución del Entorno y Archivos
El código de software se divide siguiendo el principio de separación de responsabilidades:
- **`main.py`**: Orquestador principal que centraliza el flujo de control bajo condiciones de ejecución segura.
- **`blog/datos.py`**: Base de almacenamiento estático que define colecciones, diccionarios de posts y metadatos de autoría.
- **`blog/validaciones.py`**: Motor lógico a cargo de auditar la integridad de estructuras de datos según las reglas de negocio.
- **`blog/operaciones.py`**: Módulo algorítmico encargado de resolver búsquedas e indexaciones insensibles a mayúsculas/minúsculas.
- **`blog/menu.py`**: Interfaz de terminal orientada a la visualización y captura segura de flujos de interacción.

## 🚀 Guía de Uso del Sistema
Para correr el software localmente, abre una terminal de comandos posicionada en la carpeta raíz del proyecto y ejecuta:

```bash
python main.py
```

### Funcionalidades disponibles:
1. **Ver todos los posts**: Renderiza un listado filtrando los posts completos de los incompletos.
2. **Buscar por título**: Devuelve ocurrencias de textos parciales ingresados por el operador.
3. **Filtrar por tag**: Busca coincidencias semánticas entre las etiquetas asociadas.
4. **Validar publicaciones**: Genera reportes lógicos sobre fallas de campos o ausencias de datos en posts.
5. **Salir**: Desactiva el ciclo principal del entorno de comandos.
