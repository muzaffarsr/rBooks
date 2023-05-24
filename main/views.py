from django.shortcuts import render
from .models import Book, Category


def home(request):
	books = Book.objects.order_by('-pub_date')
	context = {
		'books':books,
	}
	return render(request, 'main/index.html', context)


def category(request):
	books = Book.objects.order_by('-pub_date')
	categorys = Category.objects.all()
	context = {
		'books':books,
		'categorys':categorys,
	}
	return render(request, 'main/category.html', context)


def search(request):
	searching_results = Book.objects.filter( name__icontains = request.GET.get('search') )
	context = {
		'searching_results':searching_results,
	}
	return render(request, 'main/index.html', context)


def book(request, bid):
	book = Book.objects.get( id = bid )
	context = {
		'book':book,
	}
	return render(request, 'main/book.html', context)


def filter(request, cid):
	books = Book.objects.filter( category = cid )
	categorys = Category.objects.all()
	context = {
		'books':books,
		'categorys':categorys
	}
	return render(request, 'main/category.html', context)