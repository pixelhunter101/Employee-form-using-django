from django.shortcuts import render

# Create your views here.
def form(request1):
    print("Employee form")
    return render(request1, 'details.html')

def info(request2):
       Name = request2.POST['name']
       Password = request2.POST['pass']
       Address = request2.POST['address']
       City = request2.POST['City']
       Gender = request2.POST['gender']
       Vehicle = request2.POST['vehicle']
       Salary = request2.POST['salary']
       Date_of_Birth = request2.POST['date_of_birth']
       return render (request2, 'result.html', {'result': Name, 'Password':Password , 'Address': Address , 'City' : City , 'Gender': Gender , 'Vehicle' : Vehicle, 'Salary' : Salary , 'Date_of_Birth' : Date_of_Birth})