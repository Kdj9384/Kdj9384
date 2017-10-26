from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # 메인 페이지
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), # 상세정보
    url(r'^post/new/$', views.post_new, name='post_new'), # 새로 작성
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), # 수정페이지
]

# (?P<name>\d+) 이 그룹에 이름을 name이라 하고 해당하는 name을 이용하여 매칭된 문자열을 받음
# 받을 문자열을 \d+ - 숫자 로 받겠다.
