import requests
from bs4 import BeautifulSoup

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



#getting time
def get_time():
    html_text = requests.get("https://www.timeanddate.com/worldclock/india/visakhapatnam").text

    soup = BeautifulSoup(html_text, 'lxml')
    block = soup.find('section', class_='bk-focus')
    divi = block.find('div', id='qlook', class_='bk-focus__qlook')
    time = divi.find('span', id='ct', class_='h1').text
    return time