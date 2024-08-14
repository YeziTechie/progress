from django.views import View
from django.urls import reverse
from django.shortcuts import get_object_or_404, render, redirect\


from abilities.models.outcome import Outcome


class HideOutcome(View):
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        outcome = get_object_or_404(Outcome, pk=pk)
        if outcome.is_hided is False:
            outcome.is_hided = True
        else:
            outcome.is_hided = False
        outcome.save()
        return redirect(reverse('outcome_detail', kwargs={'pk': pk}))

    def get(self, request, *args, **kwargs):
        outcome = get_object_or_404(Outcome, pk=self.kwargs['pk'])
        return render(request, 'hide.html', {'outcome': outcome})
