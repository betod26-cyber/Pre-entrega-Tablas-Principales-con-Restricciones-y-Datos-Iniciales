def buscar_por_titulo(lista_posts, termino):
    """Filtra y retorna las publicaciones cuyo título coincida con el término buscado."""
    termino_busqueda = termino.strip().lower()
    resultados = []
    for post in lista_posts:
        titulo_post = post.get("titulo", "").lower()
        if termino_busqueda in titulo_post:
            resultados.append(post)
    return resultados

def filtrar_por_tag(lista_posts, tag_buscado):
    """Filtra y retorna las publicaciones asociadas a una etiqueta (case-insensitive)."""
    tag_limpio = tag_buscado.strip().lower()
    resultados = []
    for post in lista_posts:
        tags = post.get("tags", [])
        tags_en_minuscula = [str(t).lower() for t in tags]
        if tag_limpio in tags_en_minuscula:
            resultados.append(post)
    return resultados
