from django.contrib.auth.models import User
import django_filters

from django import forms

from dog.models import Breed


class BreedFilter(django_filters.FilterSet):

    #activity_level = django_filters.ModelMultipleChoiceFilter(queryset=Breed.objects.values_list('activity_level', flat=True).distinct(), widget=forms.CheckboxSelectMultiple)

    class Meta:

        model = Breed

        fields = [ 'displayName', 'activity_level', 'coat_length', 'drools', 'good_with_children', 
        'grooming_demand', 'intelligence', 'shedding_level', 'size' ]