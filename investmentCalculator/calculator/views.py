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
        
        if form.is_valid():
            total_result = form.cleaned_data['starting_amount']
            total_interest = 0
            yearly_results = {}
            return_rate = form.cleaned_data['return_rate']
            
            for i in range(1, int(form.cleaned_data['number_of_years'] + 1)):
                yearly_results[i] = {}
                
                # calculate interest
                interest = total_result * (form.cleaned_data['return_rate'] / 100)
                total_result += interest
                total_interest += interest
                
                #add additional contribution
                total_result += form.cleaned_data['annual_additional_contribution']
                
                # set values for year
                yearly_results[i]['interest'] = round(total_interest, 2)
                yearly_results[i]['total'] = round(total_result, 2)
                
                #create list of years
                context = {
                    'total_result': round(total_result, 2),
                    'yearly_results': yearly_results,
                    'number_of_years': int(form.cleaned_data['number_of_years']),
                }
                
                # set the return rate 
                context['return_rate'] = int(form.cleaned_data['return_rate'])
                

        # render the template
        return render(request, 'calculator/result.html', context)

                
            
            