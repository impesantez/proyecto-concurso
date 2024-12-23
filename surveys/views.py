from django.shortcuts import render, redirect
from .forms import ElectricitySurveyForm

def survey_view(request):
    if request.method == "POST":
        form = ElectricitySurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('survey_thanks')
    else:
        form = ElectricitySurveyForm()
    return render(request, 'survey.html', {'form': form})
