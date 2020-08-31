from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home, name = 'home'),
    path('blog/', include('blogapp.urls')),

    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
    path('portfolio/new', portfolio.views.new, name="new"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static 파일과는 다르게 개발서버에서 기본 서빙 미지원
# 개발 편의성 목적으로 서빙 rule 추가 가능
# settings.DEBUG = False 일때는 static 함수에서 빈 리스트 리턴
