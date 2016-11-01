from django.conf.urls import url
from django.contrib import admin

from guitar_tab_app.views import IndexView, TabView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^(?P<tab_url>.*)', TabView.as_view(), name="tab_view"),
]
