from django.shortcuts import render
from django.views.generic import View
from .forms import EnergyForm, CurrentForm, CollisionProbabilityForm
import math

def home_page(request):
    return render(request, 'lab_one/lab_one.html')



class Energy(View):
    def get(self, request):
        form = EnergyForm()
        return render(request, 'lab_one/energy.html', context = {'form': form} )

    def post(self, request):
        form = EnergyForm(request.POST)
        if form.is_valid():
            energy_1 = form.cleaned_data['uc_1'] * 1.6 * 10 ** -19
            energy_2 = form.cleaned_data['uc_2'] * 1.6 * 10 ** -19
            energy_3 = form.cleaned_data['uc_3'] * 1.6 * 10 ** -19
            energy_4 = form.cleaned_data['uc_4'] * 1.6 * 10 ** -19
            energy_5 = form.cleaned_data['uc_5'] * 1.6 * 10 ** -19
            energy_6 = form.cleaned_data['uc_6'] * 1.6 * 10 ** -19
            energy_7 = form.cleaned_data['uc_7'] * 1.6 * 10 ** -19
            energy_8 = form.cleaned_data['uc_8'] * 1.6 * 10 ** -19
            energy_9 = form.cleaned_data['uc_9'] * 1.6 * 10 ** -19
            energy_10 = form.cleaned_data['uc_10'] * 1.6 * 10 ** -19

            energys = [
                energy_1, energy_2, energy_3, energy_4, energy_5, energy_6, energy_7, energy_8, energy_9, energy_10
            ]

        return render(request, 'lab_one/answer_energy.html', context = {'energys': energys} )


class Current(View):
    def get(self, request):
        current_form = CurrentForm()
        return render(request, 'lab_one/current.html', context = {'current_form': current_form } )

    def post(self, request):
        current_form = CurrentForm(request.POST)
        if current_form.is_valid():
            collision_probability_1  = 1 -  current_form.cleaned_data['ia_1'] / (current_form.cleaned_data['ic_1'] * 0.525)
            collision_probability_2  = 1 -  current_form.cleaned_data['ia_2'] / (current_form.cleaned_data['ic_2'] * 0.525)
            collision_probability_3  = 1 -  current_form.cleaned_data['ia_3'] / (current_form.cleaned_data['ic_3'] * 0.525)
            collision_probability_4  = 1 -  current_form.cleaned_data['ia_4'] / (current_form.cleaned_data['ic_4'] * 0.525)
            collision_probability_5  = 1 -  current_form.cleaned_data['ia_5'] / (current_form.cleaned_data['ic_5'] * 0.525)
            collision_probability_6  = 1 -  current_form.cleaned_data['ia_6'] / (current_form.cleaned_data['ic_6'] * 0.525)
            collision_probability_7  = 1 -  current_form.cleaned_data['ia_7'] / (current_form.cleaned_data['ic_7'] * 0.525)
            collision_probability_8  = 1 -  current_form.cleaned_data['ia_8'] / (current_form.cleaned_data['ic_8'] * 0.525)
            collision_probability_9  = 1 -  current_form.cleaned_data['ia_9'] / (current_form.cleaned_data['ic_9'] * 0.525)
            collision_probability_10  = 1 -  current_form.cleaned_data['ia_10'] / (current_form.cleaned_data['ic_10'] * 0.525)


            collision_probabilitys = [
                collision_probability_1, collision_probability_2, collision_probability_3, collision_probability_4,
                collision_probability_5, collision_probability_6, collision_probability_7, collision_probability_8,
                collision_probability_9, collision_probability_10
            ]

        return render(request, 'lab_one/answer_current.html', context = {'collision_probabilitys': collision_probabilitys} )


class CollisionProbability(View):
    def get(self, request):
        collision_probability_form = CollisionProbabilityForm()
        return render(request, 'lab_one/interaction_section.html', context = {'collision_probability_form': collision_probability_form } )

    def post(self, request):
        collision_probability_form = CollisionProbabilityForm(request.POST)
        if collision_probability_form.is_valid():
            interaction_section_1 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_1'])
            interaction_section_2 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_2'])
            interaction_section_3 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_3'])
            interaction_section_4 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_4'])
            interaction_section_5 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_5'])
            interaction_section_6 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_6'])
            interaction_section_7 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_7'])
            interaction_section_8 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_8'])
            interaction_section_9 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_9'])
            interaction_section_10 = (- 1 / collision_probability_form.cleaned_data['substance_quantity'] * 0.007) * math.log(1 - collision_probability_form.cleaned_data['ps_10'])

            interaction_sections = [
                interaction_section_1, interaction_section_2, interaction_section_3,
                interaction_section_4, interaction_section_5, interaction_section_6,
                interaction_section_7, interaction_section_8, interaction_section_9,
                interaction_section_10
            ]


        return render(request, 'lab_one/answer_interaction_section.html', context = {'interaction_sections': interaction_sections} )
