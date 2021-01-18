from django.contrib import admin
from django.conf.urls import url
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from to_do_app import views

schema_view = get_schema_view(
    openapi.Info(
        title='To Do APP Documentation',
        default_version='v1',
        contact=openapi.Contact(email='tanuljain25feb@gmail.com'),
    ),
    public=True,
    )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/task', views.LCTaskAPI.as_view()),
    path('api/v1/task/<int:pk>', views.RUDTaskAPI.as_view()),
    url(r'^api/v1/doc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]



