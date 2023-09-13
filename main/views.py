from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm, UserRegistrationForm
from django.views.generic import ListView


def index(request):
    return render(request, 'main/index.html')


def info(request):
    return render(request, 'main/information.html')


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'main/blog.html'


def sending_post(request):
    # error = ''
    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         dream_post = form.save(commit=False)
    #         dream_post.user = request.user  # Установите пользователя из текущей сессии
    #         dream_post.save()
    #         return redirect('blog')
    #     else:
    #         error = 'Попробуй еще раз'
    # else:
    #     form = PostForm()
    # return render(request, 'main/sending.html', {'form': form, 'error': error})
    data = request.POST.copy()
    data.update({'name': request.user.first_name})
    form = PostForm(data)
    if form.is_valid():
        form.name = request.user.first_name
        form.save()
        return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'main/sending.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    error = ''
    data = request.POST.copy()
    data.update({'name': request.user.first_name})
    comment_form = CommentForm(data)
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment_data = comment_form.cleaned_data
        existing_comment = Comment.objects.filter(post=post, name=comment_data['name'],
                                                      content=comment_data['content']).first()
        if not existing_comment:
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            error = 'Комментарий уже существует'
    else:
        comment_form = CommentForm()
    return render(request, 'main/blog_comment.html', {'post': post, 'comment_form': comment_form, 'error': error})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            login(request, new_user)
            return redirect('home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.user in post.liked_by.all():
        post.liked_by.remove(request.user)
        post.likes -= 1
    else:
        post.liked_by.add(request.user)
        post.likes += 1

    post.save()

    return redirect('blog')



