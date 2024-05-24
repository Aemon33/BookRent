from django.shortcuts import render, redirect
from .forms import SearchBookForm
from books.models import Book
from django.views.generic import ListView
from .models import Rental
def search_book_view(request):
    form = SearchBookForm(request.POST or None)
    search_query = request.POST.get('search',None)
    book_ex = Book.objects.filter(isbn=search_query).exists()


    if search_query is not None and book_ex:
        #redirected to detail page (rentals list of the book )
        return redirect('rentals:detail', search_query)
    context = {'form':form}
    return render(request, "rentals/main.js", context)


class BookRentalHistoryView(ListView):
    
    model = Rental
    template_name = "rentals/detail.html"


    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        return Rental.objects.filter(book__isbn=book_id)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        qs = self.get_queryset()
        obj = None
        if qs.exists():
            obj = qs.first()
        context['obj'] = obj
        return context