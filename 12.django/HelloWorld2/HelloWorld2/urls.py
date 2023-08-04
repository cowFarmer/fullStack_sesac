from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloapp.urls')),
    path('todo/', include('todo.urls')),
    path('photo/', include('photo_upload.urls')),
    path('poll/', include('poll.urls'))
    # static('/media), BASE_DIR/upload/photos -> urlpatterns와 동일
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)