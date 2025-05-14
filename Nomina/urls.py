
from django.urls import path
from . import views  # Importa las vistas que usas en la app

app_name = 'Nomina'  # Nombre de la aplicación para el espacio de nombres
urlpatterns = [
    
    path('crear_empleado/',views.crear_empleado, name='crear_empleado'), 
    path('listar_empleados/', views.listar_empleados, name='listar_empleados'), 
    path('actualizar_empleado/<int:id>/', views.actualizar_empleado,name='actualizar_empleado'),
    path('eliminar_empleado/<int:id>/', views.eliminar_empleado,name='eliminar_empleado'),
    # Rutas para CARGO
    path('listar_cargos/', views.listar_cargos, name='listar_cargos'),
    path('crear_cargo/', views.crear_cargo, name='crear_cargo'),
    path('actualizar_cargo/<int:id>/', views.actualizar_cargo, name='actualizar_cargo'),
    path('eliminar_cargo/<int:id>/', views.eliminar_cargo, name='eliminar_cargo'),
    # Rutas para DEPARTAMENTO
    path('listar_departamentos/', views.listar_departamentos, name='listar_departamentos'),
    path('crear_departamento/', views.crear_departamento, name='crear_departamento'),
    path('actualizar_departamento/<int:id>/', views.actualizar_departamento, name='actualizar_departamento'),
    path('eliminar_departamento/<int:id>/', views.eliminar_departamento, name='eliminar_departamento'),
    
    # Rutas para TIPO CONTRATO
    path('listar_tipos_contrato/', views.listar_tipos_contrato, name='listar_tipos_contrato'),
    path('crear_tipo_contrato/', views.crear_tipo_contrato, name='crear_tipo_contrato'),
    path('actualizar_tipo_contrato/<int:id>/', views.actualizar_tipo_contrato, name='actualizar_tipo_contrato'),
    path('eliminar_tipo_contrato/<int:id>/', views.eliminar_tipo_contrato, name='eliminar_tipo_contrato'),
    
    # Rutas para ROL
    path('listar_roles/', views.listar_roles, name='listar_roles'),
    path('crear_rol/', views.crear_rol, name='crear_rol'),
    path('actualizar_rol/<int:id>/', views.actualizar_rol, name='actualizar_rol'),
    path('eliminar_rol/<int:id>/', views.eliminar_rol, name='eliminar_rol'),

    # Rutas para login
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    
    #Crud Adicional (Examen Práctico)
    path('listar_prestamos/', views.listar_prestamos, name='listar_prestamos'),
    path('crear_prestamo/', views.crear_prestamo, name='crear_prestamo'),
    path('actualizar_prestamo/<int:id>/', views.actualizar_prestamo, name='actualizar_prestamo'),
    path('eliminar_prestamo/<int:id>/', views.eliminar_prestamo, name='eliminar_prestamo'),


]

