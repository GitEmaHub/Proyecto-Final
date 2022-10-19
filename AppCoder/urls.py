from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name="Inicio"),
    path("about/", about, name="About"),
    path("latestWork/", latestWork, name="LatestWork"),
    path("comunidad/", comunidad, name="Comunidad"),
    path("contacto/", contacto, name="Contacto"),
    path("comuniFormulario/", comuniFormulario, name="FormularioComunidad"),
    path("buscarContacto/", busquedaComunidad, name="BuscarContacto"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    path("login/", inicioSesion, name="Login"),
    path("register/", registro, name="Registro"),
    path("logout/", LogoutView.as_view(template_name="AppCoder/logout.html"), name="Logout"),
    path("editar/", editarUsuario, name="EditarUsuario"),

    #CRUD de Contactos con funciones

    path("leerContactos/", leerContactos, name="ContactosLeer"),
    path("crearContactos/", crearContactos, name="ContactosCrear"),
    path("eliminarContactos/<contactoNombre>/", eliminarContactos, name="ContactosEliminar"),
    path("editarContactos/<contactoNombre>/", editarContactos, name="ContactosEditar"),

    #CRUD de Comunidad con clases

    path("comunidad/list/", ListaComunidad.as_view(), name="ComunidadLeer"),
    path("comunidad/<int:pk>", DetalleComunidad.as_view(), name="ComunidadDetalle"),
    path("comunidad/crear/", CrearComunidad.as_view(), name="ComunidadCrear"),
    path("comunidad/editar/<int:pk>", ActualizarComunidad.as_view(), name="ComunidadEditar"),
    path("comunidad/borrar/<int:pk>", BorrarComunidad.as_view(), name="ComunidadBorrar"),
    
  


]
