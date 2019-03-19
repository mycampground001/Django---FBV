from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm

# Create your views here.
def index(request):
    
    boards = Board.objects.order_by('-pk')
    
    context = {
        'boards':boards
        }
        
    return render(request, 'boards/index.html',context)

def create(request):
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        if board_form.is_valid(): #유효하면
            title = board_form.cleaned_data.get('title') #정제된 데이터를 가져온다.
            content = board_form.cleaned_data.get('content')
            board = Board(title=title,content=content)
            board.save()
        return redirect('boards:index')
    else:
        board_form = BoardForm()
    context = {
        'board_form':board_form
        }
    return render(request,'boards/create.html',context)