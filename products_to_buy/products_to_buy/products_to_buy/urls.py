from django.contrib import admin
from django.urls import path, include
from django.conf.urls  import handler404, handler500, handler403, handler400
from products import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls'))  # a raiz será apontada para o app products
]


handler404 = views.error404  # define onde será os possiveis erros
handler404 = views.error500
