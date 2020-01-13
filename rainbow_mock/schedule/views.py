from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.db import connection
from .forms import InquiryForm
from .models import Schedules, Friends
import logging

from django.urls import reverse_lazy

logger = logging.getLogger(__name__)

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('schedule:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました．')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)


class ScheduleView(LoginRequiredMixin, generic.ListView):
    model = Schedules
    template_name = 'schedule_index.html'

    def _custom_sql(self):
        query = '''
          SELECT * 
          FROM schedule_schedules 
          WHERE user_id = {i} or user_id in (select friend_id from schedule_friends where user_id = {i})
        '''.format(i=self.request.user.id)

        with connection.cursor() as cursor:
            cursor.execute(
                query
            )
            row = cursor.fetchall()

        return row

    def get_queryset(self):
        schedules = Schedules.objects.distinct().filter(
            user=self.request.user
        ).select_related()
    #    '''.filter(
    #        schedule_date__gte=timezone.now()
    #    )'''
    #    '''
    #    schedules.union(
    #        Schedules.objects.distinct().filter(
    #            user_id__in=list(Friends.objects.filter(user=self.request.user).values_list('friend_id', flat=True))
    #        ).filter(
    #            schedule_date__gte=timezone.now()
    #        ).select_related()
    #    )
    #    '''

        # friend = list(Friends.objects.all().filter(user=self.request.user).values_list('friend_id', flat=True))
        # return self._custom_sql()
        return schedules

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['friend_list'] = Schedules.objects.distinct().filter(
            user_id__in=list(Friends.objects.filter(user=self.request.user).values_list('friend_id', flat=True))
        )
        '''.filter(
            schedule_date__gte=timezone.now()
        )'''
        return context

