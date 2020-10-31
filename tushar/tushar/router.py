from rest_framework import routers
from books.api import BooksViewSet

router = routers.DefaultRouter()
router.register('books', BooksViewSet, 'books')
