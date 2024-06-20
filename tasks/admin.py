from django.shortcuts import render, redirect
from django.urls import path
from django.contrib import admin
from abilities.models.outcome import Outcome
from .models.task import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'outcome',
        'description',
        'is_done',
        'is_added'
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
            tasks = Task.objects.filter(id__in=task_ids)
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

    change_outcome.short_description = "Change assigned outcome for selected tasks"

    def make_isadded_false(modeladmin, request, queryset):
        queryset.update(is_done=False)
        modeladmin.message_user(request, "Selected tasks is done property have set to False")

    make_isadded_false.short_description = "Make is added to False"

    actions = [
        change_outcome,
        make_isadded_false
    ]


admin.site.register(Task, TaskAdmin)
