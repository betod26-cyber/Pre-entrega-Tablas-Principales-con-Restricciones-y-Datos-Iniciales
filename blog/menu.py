def mostrar_menu():
    """Muestra el menú del blog actualizado para POO y guarda la opción del usuario."""
    print("\n--- MENU DEL BLOG (PROGRAMACIÓN ORIENTADA A OBJETOS) ---")
    print("1. Listar todos los posts")
    print("2. Buscar post por título")
    print("3. Filtrar posts por tag")
    print("4. Crear un nuevo post (Guardar en JSON)")
    print("5. Salir del sistema")
    entrada = input("Selecciona una opción (1-5): ").strip()
    try:
        return int(entrada)
    except ValueError:
        return -1  # Captura de error controlado para opciones no numéricas

def listar_posts_objetos(lista_posts):
    """Muestra en la consola los atributos directamente desde las instancias de objeto Post."""
    print("\n--- POSTS REGISTRADOS EN EL SISTEMA ---")
    if not lista_posts:
        print("No se encontraron publicaciones almacenadas en el archivo JSON.")
        return
    for post in lista_posts:
        print(f"- ID: {post.id} | Título: {post.titulo} | Autor: {post.autor.nombre} | Estado: {post.estado}")
