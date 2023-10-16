from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

<<<<<<< Updated upstream
from project.models import ExampleModel
from project.serializers import ExampleModelSerializer
=======
def index(request):
	return render(request, 'upload.html')
class Home(generic.ListView):

    model = Room
    template_name = 'home.html'

class RoomCreateView(CreateView):
	model = Room
	form_class = RoomForm
	template_name = 'upload.html'

class RoomUpdateView(UpdateView):
	model = Room
	fields = ['name', 'size']

class RoomDeleteView(DeleteView):
	model = Room
	template_name = 'delete-sala.html'
>>>>>>> Stashed changes

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = ExampleModel.objects.all()
	if request.method == 'GET':
		serializer = ExampleModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)