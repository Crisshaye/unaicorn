from django.shortcuts import render
from . import fake_predict
from . import ml_model

def home(request):
	return render(request,'index.html')

def results(request):

#parameter pclass,sex,age,sibsp,parch,fare,embarked,title
	user_input_pclass = int(request.GET['pclass'])
	user_input_sex = int(request.GET['sex'])
	user_input_age = int(request.GET['age'])
	user_input_sibsp = int(request.GET['sibsp'])
	user_input_parch = int(request.GET['parch'])
	user_input_fare = int(request.GET['fare'])
	user_input_embarked = int(request.GET['embarked'])
	user_input_title = int(request.GET['title'])
	prediction = ml_model.prediction_model(user_input_pclass,user_input_sex,user_input_age,user_input_sibsp,user_input_parch,user_input_fare,user_input_embarked,user_input_title)
	return render(request,'results.html',{'prediction':prediction})