from cx_Oracle import DatabaseError
from django.shortcuts import render
from.models import Destination,Masjid
from django.http import HttpResponse
from django.db import connection


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

def q1(request):
    strq1 = request.POST['str1']
    val = strq1
    v_i = []

    for ele in range(len(val)):
        if val[ele] in "aeiou":
            v_i.append(ele)

    hun_m = [x * 100 for x in v_i]

    map_object1 = map(prime_c, hun_m)
    sum_prime = list(map_object1)

    map_object2 = map(getSum, sum_prime)
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


def prime_c(upto):
    # to fetch the sum of n prime numbers
    sum = 0

    for num in range(1, upto + 1):

        i = 1

        for i in range(2, num):
            if (int(num % i) == 0):
                i = num
                break;

        # If the number is prime then add it.
        if i is not num:
            sum += num
    return sum


def getSum(n):
    # to fetch sum of digits
    sum = 0
    for digit in str(n):
        sum += int(digit)
    if sum >= 10:
        k = sum
        sum = 0
        for digit in str(k):
            sum += int(digit)
        if sum >= 10:
            j = sum
            sum = 0
            for digit in str(j):
                sum += int(digit)
        return sum
    else:
        return sum