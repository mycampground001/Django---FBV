from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.

def index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'users/index.html', context)
    
def detail(request, user_pk):
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    # user_boards = user.board_set.all()
    context = {'user_detail':user}
    # context = {'user_detail':user, 'user_boards':user_boards}
    return render(request, 'users/detail.html',context)