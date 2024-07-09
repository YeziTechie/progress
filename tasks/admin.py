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

    def make_is_added_false(modeladmin, request, queryset):
        queryset.update(is_added=False)
        modeladmin.message_user(request, "is added false")

    def make_is_added_true(modeladmin, request, queryset):
        queryset.update(is_added=True)
        modeladmin.message_user(request, "is added true")

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

    make_is_added_false.short_description = "is added false"
    make_is_added_true.short_description = "is added true"
    make_is_done_false.short_description = "is done false"
    make_is_done_true.short_description = "is done true"
    change_outcome.short_description = "Change assigned outcome for selected tasks"
    save_task.short_description = "Save tasks"

    actions = [
        make_is_added_true,
        make_is_added_false,
        make_is_done_false,
        make_is_done_true,
        change_outcome,
        save_task,
    ]


admin.site.register(Task, TaskAdmin)
