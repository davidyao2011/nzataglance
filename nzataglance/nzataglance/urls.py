from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('home/', include('home.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/accounts/login/')),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]