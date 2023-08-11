"""
URL configuration for index project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Truy vấn thể loại sách có ít độc giả nhất và danh sách các độc giả của từng thể loại sách.
    path('unpopular-genres-readers/', views.unpopular_genres_and_readers, name='unpopular-genres-readers'),
    # Truy vấn tác giả có nhiều độc giả đặt hàng sách nhiều nhất và danh sách các độc giả của từng tác giả.
    path('popular-authors-readers/', views.popular_authors_and_readers, name='popular-authors-readers'),
    # Hiển thị đầy đủ thông tin danh sách sách
    path('book-list/', views.book_list, name='book-list'),
    # Hiển thị đầy đủ thông tin tác giả và sách viết bởi tác giả
    path('author-list/', views.author_list, name='author-list'),
    # Tìm sách có khuyến mãi và thông tin khuyến mãi
    path('book-promotion-list/', views.book_promotion_list, name='book-promotion-list'),
    # Tìm sách có khuyen mai bang model Book
    path('book-promotion/', views.book_promotion, name='book-promotion'),
]
