from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def index(request):
    blog = Blog.objects.all()
    #페이지 3개로 자르기
    paginator = Paginator(blog, 3)
    #request된 페이지 변수에 담음
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'blogs':blog, 'posts':posts})

def detail(request, detail_id):
    blog_detail = get_object_or_404(Blog, pk = detail_id)
    return render(request, 'detail.html', {'detail':blog_detail})

# def new(request):
#     return render(request, 'new.html')

# def create(request):

#     blog = Blog()
#     blog.title = request.POST['title']
#     blog.body = request.POST['body']
#     blog.photo = request.FILES['photo']
#     blog.pub_date = timezone.datetime.now()
#     blog.save()
#     return redirect('/')

def new(request):
    #1.입력된 내용을 처리하는 기능:POST
    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES) #POST로써 들어온 내용을 form에 담아줌
        if form.is_valid():#잘 입력되어는지 확인
            blogpost = form.save(commit = False)#블로그 객체를 가져오되 아직은 저장하지 말아라
                                                #blogpost는 Blog객체가 됨
            blogpost.pub_date = timezone.datetime.now()
            blogpost.save()

            return redirect('/detail/' + str(blogpost.id))
    #2.빈페이지를 띄워주는 기능:GET
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})
#처음 new.html에 들어갔을 때 빈 입력공간을 띄우기 : GET : form이라는것을 갖다줘야하니까 if
#이용자가 뭘 입력하면 그 입력값들을 처리하기 : POST : 데이터를 처리해줘 else
#정의한 모든 모델을 입력받고싶지 않을수 있음, 자동으로 입력되게 하고싶은것도 있음(예, 날짜)

#form.save(commit = False)#일단 저장하지 말고 form객체 말고 model객체에 접근, commit = False라는 인자때문에 model객체가 저장되지 않고 반환됨
#model객체 안의 date변수에 접근, 수정
#model객체 저장

# def update(request, blog_id):
#     forms = get_object_or_404(Blog, pk=blog_id)
    
#     if request.method == 'POST':
#         forms.title = request.POST['title'] #name=title인 애한테 담긴 내용 저장
#         forms.body = request.POST['body'] #name=body인 애한테 담긴내용 저장
#         forms.save()
#         return redirect('/blog/'+str(blog_id))

#     else: #수정사항을 입력하려고 페이지에 접속하면
#         return render(request, 'new.html', {'forms':forms})

def updateform(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':#이렇게 해야 기존 내용을 불러올 수 있어
        form = BlogPost(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()#수정한 날짜로 저장
            post.save()
            return redirect('/detail/'+str(blog.id))
    else:#"
        form = BlogPost(instance = blog)#"
        return render(request, 'new.html', {'form':form})
