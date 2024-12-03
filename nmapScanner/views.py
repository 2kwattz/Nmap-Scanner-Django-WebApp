from django.http import HttpResponse
from django.shortcuts import render
from services.models import ContactDetails
import subprocess


def run_nmap(target,scanType,port):

    if scanType == "defaultPingScan":
        command = ["nmap", target]
    elif scanType == "scanPortRange":
        command = ["nmap", "-p", "20-80", target]
    elif scanType == "tcpConnectionScan":
        command = ["nmap", "-sT", target]
    elif scanType == "disablePingScan":
        command = ["nmap", "-Pn", target]
    elif scanType == "verboseOutput":
        command = ["nmap", "-Pn", target]
    elif scanType == "aggressiveScan":
        command = ["nmap", "-A", target]
    elif scanType == "scanPort":
        command = ["nmap", "-p", port, target]
    
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

def index(request):
    # data = {
    #     'title':'HealthCheck',
    #     'desc':'Welcome to the Health Check Monitoring App for nmapScanner',
    #     'available_ports': [80,443,8080,8081,8000,3000],
    #     'numbers': [1,6,34,45,12,43,56,23,56,57],
    #     'port_details': [{'Port': 80,'WebApp':'MainServer'},{'Port': 3000,'WebApp': 'CustomApp1'}]
    # }

    # contactDetailsData = ContactDetails.objects.all().order_by('-fullName')[:4]


    # return render(request,"index.html",{'ContactDetails': contactDetailsData})

    try:
        if request.method == "GET":
            
            response = ""
            return render(request, "index.html")
        elif request.method == "POST":

            ipAddress = request.POST.get('ipAddress')
            port = request.POST.get('port')
            scanType = request.POST.get('scanType')

            print(type(ipAddress))  # Check if the variable is a set


            response = run_nmap(ipAddress,scanType,port)

            print("Type of response",response)
            

            return render(request, "index.html",{"response":response})
    except Exception as e:
        print("Error", e)
        return render(request, "index.html",{'response':e})


def dynamicRouteTest(request,courseid):
    print("Course Id", courseid)
    return HttpResponse(f"HealthCheck Server. Course Id {courseid}")

def contactForm(request):

    try:

        if request.method == "POST":

            try:
            
                fullName = request.POST.get('fullName')
                description = request.POST.get('description')
                subject = request.POST.get('subject')
                email = request.POST.get('email')

                print("Full Name ", fullName)
                print("Description ", description)
                print("Subject", subject)
                print("Email",email)

                contactData = ContactDetails(fullName=fullName, description=description, subject=subject,email=email)

                contactData.save()

                return render(request, 'contactForm.html', {'message':'Your input has been recieved'})
            
            except Exception as e:
                return render(request, 'contactForm.html', {'message': e})
            
            except:
                pass
                
        

        elif request.method == "GET":
            return render(request, 'contactForm.html')
    except:
        pass


def userForms(request):
    print("In User Forms Route")
    try:

        if request.method =="POST":
            number = request.POST.get('text')
    except:
        pass

    return render(request,'form.html')

