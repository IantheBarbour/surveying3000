from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^survey_app/', include('survey_app.urls')),
    url(r'^admin/', admin.site.urls),
]
