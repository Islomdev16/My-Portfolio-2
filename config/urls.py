from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    # path(r'^download/^(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# @admin.register()
# class Admin(admin.ModelAdmin):
#     list_display = ("")
