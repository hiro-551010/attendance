from django.shortcuts import render
from accounts.models import User, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from payment.forms import AttendanceForm
from payment.models import AttendanceEmployee
from datetime import datetime

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        form = AttendanceForm
        context = {
            'form': form,
            "user": request.user,
        }
        return render(request, 'payment/attendance.html', context)

class ResultView(View):
    def post(self, request):
        form = AttendanceForm(request.POST)
        now = datetime.now()
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        obj = form.save(commit=False)
        obj.place = request.POST["place"]
        obj.in_out = request.POST["in_out"]
        obj.employee = request.user
        obj.date = datetime.now().date()
        obj.time = datetime.now().time()
        obj.save()
        if request.POST["in_out"] == '1':
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "出勤確認しました。今日も頑張りましょう！"
        else:
            comment = str(month) + "月" + str(day) +"日" + str(hour) + "時" + str(minute) + "分\n" + "退勤確認しました。お疲れ様でした(^-^)！"
        context = {
            'place': AttendanceEmployee.PLACES[int(obj.place)-1][1],
            'comment': comment,
        }
        return render(request, 'payment/result.html', context)

# def pay(request):
#     users = User.objects.all()
#     for user in users:
#         user_name = user.email
#         payment = user.profile.hourly_wage
#         context = {
#             'user_name': user_name,
#             'payment': payment
#         }
        
#         return render(request, 'payment/pay.html', context)