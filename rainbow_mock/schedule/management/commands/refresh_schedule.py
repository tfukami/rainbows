import datetime
import jpholiday

from django.conf import settings
from django.utils import timezone
from django.core.management.base import BaseCommand
from accounts.models import CustomUser

from ...models import Schedules


class Command(BaseCommand):
    help = "Refresh schedule data"

    def handle(self, **args):

        now = datetime.datetime.now()
        users = CustomUser.objects.all()
        Schedules.objects.filter(schedule_date__lt=timezone.now()).delete()

        dat = []
        for i in range(6, 7):
            d = now + datetime.timedelta(days=i)
            print(d.strftime("%Y-%m-%d"))
            for u in users:
                if u.occupation == 1 or jpholiday.is_holiday(d.date()) or d.date().weekday() in (5, 6):
                    dat.append(
                        Schedules(user_id=u.id, schedule_date='{}'.format(d.strftime("%Y-%m-%d")), period=0, status=1)
                    )
                    dat.append(
                        Schedules(user_id=u.id, schedule_date='{}'.format(d.strftime("%Y-%m-%d")), period=1, status=1)
                    )
                    dat.append(
                        Schedules(user_id=u.id, schedule_date='{}'.format(d.strftime("%Y-%m-%d")), period=2, status=1)
                    )
        Schedules.objects.bulk_create(dat)

        for user in users:
            print(user, user.gender, user.id)

        schedules = Schedules.objects.all()
        for schedule in schedules:
            print(schedule, schedule.user_id, schedule.schedule_date, schedule.period, schedule.status)
