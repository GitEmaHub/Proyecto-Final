from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("about/", about, name="About"),
    path("latestWork/", latestWork, name="LatestWork"),
    path("comunidad/", comunidad, name="Comunidad"),
    path("contacto/", contacto, name="Contacto"),
    path("comuniFormulario/", comuniFormulario, name="FormularioComunidad"),
    path("buscarContacto/", busquedaComunidad, name="BuscarContacto"),
    path("resultados/", resultados, name="ResultadosBusqueda"),

    #CRUD de Contactos

    path("leerContactos/", leerContactos, name="ContactosLeer"),
    path("crearContactos/", crearContactos, name="Contactoscrear"),

    #CRUD de Comunidad

    path("comunidad/list/", listaComunidad.as_view(), name="ComunidadLeer"),
    path("comunidad/<int:pk>", detalleComunidad.as_view(), name="ComunidadDetalle"),
  


]
