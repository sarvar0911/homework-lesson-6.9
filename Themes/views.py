from django.shortcuts import render
from .models import Theme


def themes_list(request):
    themes = Theme.objects.all()
    return render(request, 'Themes/themes_list.html', {'themes': themes})
