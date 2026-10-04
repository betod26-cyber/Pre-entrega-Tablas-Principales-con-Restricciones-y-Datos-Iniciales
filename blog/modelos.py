class Autor:
    def __init__(self, nombre, bio):
        self.nombre = nombre
        self.bio = bio

    def to_dict(self):
        """Convierte el objeto Autor a diccionario para almacenamiento JSON."""
        return {
            "nombre": self.nombre,
            "bio": self.bio
        }


class Post:
    def __init__(self, id_post, titulo, contenido, autor: Autor, tags, estado):
        self.id = id_post
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor  # Recibe una instancia de la clase Autor
        self.tags = tags
        self.estado = estado

    def to_dict(self):
        """Convierte el objeto Post a un diccionario plano compatible con JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),  # Serializa el objeto anidado Autor
            "tags": self.tags,
            "estado": self.estado
        }


class Blog:
    def __init__(self):
        self.posts = []  # Lista que almacena exclusivamente objetos Post

    def agregar_post(self, post: Post):
        """Añade un objeto Post a la colección central."""
        self.posts.append(post)

    def buscar_por_titulo(self, termino):
        """Centraliza la búsqueda por título ignorando mayúsculas y minúsculas."""
        termino_limpio = termino.strip().lower()
        return [p for p in self.posts if termino_limpio in p.titulo.lower()]

    def filtrar_por_tag(self, tag_buscado):
        """Centraliza el filtrado por etiquetas ignorando mayúsculas y minúsculas."""
        tag_limpio = tag_buscado.strip().lower()
        resultados = []
        for post in self.posts:
            # Convierte todos los tags del post a minúsculas de forma segura
            tags_minuscula = [str(t).lower() for t in post.tags]
            if tag_limpio in tags_minuscula:
                resultados.append(post)
        return resultados
