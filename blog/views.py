from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
#    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST) #form이 Post의 인스턴스
        if form.is_valid():
            post = form.save(commit=False) #form.save를 통해 post를 Post의 인스턴스로 만들어줌
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/form_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) #Post에서 pk값에 해당하는 인스턴스를 리턴함
    if request.method == "POST":
        form = PostForm(request.POST, instance=post) #post값이 저장되 있는 채로 보여줌
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) #입력한 post의 pk값을 가진 디테일로 들어감
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/form_edit.html', {'form': form})
