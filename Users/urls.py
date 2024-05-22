from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', views.admin.as_view(), name = 'admin'),
    path('User/', views.UserListCreate.as_view(), name='User-list-create'),
    path('User/<int:pk>/',views.UserRetrieveUpdateDestroy.as_view(), name = 'update-delete-user'),
    path('Celeb/', views.CelebListCreate.as_view(), name='Celebs-list-create'),
    path('Celeb/<int:pk>/',views.CelebRetrieveUpdateDestroy.as_view(), name = 'update-delete-celeb'),
    path('ngo/', views.ngoListCreate.as_view(), name='ngo-list-create'),
    path('ngo/<int:pk>/',views.ngoRetrieveUpdateDestroy.as_view(), name = 'update-delete-ngo'),
    path('Fans/', views.FansListCreate.as_view(), name='Fans-list-create'),
    path('Fans/<int:pk>/',views.FansRetrieveUpdateDestroy.as_view(), name = 'update-delete-Fans')
]