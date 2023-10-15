from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Room
from .forms import RoomForm, FileUploadForm

from django.views import View, generic

from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

class Home(generic.ListView):

    model = Room
    template_name = 'home.html'

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
		
		