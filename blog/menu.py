from blog.validaciones import validar_post

def mostrar_menu():
    """Muestra las opciones del menú y captura la selección manejando excepciones."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar publicaciones")
    print("5. Salir")
    entrada = input("Selecciona una opción (1-5): ").strip()
    try:
        return int(entrada)
    except ValueError:
        return -1

def listar_posts(lista_posts):
    """Recorre y muestra en consola la lista de posts de manera formateada."""
    print("\n--- POSTS DISPONIBLES ---")
    if not lista_posts:
        print("No hay publicaciones para mostrar.")
        return
    for post in lista_posts:
        es_valido, _ = validar_post(post)
        if es_valido:
            nombre_autor = post.get("autor", {}).get("nombre", "Desconocido")
            print(f"- [{post.get('id')}] {post.get('titulo')} | Autor: {nombre_autor} | Estado: {post.get('estado')}")
        else:
            print(f"- [{post.get('id', 'N/A')}] (Post Incompleto / Inválido: '{post.get('titulo', 'Sin título')}')")
