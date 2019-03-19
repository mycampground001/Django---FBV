from django.contrib import admin
from .models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    # 표 형태로 출력하기 위해 클래스 작성
    list_display = ['id','title','content','hit','created_at','updated_at']


admin.site.register(Board, BoardAdmin)