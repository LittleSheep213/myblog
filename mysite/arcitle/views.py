from django.shortcuts import render_to_response, get_object_or_404
from .models import Article  #这里使用了相对路径

# Create your views here.
def article_detail(request, article_id):
	# try:
	# 	article = Article.objects.get(id = article_id)
	# 	context = {}
	# 	context['article_obj'] = article
	# 	# return render(request, "article_detail.html", context)
	# 	return render_to_response("article_detail.html", context)
	# except Article.DoesNotExist:
	# 	raise Http404("DoesNotExist")

	article = get_object_or_404(Article, pk=article_id) # pk是主关键字(primary key)，你不知道主键名时写的。可以仍然写成id
	context = {}
	context['article_obj'] = article
	return render_to_response('article_detail.html', context)
	

def article_list(request):
	articles = Article.objects.all();
	context = {}
	context['articles'] = articles
	return render_to_response("article_list.html", context)