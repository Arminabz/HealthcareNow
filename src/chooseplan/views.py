from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import chooseplanform
from .models import questions

# python local setting
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import psycopg2
import re
import pprint 
from itertools import chain

engine = create_engine("postgres+psycopg2://postgres:12221992@localhost:5432")
connection = engine.connect()
metadata = MetaData()
HCT = Table('Healthcare_Categories', metadata, autoload=True, autoload_with=engine)

Health_Care_Plans  =    [
                        {'Sharp_Silver_70_HMO____': {"Specialist": '3S', 'Preventive_Care': "1PC", "Diagnostic_Test": "3DT", "Generic_Drugs": "4GD",
"Outpatien_Surgery":'3OS', 'Immediate_Medical_Attention': '3IMA', 'Outpatient_Services/Inpatient_Services': '1OSIS', 'Pregnant': "2P", 'Home_Health_Care': '3HHC',
'Rehabilitation_Services': '3RS', 'Skilled_Nursing_Care': '3SNC'}},
                        {'Kaiser_Covered_California_Silver_87_HMO____' : {"Specialist": '1S', 'Preventive_Care': "2PC", "Diagnostic_Test": "1DT", "Generic_Drugs": "2GD",
"Outpatien_Surgery":'1OS', 'Immediate_Medical_Attention': '2IMA', 'Outpatient_Services/Inpatient_Services': '3OSIS', 'Pregnant': "4P", 'Home_Health_Care': '2HHC',
'Rehabilitation_Services': '1RS', 'Skilled_Nursing_Care': '2SNC'}},
                        {'LA_Coverd_Silver_70_HMO____' : {"Specialist": '4S', 'Preventive_Care': "3PC", "Diagnostic_Test": "2DT", "Generic_Drugs": "3GD",
"Outpatien_Surgery":'4OS', 'Immediate_Medical_Attention': '4IMA', 'Outpatient_Services/Inpatient_Services': '4OSIS', 'Pregnant': "3P", 'Home_Health_Care': '4HHC',
'Rehabilitation_Services': '4RS', 'Skilled_Nursing_Care': '4SNC'}},
                        {'Blue_Shield_87_PPO_Silver____' : {"Specialist": '2S', 'Preventive_Care': "4PC", "Diagnostic_Test": "1DT", "Generic_Drugs": "1GD",
"Outpatien_Surgery":'2OS', 'Immediate_Medical_Attention': '1IMA', 'Outpatient_Services/Inpatient_Services': '2OSIS', 'Pregnant': "1P", 'Home_Health_Care': '1HHC',
'Rehabilitation_Services': '2RS', 'Skilled_Nursing_Care': '1SNC'}}
]



# def chooseplan(request):
#     return render(request, 'chooseplan/chooseplan.html')

def chooseplan(request):
    if request.method == 'POST':
        form = chooseplanform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_chooseplan")
    else:
        form = chooseplanform()
    return render(request, 'chooseplan/chooseplan.html', {'form': form})


def show_chooseplan(request):
    try:
        test_result = match_code1(ret_code1(get_data1("self")))
        if test_result == []:
            test_result = "no answers checked"
    except:
        test_result = "no answers checked"

    return HttpResponse(test_result)

def ret_code(provider_list):
    healthlist = [ ]
    for i in provider_list:
        ilist = list(i)
        for b in range (len(ilist)):
            if '32S' and '20S' in ilist:
                healthlist.append("1S")
            if '12PC' and '14PC' in ilist:
                healthlist.append("1PC")
            if '10DT' and '42DT' in ilist:
                healthlist.append("1DT")
            if '8GD' and '18GD' in ilist:
                healthlist.append("1GD")
            if '44OS' and '26OSSNC' in ilist:
                healthlist.append("1OS")
            if '36IMA' and '24IMARS' in ilist:
                healthlist.append("1IMA")
            if '34OSIS' and '40OSIS' in ilist:
                healthlist.append("1OSIS")
            if '16P' and '30P' in ilist:
                healthlist.append("1P")
            if '48HHC' and '46HHC' in ilist:
                healthlist.append("1HHC")
            if '38RS' and '24IMARS' in ilist:
                healthlist.append("1RS")
            if '28SNC' and '26OSSNC' in ilist:
                healthlist.append("1SNC")
            return healthlist

def match_code(hcp):
    final_outcome = [ ]
    final_outcome_improved = [ ]
    for mc in hcp:
        for hp in Health_Care_Plans:
            for plans in hp.values():
                for plans_attributes in plans.values():
                    if mc in plans_attributes:
                        final_outcome.append(list(hp.keys()))
                        for f in final_outcome:
                            if f not in final_outcome_improved:
                                final_outcome_improved.append(f)
                                finalized = list(chain(*final_outcome_improved))
    return (finalized)

# =================================

def get_data1(self):
    stmt = 'Select * From public."chooseplan_questions" Order By id DESC LIMIT 1'
    result_proxy = connection.execute(stmt)
    results = result_proxy.fetchall()
    return results



def ret_code1(provider_list):
    healthlist = [ ] 
    for i in provider_list:
        ilist = list(i)
        for b in range (len(ilist)):
            if '32S' and '20S' in ilist:
                healthlist.append("1S")
            if '12PC' and '14PC' in ilist:
                healthlist.append("1PC")
            if '10DT' and '42DT' in ilist:
                healthlist.append("1DT")
            if '8GD' and '18GD' in ilist:
                healthlist.append("1GD")
            if '44OS' and '26OSSNC' in ilist:
                healthlist.append("1OS")
            if '36IMA' and '24IMARS' in ilist:
                healthlist.append("1IMA")
            if '34OSIS' and '40OSIS' in ilist:
                healthlist.append("1OSIS")
            if '16P' and '30P' in ilist:
                healthlist.append("1P")
            if '48HHC' and '46HHC' in ilist:
                healthlist.append("1HHC")
            if '38RS' and '24IMARS' in ilist:
                healthlist.append("1RS")
            if '28SNC' and '26OSSNC' in ilist:
                healthlist.append("1SNC")
            return healthlist

def match_code1(hcp):
    final_outcome = [ ]
    final_outcome_improved = [ ]
    finalized = []
    for mc in hcp:
        for hp in Health_Care_Plans:
            for plans in hp.values():
                for plans_attributes in plans.values():
                    if mc in plans_attributes:
                        final_outcome.append(list(hp.keys()))
                        for f in final_outcome:
                            if f not in final_outcome_improved:
                                final_outcome_improved.append(f)
                                finalized = list(chain(*final_outcome_improved))
    return (finalized)

