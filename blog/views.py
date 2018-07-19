from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post
from .forms import PostForm

# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully created!")
        return HttpResponseRedirect(instance.get_absolute_url())

    context={ 'form':form}
    return render(request,'post_form.html',context)

def post_detail(request,id=None):
    instance = get_object_or_404(Post,id=id)

    context = {'title': instance.title,
               'instance':instance,
               }
    return render(request,'post_detail.html',context)

def post_list(request):
    queryset_list= Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset_list, 10)

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context = {'object_list': queryset,
               'title':'List'}
    return render(request,'post_list.html',context)


def listing(request):
    contact_list = Contacts.objects.all()
     # Show 25 contacts per page


def post_update(request,id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Saved')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'title': instance.title,
               'instance':instance,
               'form':form}
    return render(request,'post_form.html',context)

def post_delete(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request,'Deleted')
    return redirect("blog:list")
