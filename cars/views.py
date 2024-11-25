from django.urls import reverse_lazy
from .models import Cars
from .forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class CarsListView(ListView):
    model = Cars
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search).order_by('model')        
        return cars
    

class CarDetailView(DetailView):
    model = Cars
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'create_car.html'
    success_url = '/cars/'



@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Cars
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk':self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Cars
    template_name = 'car_detele.html'
    success_url = '/cars/'


