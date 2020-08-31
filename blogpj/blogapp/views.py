from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import CommentForm
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages


def searchyy(request):          
    contents =  request.GET.get('searchqq') #name = searchqq에 입력된 내용을 title로 받기
    if contents:   #검색어가 입력되면 
        status = Blog.objects.filter(Q(title__icontains = contents) | Q(body__icontains = contents.replace(" ", ""))) #(title__icontains=title)제목만
        return render(request,'search.html',{'status':status})
    else:       #입력된 검색어가 없으면
        return redirect('/')
        

def home(request):
    blogs = Blog.objects #쿼리셋 #메소드
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, b_id):
    blog_detail = get_object_or_404(Blog, pk = b_id)
    return render(request, 'detail.html', {'bb':blog_detail})

def update(request, u_id): #url에 이름이 update라는 애를 통해서 request(요청)이 들어오고 여러 글들 중 어떤 블로그를 수정할지 u_id라는 pk값도 같이 url로 들어옴.
    zz = get_object_or_404(Blog, pk = u_id) #zz라는 변수에 수정하고 싶다고 콕! 찍은 그 pk(위에서 알려준 u_id)를 갖는 (Blog라는모델 형태의) 글을 담음, 
                                             #(get_object_or_404 = 그 글이 없다면 404에러를 보여줘~) 

    if request.method == 'POST':#만약 요청이 POST라면~ (create.html에 있는 form 의 method = 'POST'니까 POST로 요청이 들어오겠죠?)
         zz.title = request.POST['t']#수정하고 싶은 글 zz중에 title을(zz는 Blog라는 모델을 틀로 title, body를 전부 가져오니까) 
                                         #create.html에 있는 태그중에서 <... name="t" ...>이렇게 이름이 t인 애한테 담긴 내용을 저장해줘
         zz.body = request.POST['b']#수정하고 싶은 글 zz중에 body를 create.html에 있는 태그중에서 <... name="b" ...> 이렇게 이름이 b인 애한테 담긴 내용을 저장해줘
                                     ##사용자는 수정하고 싶은 내용을 담으면 되겠죠?
         zz.photo = request.FIELS['p']
         zz.save()                   #이제 저장..★해줘
         return redirect('/blog/'+str(u_id)) #저장하고 url이 blog/u_id인 애한테로 가자

    else:                       #요청이 POST로 들어오지 않으면 즉, 수정사항을 입력하기 위해 페이지에 처음 접속했을 때

        return render(request, 'update.html', {'blog2':zz}) #원래 블로그 글zz를 blog2라는 이름으로 넘겨줘

#pk vs fk??
#pk = primary key라는 뜻으로 예를 들면 블로그 글들이 갖는 번호와도 같은것입니다.
#블로그 글이 3개 있다면 블로그 글 각각에 /blog/1 , /blog/2, /blog/3/ <- 이런식으로 url에 숫자가 붙죠?? 그리고 이를 통해서 글들을 구분해주죠?? 그것들이 pk입니다!

#fk = foreign key라는 뜻으로 pk를 갖는 블로그 글에 붙는 댓글들의 번호와도같은 것입니다.
#하나의 글에 댓글이 여러개가 달릴 수 있고 이들을 구분해주어야겠죠?
#pk가 1번인 글에 댓글이 3개가 달렸다면 그 댓글은 각각 fk가 1,2,3이겠죠??
#그리고 이 댓글들은 1번 글이 사라지면 모두 사라져버리게됩니다! 따라서 pk와 fk는 1:N관계가 되는것이죠.

#일단은 간단하게 pk는 엄마오리고 이 엄마오리를 졸졸 따라다니는 아기오리들이 fk라고 생각하시면 쉬울거에요~
#그리고 슬프게도 엄마오리가 사라지면 아기오리도 사라지는거에요ㅜ^ㅜ
#이렇게라도 이해가 조금이나마 가셨길 바랍니다^^

def create(request):

    if request.method == 'POST': #POST로 요청이 들어오면
        blogssss = Blog()#Blog모델의 내용들을 blog라는 변수에 담고
        blogssss.photo = request.FILES['p']
        blogssss.title = request.POST['t']
        blogssss.body = request.POST['b']
        blogssss.pub_date = timezone.datetime.now()
        blogssss.save()
        return redirect('/blog/'+str(blogssss.id))
    else:
        return render(request, 'create.html')


def comment_create(request, posts_id):

    if request.method == 'POST':
        post = get_object_or_404(Blog, pk = posts_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/blog/'+str(post.id))
    else:
        form = CommentForm()
        return render(request, 'detail.html', {'form':form})
