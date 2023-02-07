from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
import poseSelect.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', poseSelect.views.index, name='index'),
    path('fourbyone/', poseSelect.views.fourbyone, name='fourbyone'),
    path('twobytwo/', poseSelect.views.twobytwo, name='twobytwo'),
    path('fourbyone_1/', poseSelect.views.fourbyone_1, name='fourbyone_1'),
    path('fourbyone_2/', poseSelect.views.fourbyone_2, name='fourbyone_2'),
    path('fourbyone_3/', poseSelect.views.fourbyone_3, name='fourbyone_3'),
    path('fourbyone_4/', poseSelect.views.fourbyone_4, name='fourbyone_4'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
