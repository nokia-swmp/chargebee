from django.shortcuts import render
import sys
sys.path.insert(0, '..')
from source import getNames

def table(request):
    usage = getNames.initUsage()

    return render(
            request,
            'base_table.html',
            context={'usage': usage},
        )
