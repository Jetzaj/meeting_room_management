from django.conf.urls import url
from meetings import views

urlpatterns = [
    # 会议室列表
    url(r"^roomlist/", views.roomlist, name="会议室列表"),
    url(r"^room/(?P<room_id>\d+)/$", views.detail, name="会议室详情")
]
