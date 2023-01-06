from django.shortcuts import render, get_object_or_404
from . models import Project, Post, Comment, Profile, Expertise, Education, Skills
from . forms  import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.

def home(request):
    profiles = Profile.objects.all()
    skills = Skills.objects.all()
    educations = Education.objects.all()
    expertises = Expertise.objects.all()
    project = Project.objects.all()


    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Portfolio message from' + name,
            message, 
            email,
            ['omejesixtusnnanna@yahoo.com',],
            fail_silently=True
        )
        return render(request, 'main/home.html', {'name':name})
    context = {
        'skills':skills, 
        'profiles': profiles,
        'educations':educations,
        'expertises': expertises,
        'project': project,

      
        
    
    }
    return render(request, 'main/home.html', context)


def projectList(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'main/index.html', context)


def projectDetail(request, project_id):
    project = get_object_or_404(Project, pk = project_id)
    context = {'project':project}
    return render(request, 'main/project_detail.html', context)


def categoryPost(request, category):
    posts = Post.objects.filter(category__name__contains=category).order_by('-created_on')
    return render(request, 'main/post_category.html', {'posts':posts})


def postList(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts':posts}

    return render(request, 'main/post_list.html', context)

def postDetail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[str(post_id)]))
    comments = Comment.objects.filter(post=post)
    context = {
        'post':post,
        'form':form,
        'comments':comments,
    }
    return render(request, 'main/post_detail.html', context)

