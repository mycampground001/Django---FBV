from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import hashlib
from .models import Board
from .forms import BoardForm

# Create your views here.
# @login_required
def index(request):
    boards = Board.objects.order_by('-pk')
    if request.user.is_authenticated:
        gravatar_url = hashlib.md5(request.user.email.strip().lower().encode('utf-8')).hexdigest()
    else:
        gravatar_url = None
        # d0e53a9a9bbc9cf481144a929930f41c
    context = {
        'boards':boards,
        'gravatar_url':gravatar_url,
        }
    return render(request, 'boards/index.html',context)

@login_required
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('boards:index')
    
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        if board_form.is_valid(): #유효하면
            # title = board_form.cleaned_data.get('title') #정제된 데이터를 가져온다.
            # content = board_form.cleaned_data.get('content')
            # board = Board(title=title,content=content)
            # board.save()
            board = board_form.save(commit=False) #위의 주석4줄과 동일함.
            board.user = request.user
            board.save()
            return redirect(board)
    else:
        board_form = BoardForm()
        
    context = {
        'board_form':board_form
        }
    return render(request,'boards/form.html',context)
    
def detail(request,board_pk):
    # board = Board.objects.get(pk=board_pk) #사용자가 없는 값을 입력하면 에러가 떠, 그래서 get_object_or_404를 import 해줘
    board = get_object_or_404(Board,pk=board_pk)
    board.hit += 1
    board.save()
    context = {
        "board":board
    }
    return render(request,'boards/detail.html',context)
    
def delete(request,board_pk):
    board = get_object_or_404(Board,pk=board_pk)
    if request.user == board.user:
        if request.method == "POST":
            board.delete()
            return redirect('boards:index')
        else:
            return redirect(board)
    else:
        return redirect(board)
        
        
def update(request, board_pk):
    # 1. board_pk에 해당하는 오브젝트를 가져온다.
    #    - 없으면, 404
    #    - 있으면, board = Board.objects.get(pk=board_pk) 와 동일
    board = get_object_or_404(Board, pk=board_pk)
    if request.user == board.user:
        # 2-1. POST 요청이면 (사용자가 form을 통해 데이터를 보내 준 것.)
        if request.method == "POST":
            # 사용자 입력값(request.POST)을 BoardForm에 전달해주고, 
            board_form = BoardForm(request.POST, instance=board)
            # 검증 (유효성 체크)
            if board_form.is_valid():
                # board.title = board_form.cleaned_data.get('title')
                # board.content = board_form.cleaned_data.get('content')
                # board.save()
                board = board_form.save() # 위 주석 3줄과 동일
                return redirect(board)
        # 2-2. GET 요청이면 (수정하기 버튼을 눌렀을 때)
        else:
            # BoardForm을 초기화 (사용자 입력값을 넣어준 상태)
            # board_form = BoardForm(initial=board.__dict__)
            board_form = BoardForm(instance=board)
        # context에 담겨있는 board_form은 두 가지 상황이 있다.
        # 1 - POST 요청에서 검증에 실패하였을 때, 오류 메세지가 포함된 상태
        # 2 - GET 요청에서 초기화된 상태
        context = {
            'board_form': board_form
        }    
        return render(request,'boards/form.html',context)
    else:
        return redirect(board)
    
    
