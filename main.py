from blog.datos import cargar_datos_json, guardar_datos_json
from blog.menu import mostrar_menu, listar_posts_objetos
from blog.modelos import Post, Autor

def ejecutar_sistema():
    # Instanciamos la clase Blog cargando los datos persistidos desde el JSON al iniciar
    mi_blog = cargar_datos_json()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            # Lista los posts pasando la lista de objetos de la instancia del blog
            listar_posts_objetos(mi_blog.posts)
            
        elif opcion == 2:
            busqueda = input("\nIngresa el título o frase a buscar: ")
            coincidencias = mi_blog.buscar_por_titulo(busqueda)
            print(f"\nResultados de búsqueda ({len(coincidencias)}):")
            if coincidencias:
                for p in coincidencias:
                    print(f"- {p.titulo} | Autor: {p.autor.nombre} | Estado: {p.estado}")
            else:
                print("No se localizaron títulos que coincidan con la búsqueda.")
                
        elif opcion == 3:
            tag = input("\nIngresa la etiqueta (tag) a filtrar: ")
            coincidencias = mi_blog.filtrar_por_tag(tag)
            print(f"\nPublicaciones bajo la etiqueta '{tag}' ({len(coincidencias)}):")
            if coincidencias:
                for p in coincidencias:
                    print(f"- {p.titulo} (ID: {p.id})")
            else:
                print(f"No hay registros categorizados con el tag '{tag}'.")
                
        elif opcion == 4:
            print("\n--- CREACIÓN DE NUEVA PUBLICACIÓN EN TIEMPO REAL ---")
            titulo = input("Título del post: ").strip()
            contenido = input("Contenido de la nota: ").strip()
            nombre_autor = input("Nombre del Autor: ").strip()
            bio_autor = input("Biografía corta del Autor: ").strip()
            tags_input = input("Tags (escríbelos separados por comas): ")
            
            # Limpieza y filtrado básico de los tags ingresados
            tags = [t.strip() for t in tags_input.split(",") if t.strip()]
            estado = input("Estado (borrador / publicado / archivado): ").strip().lower()
            
            # Validaciones básicas de campos vacíos en consola
            if not titulo or not contenido or not nombre_autor:
                print("\n❌ Error: Título, Contenido y Nombre de Autor son obligatorios. Registro cancelado.")
                continue
            
            # Generación de identificador incremental basado en el tamaño actual de la lista
            nuevo_id = len(mi_blog.posts) + 1
            
            # Instanciamos la clase Autor y la inyectamos dentro de la nueva instancia de Post
            autor_instancia = Autor(nombre_autor, bio_autor)
            nuevo_post = Post(nuevo_id, titulo, contenido, autor_instancia, tags, estado)
            
            # Agregamos el objeto a nuestra instancia centralizada de Blog
            mi_blog.agregar_post(nuevo_post)
            
            # Guardamos la colección actualizada convirtiéndola en JSON plano de forma inmediata
            if guardar_datos_json(mi_blog):
                print(f"\n✅ ¡Éxito! El post '{titulo}' fue serializado y almacenado en posts.json.")
                
        elif opcion == 5:
            print("\nCerrando flujos y resguardando base de datos. ¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Introduce un valor numérico correcto (1 al 5).")

# Uso estricto del bloque condicional obligatorio de arranque
if __name__ == "__main__":
    ejecutar_sistema()
