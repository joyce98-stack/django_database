from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import normalize_newlines
from unicodedata import category

from app.models import Book
from app.my_forms import BookForm


# Create your views here.
@login_required
def show_books(request):
    books = Book.objects.all()
    return render(request, 'show_books.html', {'books': books})


@login_required
@permission_required('app.add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Book{request.POST.get('title')}Added Successfully')
            # messages.success(request,f'Book {request.POST.get('title)} Created')
            return redirect('show_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


# django models
# Book.objects.create(title='Too Pretty To Be Broke',
#                     year=2020,
#                     category='Fiction',
#                     cost=800,
#                     isbn='3356909090',
#                     published=True )
#
# Book.objects.create(title='Money Madness',
#                     year=2022,
#                     category='Fiction',
#                     cost=1000,
#                     isbn='4356909090',
#                     published=True)

@login_required
@permission_required('app.delete_book')
def delete_book(request, id):
    book = Book.objects.get(id=id)  # select * from books where id =
    book.delete()
    messages.error(request, f'{book.title}Deleted Successfully')  # delete from books where id =
    return redirect('show_books')


@login_required
@permission_required('app.change_book', raise_exception=True)
def edit_book(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, f'{book.title}Updated Successfully')
            return redirect('show_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('show_books')
        else:
            form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            form = RegisterForm()
        return render(request, 'registration/signup.html', {'form': form})


@login_required
def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
