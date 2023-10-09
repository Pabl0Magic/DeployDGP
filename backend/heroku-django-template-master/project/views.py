from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Room
from .forms import RoomForm, FileUploadForm

from django.views import View

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from project.models import ExampleModel
from project.serializers import ExampleModelSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = ExampleModel.objects.all()
	if request.method == 'GET':
		serializer = ExampleModelSerializer(data, many=True)
		return JsonResponse(serializer.data, safe=False)
	

class RoomCreateView(CreateView):
	model = Room
	form_class = RoomForm
	template_name = 'new-sala.html'

class RoomUpdateView(UpdateView):
	model = Room
	fields = ['name', 'size']

class RoomDeleteView(DeleteView):
	model = Room
	template_name = 'delete-sala.html'

class FileUploadView(View):
	def post(self, request):
		form = FileUploadForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return JsonResponse({'message': 'File uploaded succesfully'})
		else:
			return JsonResponse({'message': 'Error uploading file'}, staus=400)
		
		