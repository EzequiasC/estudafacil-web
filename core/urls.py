from django.contrib import admin
from django.urls import path
from gestao_estudos.views import login_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('painel/', dashboard_view, name='dashboard'), 
]