# Alexandria/review/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import Book
from review.forms import ReviewForm
from review.models import Review

@login_required
def review_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        try:
            review = Review.objects.get(book=book, user=request.user)
            form = ReviewForm(request.POST, instance=review)
        except Review.DoesNotExist:
            form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book', book_id=book.id)

        # Form not valid, re-render with errors
        data = {
            'book':book,
            'form':form,
        }

        return render(request, 'review.html', data)

    # GET method
    try:
        review = Review.objects.get(book=book, user=request.user)
        form = ReviewForm(instance=review)
    except Review.DoesNotExist:
        form = ReviewForm()

    data = {
        'book':book,
        'form':form,
    }

    return render(request, 'review.html', data)
