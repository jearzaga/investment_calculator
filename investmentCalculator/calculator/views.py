from django.shortcuts import render
from django.views import View
from .forms import InvestmentForm
# Create your views here.

class Index(View):
    def get(self, request):
        form = InvestmentForm()
        return render(request, 'calculator/index.html', {'form': form})
    
    def post(self,request):
        form = InvestmentForm(request.POST)