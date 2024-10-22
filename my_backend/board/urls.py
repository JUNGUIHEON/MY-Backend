from django.urls import path, include
from rest_framework.routers import DefaultRouter

from board.controller.views import BoardView

router = DefaultRouter()
router.register(r'board', BoardView)

urlpatterns = [
    path('', include(router.urls)),
    path('get-allcontent', BoardView.as_view({'get': 'list'}), name='board-list'),
    path('list-by-category', BoardView.as_view({'post': 'listByCategory'}), name='list-by-category'),
    path('list-by-title', BoardView.as_view({'get': 'listByTitle'}), name='list-by-title'),
    path('list-by-content', BoardView.as_view({'get': 'listByContent'}), name='list-by-content'),
    path('list-by-nickname', BoardView.as_view({'get': 'listByNickname'}), name='list-by-nickname'),
    path('register', BoardView.as_view({'post': 'create'}), name='board-register'),
    path('create-category', BoardView.as_view({'post': 'createCategory'}), name='create-category'),
    path('get-categories', BoardView.as_view({'get': 'getCategories'}), name='get-categories'),
    path('read/<int:pk>', BoardView.as_view({'get': 'readBoard'}), name='board-read'),
    path('delete/<int:pk>', BoardView.as_view({'delete': 'removeBoard'}), name='board-remove'),
    path('modify/<int:pk>', BoardView.as_view({'put': 'modifyBoard'}), name='board-modify'),
    path('check-authority/<int:pk>', BoardView.as_view({'post': 'checkAuthority'}), name='check-authority'),
]