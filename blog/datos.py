# Perfil del autor (Diccionario anidado)
perfil_autor = {
    "nombre": "Daniel Debasto",
    "bio": "Desarrollador web y creador de contenido sobre programación.",
    "especialidad": "Python y Ciencia de Datos",
    "redes_sociales": ["@daniel_dev", "@daniel_python"],
}

# Estados posibles del post (Tupla)
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas globales del blog (Set)
etiquetas_blog = {"Python", "Django", "DataScience", "Web"}

# Lista de publicaciones (Lista de Diccionarios)
posts = [
    {
        "id": 1,
        "titulo": "Primeros pasos con Python",
        "contenido": "En este post veremos cómo empezar a programar con Python desde cero.",
        "autor": perfil_autor,
        "tags": ["Python", "Principiantes"],
        "estado": estados_post[1],  # "publicado"
    },
    {
        "id": 2,
        "titulo": "Estructuras de datos esenciales",
        "contenido": "Aprende a organizar tu información mediante listas, diccionarios y tuplas.",
        "autor": perfil_autor,
        "tags": ["Python", "DataScience"],
        "estado": estados_post[0],  # "borrador"
    },
    {
        "id": 3,
        "titulo": "Organizando datos con diccionarios",
        "contenido": "Descubre el poder de las estructuras clave-valor en Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Diccionarios"],
        "estado": estados_post[2],  # "archivado"
    },
    {
        "id": 4,
        "titulo": "",  # Título vacío para evaluar validaciones
        "contenido": "Post de prueba con datos incompletos.",
        "autor": None,
        "tags": [],
        "estado": "invalido",
    },
]
