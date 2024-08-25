from django.urls import path
import app.user.views as view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', view.UserListView.as_view(), name='user_list'),
    path('<int:pk>/', view.UserDetailView.as_view(), name='user_detail'),
    path('profile/', view.UserDetailProfileView.as_view(), name='user_detail_profile'),
    path('create/', view.UserCreateView.as_view(), name='user_create_profile'),
    path('update/<int:pk>', view.UserUpdateView.as_view(), name='user_update'),
    path('profile/update/', view.UserUpdateProfileView.as_view(), name='user_update_profile'),
    path('delete/<int:pk>', view.UserDeleteView.as_view(), name='user_delete'),
    path('logout/', LogoutView.as_view(next_page='user_login'), name='user_logout'),
]
