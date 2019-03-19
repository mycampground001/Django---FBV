from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect(board)
    else:
        board_form = BoardForm()
    context = {
        'board_form':board_form
        }
    return render(request,'boards/create.html',context)
    
def detail(request,board_pk):
    # board = Board.objects.get(pk=board_pk) #사용자가 없는 값을 입력하면 에러가 떠, 그래서 get_object_or_404를 import 해줘
    board = get_object_or_404(Board,pk=board_pk)
    board.hit += 1
    board.save()
    context = {
        "board":board
    }
    return render(request,'boards/detail.html',context)