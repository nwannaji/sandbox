from itertools import chain
from django.shortcuts import render, redirect
from .models import AgriTechSensorData, FinTechSensorData, MedTechSensorData, OtherSensorData
from .forms import AgricTechSensorDataForm,MedTechSensorDataForm,FinTechSensorDataForm,OtherSensorDataForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accelerator/home.html')

@login_required
def add_sensor_data(request):
    industry_type = request.GET.get('industry_type')
    print(industry_type)
    if request.method == 'POST':
        if industry_type == 'AgriTech':
            form = AgricTechSensorDataForm(request.POST, request.FILES)
        elif industry_type == 'MedTech':
            form = MedTechSensorDataForm(request.POST, request.FILES)
        elif industry_type == 'FinTech':
            form = FinTechSensorDataForm(request.POST, request.FILES)
        else:
            form = OtherSensorDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_sensor_data')
    else:
        if industry_type == 'AgriTech':
            form = AgricTechSensorDataForm()
        elif industry_type == 'MedTech':
            form = MedTechSensorDataForm()
        elif industry_type == 'FinTech':
            form = FinTechSensorDataForm()
        else:
            form = OtherSensorDataForm()
    return render(request, 'accelerator/add_sensor_data.html', {'form': form, 'industry_type':industry_type})

@login_required
def view_sensor_data(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort_by', '-timestamp')
    # Fetch and combine querysets efficiently
    agrictech_sensor_data = AgriTechSensorData.objects.all().order_by(sort_by)
    medtech_sensor_data = MedTechSensorData.objects.all().order_by(sort_by)
    fintech_sensor_data = FinTechSensorData.objects.all().order_by(sort_by)
    other_sensor_data = OtherSensorData.objects.all().order_by(sort_by)

    # Combine querysets using itertools.chain
    combined_queryset = list(chain(
        agrictech_sensor_data,
        medtech_sensor_data,
        fintech_sensor_data,
        other_sensor_data
    ))
    # Apply filtering if a query is provided
    if query:
        combined_queryset = [
    data for data in combined_queryset if (
        query.lower() in str(getattr(data, 'industry_type', '')).lower() or
        query.lower() in str(getattr(data, 'sensor_type', '')).lower() or
        query.lower() in str(getattr(data, 'sensor_id', '')).lower() or
        query.lower() in str(getattr(data, 'patient_id', '')).lower() or
        query.lower() in str(getattr(data, 'transaction_id', '')).lower()
    )
]
    paginator =  Paginator(combined_queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'accelerator/view_sensor_data.html', {'page_obj': page_obj})

def analytics_dashboard(request):
    # Fetch data for charts
    agric_data = AgriTechSensorData.objects.all()
    medtech_data = MedTechSensorData.objects.all()
    fintech_data = FinTechSensorData.objects.all()
    other_data = OtherSensorData.objects.all()

    # Prepare data for Chart.js
    context = {
        'agric_labels': [data.timestamp.strftime('%Y-%m-%d %H:%M:%S') for data in agric_data],
        'agric_soil_moisture': [data.soil_moisture for data in agric_data],
        'medtech_heart_rate': [data.heart_rate for data in medtech_data],
        'fintech_transaction_amounts': [float(data.transaction_amount) for data in fintech_data],
        'industry_counts': {
            'AgriTech': agric_data.count(),
            'MedTech': medtech_data.count(),
            'FinTech': fintech_data.count(),
            'Other': other_data.count(),
        },
    }
    return render(request, 'accelerator/data_visualization.html', context)