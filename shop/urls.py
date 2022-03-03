from django.contrib import admin
from django.urls import (path , include)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route='' , view=include('home.urls')),
    path(route='' , view=include('accounts.urls')),
    path(route='products/' , view=include('product.urls')),
    path(route='contact-us/' , view=include('contact.urls'))
]


urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)