from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import admin

from .models.classic import Classic
from .models.count import Count
from .models.time import Time
from .models.deadline import Deadline

from outcomes.models.outcome import Outcome


class ClassicAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'description',
        'is_done',
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('change_outcome/', self.admin_site.admin_view(self.change_outcome_view), name='change_outcome')
        ]
        return custom_urls + urls

    def change_outcome_view(self, request):
        if request.method == 'POST':
            outcome_id = request.POST.get('outcome')
            task_ids = request.POST.get('tasks').split(',')
            new_outcome = Outcome.objects.get(pk=outcome_id)
            tasks = Classic.objects.filter(id__in=task_ids)
            tasks.update(outcome=new_outcome)
            self.message_user(request, "Selected tasks have been reassigned.")
            return redirect('..')

        outcomes = Outcome.objects.all()
        tasks = request.GET.get('tasks').split(',')
        context = {'outcomes': outcomes, 'tasks': ','.join(tasks)}
        return render(request, 'admin/change_outcome.html', context)

    def change_outcome(self, request, queryset):
        task_ids = ','.join([str(task.id) for task in queryset])
        return redirect(f'change_outcome/?tasks={task_ids}')

    def make_is_done_true(modeladmin, request, queryset):
        queryset.update(is_done=True)
        modeladmin.message_user(request, "is done true")

    def make_is_done_false(modeladmin, request, queryset):
        queryset.update(is_done=False)
        modeladmin.message_user(request, "is done false")

    def save_task(modeladmin, request, queryset):
        for task in queryset:
            task.save()
        modeladmin.message_user(request, "save")

    make_is_done_false.short_description = "is done false"
    make_is_done_true.short_description = "is done true"
    change_outcome.short_description = "Change assigned outcome for selected tasks"
    save_task.short_description = "Save tasks"

    actions = [
        make_is_done_false,
        make_is_done_true,
        change_outcome,
        save_task,
    ]


class CountAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'description',
        'total_count',
        'xp'
    ]


class TimeAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'description',
        'total_time',
        'xp'
    ]


class DeadlineAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'description',
        'deadline_date',
        'xp'
    ]


admin.site.register(Classic, ClassicAdmin)
admin.site.register(Count, CountAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Deadline, DeadlineAdmin)
