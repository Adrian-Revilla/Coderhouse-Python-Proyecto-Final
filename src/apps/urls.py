
from django.urls import path

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('', views.index, name="index"),
	
	path('register/', views.RegisterView.as_view(), name="register"),
	path("login/", LoginView.as_view(template_name="login.html"), name="login"),
	path("logout/", LogoutView.as_view(), name="logout"),
	path('about/', views.about , name="acerca_del_autor"),
	path('nukear_db/', staff_member_required(views.nukear_db), name="borrar_data"),

	path('vehiculos/', views.VehiculoList.as_view(), name="vehiculos" ),
	path('vehiculos/<int:pk>', staff_member_required(views.VehiculoDetail.as_view()), name="vehiculos_detail" ),
	path('vehiculos/create', staff_member_required( views.VehiculosCreate.as_view()), name="vehiculos_create" ),
	path('vehiculos/delete/<int:pk>', staff_member_required( views.VehiculoDelete.as_view()), name="vehiculos_delete" ),
	path('vehiculos/update/<int:pk>', staff_member_required( views.VehiculoUpdate.as_view()), name="vehiculos_update" ),

	path('conductores/', views.ConductorList.as_view(), name="conductores" ),
	path('conductores/<int:pk>', views.ConductorDetail.as_view(), name="conductores_detail"),
	path('conductores/create', staff_member_required(views.ConductoresCreate.as_view()), name="conductores_create" ),
	path('conductores/delete/<int:pk>', staff_member_required(views.ConductorDelete.as_view()), name="conductores_delete" ),
	path('conductores/update/<int:pk>', staff_member_required( views.ConductorUpdate.as_view()), name="vehiculos_update" ),
	
	path('viajes/',  views.ViajeList.as_view(), name="viajes" ),
	path('viajes/<int:pk>', views.ViajeDetail.as_view(), name="viajes_detail" ),
	path('viajes/create', staff_member_required(views.ViajeCreate.as_view()), name="viajes_create" ),
	path('viajes/delete/<int:pk>',  staff_member_required(views.ViajeDelete.as_view()), name="viajes_delete" ),
	path('viajes/update/<int:pk>', staff_member_required(views.ViajeUpdate.as_view()), name="vehiculos_update" )
] + staticfiles_urlpatterns()


