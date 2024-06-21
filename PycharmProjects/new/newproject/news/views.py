from django.shortcuts import render, redirect
from .models import Articles, News
from .forms import ArticlesForm, SearchForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q

def news_home(request):
    news = Articles.objects.order_by('-date')[:2]
    return render(request, 'news/news_home.html',{'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm



def search_results(request):
    form = SearchForm(request.GET)
    results = []
    if form.is_valid():
        query = form.cleaned_data['query']
        results = News.objects.filter(Q(title__icontains=query) | Q(anons__icontains=query))
    return render(request, 'news/details_view.html', {'form': form, 'results': results})





class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'




def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма неверна'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

