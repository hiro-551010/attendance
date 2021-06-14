from django.db import models
from config import settings

class AttendanceEmployee(models.Model):
    class Meta:
        db_table = 'attendance'

    PLACES = (
        (1, 'きゅうあん'),
        (2, 'こうしえん'),
    )
    IN_OUT = (
        (1, 'IN'),
        (0, 'OUT'),
    )

    employee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="従業員", on_delete=models.CASCADE)
    place = models.IntegerField(verbose_name='出勤場所名', choices=PLACES, default=None)
    in_out = models.IntegerField(verbose_name='IN/OUT', choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    date = models.DateField(verbose_name='打刻日')