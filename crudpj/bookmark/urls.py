from django.urls import path
from .views import *

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]

"""
컨버터의 종류
str : 비어있지 않은 모든 문자와 매칭. 단 '/'는 제외. 컨버터를 설정하지 않을 경우 default
int : 0을 포함한 양의 정수와 매칭
slug : 아스키 문자나 숫자, 하이픈, 언더스코어를 포함한 슬러그 문자열과 매칭
uuid : UUID와 매칭. 같은 페이지에 여러 URL이 연결 되는 것을 막으려고 사용
path : 기본적으로 str과 같은 기능니아 '/'도 포함. URL의 부분이 아닌 전체에 대한 매칭을 하고싶을 때 사용
"""