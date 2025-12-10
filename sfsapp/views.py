from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import StudentModel
from folium import *

# Create your views here.
def home(request):
	data = StudentModel.objects.all()
	return render(request,"home.html",{'data':data})

def create(request):
	fm = StudentForm()
	if request.method == "POST":
		data = StudentForm(request.POST,request.FILES)
		if data.is_valid():
			data.save()
			msg = "record created"
			return render(request,"create.html",{'fm':fm,'msg':msg})
		else:
			msg = "Check issue"
			return render(request,"create.html",{'fm':data,'msg':msg})
	else:
		return render(request,"create.html",{'fm':fm})

def delete(request,i):
	st = get_object_or_404(StudentModel,rno=i)
	if request.method=="POST":
		st.ms.delete()
		st.delete()
		return redirect("home")
	else:
		return render(request,"delete.html",{'st':st})

def locate(request):
	loc = [19.1872 , 72.9739]
	f = Figure(width=1000,height=600)
	thane = Map(location=loc,zoom_start=20).add_to(f)
	Marker(loc,tooltip="Kamal classes thane").add_to(thane)
	thane_html = thane._repr_html_()
	return render(request,"locate.html",{'msg':thane_html})