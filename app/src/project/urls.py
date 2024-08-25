from django.contrib import admin
from django.urls import path, include

from app.user.views.login_view import UserLoginView
from app.user.views.sign_up_view import SignUpView
from app.home.views.home_view import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', SignUpView.as_view(), name='user_create'),
    path('home/', include('app.home.urls')),
    path('user/', include('app.user.urls')),
    path('trainer/', include('app.trainer.urls')),
    path('progress/', include('app.progress.urls')),
    path('exercise/', include('app.exercise.urls')),
    path('rutine/', include('app.rutine.urls')),
    path('rutine-type/', include('app.rutine_type.urls')),
    path('assign-rutine/', include('app.assign_rutine.urls')),
    path('exercise/', include('app.exercise.urls')),  
    path('exercise-type/', include('app.exercise_type.urls')), 
    path('muscle-exercise/', include('app.muscle_exercise.urls')),
    path('difficulty-level/', include('app.difficulty_level.urls')),
]
