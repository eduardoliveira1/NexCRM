from .models import Empresa

def get_empresa_logada(request):
    empresa_logada_id = request.session.get('empresa_logada_id')
    if empresa_logada_id:
        try:
            return Empresa.objects.get(id=empresa_logada_id)
        except Empresa.DoesNotExist:
            return None
    return None