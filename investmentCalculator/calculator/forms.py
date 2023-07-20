from django import forms

class InvestmentForm(forms.Form):
    starting_amount = forms.IntegerField(label='Starting Amount', min_value=0)
    number_of_years = forms.IntegerField(label='Number of Years', min_value=0)
    return_rate = forms.FloatField(label='Return Rate', min_value=0, max_value=100)
    annual_additional_contribution = forms.FloatField(label='Annual Additional Contribution', min_value=0)