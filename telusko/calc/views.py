from cx_Oracle import DatabaseError
from django.shortcuts import render
from.models import Destination,Masjid
from django.http import HttpResponse
from django.db import connection
from . import functions
import requests
from bs4 import BeautifulSoup
import cv2


# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Django'})
    #return HttpResponse('hi')

def nasir(request):
    return render(request,'nasir.html')

def travello(request):

    dests = Destination.objects.all()

    return render(request,'index.html',{'dests':dests})

def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1+val2
    return render(request,"result.html",{'result' : res})

def restapi(request):
    tab = request.POST['tab']
    tab= tab.upper()
    print(tab)
    qr1 = "SELECT * FROM " + tab
    print(qr1)
    qr2 = "SELECT column_name FROM all_tab_columns  WHERE table_name = '"+ tab+"'"
    print(qr2)
    try:
        with connection.cursor() as cursor:
            cursor.callproc('django_debug_log', ['calc/views.py'])
            cursor.execute(qr1)
            data = cursor.fetchall()
            cursor.execute(qr2)
            col_data = cursor.fetchall()
    except Exception as e:
        err = e.__str__()
        return HttpResponse('<h2>Request 404</h2><br>'+err)
    else:
        return render(request, 'restapi.html',{'db_data': data,'col':col_data,'tab_name':tab})

def table(request):
    dests = Destination.objects.all()
    masjid  = Masjid.objects.all()
    return render(request, 'table.html',{'dests':dests,'masjid':masjid})

def camera(request):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

    return render(request, 'home.html', {'name': 'Django'})

def q1(request):
    strq1 = request.POST['str1']
    val = strq1
    v_i = []

    for ele in range(len(val)):
        if val[ele] in "aeiou":
            v_i.append(ele)

    hun_m = [x * 100 for x in v_i]

    map_object1 = map(functions.prime_c, hun_m)
    sum_prime = list(map_object1)

    map_object2 = map(functions.getSum, sum_prime)
    digit_count = list(map_object2)

    s = val
    indx = v_i
    rplx = digit_count
    str1 = []
    j = 0
    for i in range(0, len(s)):
        if i in indx:
            str1.append(rplx[j])
            j = j + 1
        else:
            str1.append(s[i])

    f_str = [str(x) for x in str1]
    finalString = ''.join(f_str)

    print('Output is :')
    print(finalString)
    return render(request, "q1.html", {'result': finalString})


def time(request):
    time = get_time()
    print(time)
    return render(request, 'time.html',{'time':time})


def get_time():
    html_text = requests.get("https://www.timeanddate.com/worldclock/india/visakhapatnam").text

    soup = BeautifulSoup(html_text, 'lxml')
    block = soup.find('section', class_='bk-focus')
    divi = block.find('div', id='qlook', class_='bk-focus__qlook')
    time = divi.find('span', id='ct', class_='h1').text
    return time