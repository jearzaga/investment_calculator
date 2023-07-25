from django import forms

class InvestmentForm(forms.Form):
    starting_amount = forms.IntegerField(label='Starting Amount', min_value=0)
    number_of_years = forms.IntegerField(label='Number of Years', min_value=0)
    return_rate = forms.FloatField(label='Return Rate', min_value=0, max_value=100)
    annual_additional_contribution = forms.FloatField(label='Annual Additional Contribution', min_value=0)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_to_update = [
            'starting_amount',
            'number_of_years',
            'return_rate',
            'annual_additional_contribution'
        ]

        for field_name in fields_to_update:
            self.fields[field_name].widget.attrs.update({
                'class': 'form-control',
                'style': 'color: black;',
                })