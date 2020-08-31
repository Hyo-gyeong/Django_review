from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
#클래스형 뷰는 웹 프로그래밍에서 자주 사용하는 기능을 장고가 미리 준비해 뒀고 그걸 빌려다 쓰는 형태.
#CRUD는 정형적인 뷰들이 필요하기 때문에 클래스 형 뷰가 적절
from .models import Bookmark
from django.urls import reverse_lazy
# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark #안넣으면 ImproperlyConfigured at /bookmark/add/ ,BookmarkCreateView is missing a QuerySet에러 발생
    fields = ['site_name', 'url', 'favicon'] #어떤 필드들을 입력받을것인지
    success_url = reverse_lazy('list') #글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create' #접미사 변결설정, 기본으로 설정되어 있는 템플릿 이름들은 모델명_xxx이고 CreateView와 UpdateView는 form이 접미사인데 이걸 변경해주려고

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'favicon']
    template_name_suffix = '_update'
    #success_url나 get_absolute_url이라는 메서드를 통해 수정완료후 페이지를 설정할 수 있는데 이 둘이 없기때문에 
    # ImproperlyConfigured at /bookmark/update/1, No URL to redirect to.라는 에러 생김
    # 그러니 model에 get_absoulte_url을 설정해보자!

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')