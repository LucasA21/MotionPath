from django.urls import path
from app.progress.views.create_view import ProgressCreateView
from app.progress.views.delete_view import ProgressDeleteView
from app.progress.views.detail_view import ProgressDetailView
from app.progress.views.list_view import ProgressListView
from app.progress.views.update_view import ProgressUpdateView

urlpatterns = [
    path('', ProgressListView.as_view(), name='progress_list'),
    path('<int:pk>/', ProgressDetailView.as_view(), name='progress_detail'),
    path('create/', ProgressCreateView.as_view(), name='progress_create'),
    path('update/<int:pk>/', ProgressUpdateView.as_view(), name='progress_update'),
    path('delete/<int:pk>/', ProgressDeleteView.as_view(), name='progress_delete'),
]
