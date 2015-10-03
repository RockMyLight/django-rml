from django.shortcuts import render


# Create your views here.
def main(request):
    context = {}
    return render(request, 'rml/main.html', context)


def jam(request):
    context = {}
    return render(request, 'rml/jam.html', context)
