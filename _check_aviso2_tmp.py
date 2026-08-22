from django.test import Client
from accounts.models import Usuario

recepcionista = Usuario.objects.filter(rol=Usuario.ROL_RECEPCIONISTA).first()
c = Client(SERVER_NAME='127.0.0.1')
c.force_login(recepcionista)
r = c.get('/reportes/privado/2026-07-30/')
contenido = r.content.decode('utf-8', errors='ignore')
idx = contenido.find('<div class="aviso-pendientes">')
print(contenido[idx:idx+500])
