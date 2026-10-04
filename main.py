from blog.datos import posts
from blog.menu import mostrar_menu, listar_posts
from blog.operaciones import buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_post

def ejecutar_sistema():
    while True:
        opcion = mostrar_menu()
        
        if opcion == 1:
            listar_posts(posts)
            
        elif opcion == 2:
            busqueda = input("\nBuscar por título: ")
            coincidencias = buscar_por_titulo(posts, busqueda)
            print(f"\nResultados encontrados ({len(coincidencias)}):")
            if coincidencias:
                for p in coincidencias:
                    print(f"- {p.get('titulo')} (Estado: {p.get('estado', 'N/A')})")
            else:
                print("No se encontraron publicaciones que coincidan con la búsqueda.")
                
        elif opcion == 3:
            tag = input("\nIngresa el tag a filtrar: ")
            coincidencias = filtrar_por_tag(posts, tag)
            print(f"\nPosts asociados al tag '{tag}' ({len(coincidencias)}):")
            if coincidencias:
                for p in coincidencias:
                    print(f"- {p.get('titulo')}")
            else:
                print(f"No hay publicaciones asociadas al tag '{tag}'.")
                
        elif opcion == 4:
            print("\n--- REVISIÓN DE VALIDACIONES DE NEGOCIO ---")
            for p in posts:
                es_valido, mensaje = validar_post(p)
                estado_texto = "VALIDO" if es_valido else "INVALIDO"
                print(f"ID {p.get('id', 'N/A')}: [{estado_texto}] -> {mensaje}")
                
        elif opcion == 5:
            print("\nGracias por usar el sistema del blog. ¡Hasta luego!")
            break
            
        else:
            print("\nOpción inválida. Por favor, ingresa un número de opción válido (1-5).")

# Bloque protector obligatorio para la ejecución del programa principal
if __name__ == "__main__":
    ejecutar_sistema()
