#url은 라우팅만 담당
from django.urls import path
from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:detail_id>/results/', views.results, name='results'),
    path('<int:detail_id>/vote/', views.vote, name='vote'),
    #path('<int:detail_id>/create/', views.create, name="create"),
]
#path함수는 path(route, views, kwargs, name)형태로 호출, 총 4개의 인수를 받음
#               ^^주소  ^^호출할 뷰 ^^부에 전달할 값 ^^이름