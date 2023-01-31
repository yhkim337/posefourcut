from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
import poseSelect.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poseSelect.views.index, name='index'),
    path('fourbyone/', poseSelect.views.fourbyone, name='fourbyone'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
