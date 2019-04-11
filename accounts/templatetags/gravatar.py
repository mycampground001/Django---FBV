import hashlib
# 장고의 템플릿 내놔
from django import template
from django.template.defaultfilters import stringfilter

# 템플릿 라이브러리 가져와
register = template.Library()

# 필터로 makehash 함수를 추가해
@register.filter
@stringfilter
def makehash(email):
    return hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()