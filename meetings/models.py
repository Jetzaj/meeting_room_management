from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

Departments = [
    (0, "技术中心"),
    (1, "基础中心"),
    (2, "方案中心"),
    (3, "安全中心"),
    (4, "战略运营"),
    (5, "数字化转型项目 I"),
    (6, "数字化转型项目 II"),
    (7, "数字化转型项目 III")
]


# 会议室信息
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=250, blank=False, verbose_name="会议室名称")
    room_department = models.SmallIntegerField(choices=Departments, blank=False, verbose_name="会议室所属小微")
    room_maintenance_name = models.CharField(max_length=250, verbose_name="会议室维护人")
    room_maintenance_number = models.CharField(max_length=250, verbose_name="会议室维护人工号")
    room_maintenance_phone = models.CharField(max_length=250, verbose_name="会议室维护人电话")
    room_location = models.CharField(max_length=250, verbose_name="会议室位置")
    creator = models.ForeignKey(User, verbose_name="创建人", null=True, on_delete=models.SET_NULL)
    created_time = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    updated_time = models.DateTimeField(verbose_name="修改事件", default=datetime.now)

    class Meta:
        db_table = "meeting_room_t"
        verbose_name = "会议室信息"
        verbose_name_plural = "会议室列表"

    def __str__(self):
        return self.room_name


# 会议室预定信息
class RoomBooking(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, verbose_name="会议室", null=True, on_delete=models.SET_NULL)
    booking_user = models.ForeignKey(User, verbose_name="会议室预定人", null=True, on_delete=models.SET_NULL)
    booking_user_name = models.CharField(max_length=250, blank=False, verbose_name="会议预定人姓名")
    booking_user_phone = models.CharField(max_length=250, blank=False, verbose_name="预定人联系方式")
    start_time = models.DateTimeField(verbose_name="预定开始时间", default=datetime.now)
    end_time = models.DateTimeField(verbose_name="预定结束时间", default=datetime.now)
    created_time = models.DateTimeField(verbose_name="创建时间", default=datetime.now)
    updated_time = models.DateTimeField(verbose_name="修改时间", default=datetime.now)

    class Meta:
        db_table = "meeting_room_booking_t"
        verbose_name = "会议室预定信息"
        verbose_name_plural = "会议室预定信息列表"

