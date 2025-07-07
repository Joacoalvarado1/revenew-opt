from django.contrib import admin
from django.urls import path
from optimization_app.views import upload_csv, test_opt_model, descargar_historial_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_csv, name='upload_csv'),
    path('test/', test_opt_model, name='test_opt_model'),
    path('download/', descargar_historial_excel, name='descargar_excel'),
]
