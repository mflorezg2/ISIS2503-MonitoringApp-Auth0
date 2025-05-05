from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .serializers import PacienteSerializer
from .forms import PacienteForm

# --- API REST endpoints (DRF) ---
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = get_object_or_404(Paciente, pk=kwargs['pk'])
        return Response(self.get_serializer(obj).data)

    def create(self, request, *args, **kwargs):
        serializer = PacienteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

# --- HTML views (lista, create, detail) ---
def patient_list(request):
    return render(request, 'patients/patient_list.html', {'patients': Paciente.objects.all()})

def patient_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PacienteForm()
    return render(request, 'patients/patient_create.html', {'form': form})

def patient_detail(request, pk):
    p = get_object_or_404(Paciente, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': p})

