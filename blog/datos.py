import json
import os
from blog.modelos import Blog, Post, Autor

ARCHIVO_JSON = "posts.json"

def cargar_datos_json():
    """Lee posts.json, convierte los diccionarios en objetos y devuelve una instancia de Blog."""
    instancia_blog = Blog()
    
    # Manejo de archivo inexistente: si no existe, crea un JSON base vacío de forma segura
    if not os.path.exists(ARCHIVO_JSON):
        try:
            with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
                json.dump([], f)
            return instancia_blog
        except IOError:
            print("Error crítico: No se pudo crear el archivo de persistencia inicial.")
            return instancia_blog

    # Intenta leer y deserializar los datos del archivo
    try:
        with open(ARCHIVO_JSON, 'r', encoding='utf-8') as f:
            lista_dicts = json.load(f)
            
            for d in lista_dicts:
                # Reconstruimos el objeto Autor a partir del diccionario anidado
                dict_autor = d.get("autor", {})
                autor_obj = Autor(
                    nombre=dict_autor.get("nombre", "Anónimo"),
                    bio=dict_autor.get("bio", "")
                )
                # Reconstruimos el objeto Post
                post_obj = Post(
                    id_post=d.get("id"),
                    titulo=d.get("titulo", "Sin título"),
                    contenido=d.get("contenido", ""),
                    autor=autor_obj,
                    tags=d.get("tags", []),
                    estado=d.get("estado", "borrador")
                )
                instancia_blog.agregar_post(post_obj)
    except json.JSONDecodeError:
        print("Manejo de Error: El archivo posts.json tiene un formato inválido o está corrupto. Iniciando blog vacío.")
    except PermissionError:
        print("Manejo de Error: No se poseen permisos de lectura sobre posts.json.")
    except Exception as e:
        print(f"Error inesperado al cargar el archivo: {e}")
        
    return instancia_blog


def guardar_datos_json(instancia_blog: Blog):
    """Convierte los objetos Post del Blog a diccionarios y los guarda en posts.json."""
    try:
        # Los objetos se convierten a diccionarios antes de guardarse mediante .to_dict()
        lista_para_guardar = [post.to_dict() for post in instancia_blog.posts]
        
        with open(ARCHIVO_JSON, 'w', encoding='utf-8') as f:
            json.dump(lista_para_guardar, f, ensure_ascii=False, indent=4)
        return True
    except IOError:
        print("Manejo de Error: Falló la escritura física de los datos en posts.json.")
        return False
