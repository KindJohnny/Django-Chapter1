from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post

# Create your views here.

def post_list(request):
	posts = Post.draft.all()

	return render(request,'blog/post/list.html',{'posts':posts})


def post_detail(request,id):
	#post = get_object_or_404(Post,id=id,status = Post.Status.DRAFT)
	try:
		post = Post.draft.get(id=id)
	except Post.DoesNotExist:
		raise Http404('No post found!')
	
	return render(request,'blog/post/detail.html',{'post':post})