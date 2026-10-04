from blog.datos import estados_post

def validar_post(post):
    """Valida las reglas de negocio de una publicación y retorna True/False junto con el motivo."""
    titulo = post.get("titulo", "").strip()
    contenido = post.get("contenido", "").strip()
    autor = post.get("autor")
    estado = post.get("estado")
    
    if not titulo:
        return False, "El título está vacío o ausente."
    if not contenido:
        return False, "El contenido está vacío o ausente."
    if not isinstance(autor, dict) or "nombre" not in autor:
        return False, "El autor debe ser un diccionario válido con 'nombre'."
    if estado not in estados_post:
        return False, f"El estado '{estado}' no forma parte de {estados_post}."
    
    return True, "Publicación válida."
