# Написати програму, яка отримує дані про курси валют з сайтів кількох банків,
# накопичує отримані дані у файлі та дає змогу на вимогу користувача
# вивести графіки зміни курсів за заданий період, а також виконувати
# певне прогнозування майбутніх курсів.
import datetime
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(options=options, executable_path=r'C:\important_gavno\chromedriver.exe')
now = datetime.datetime.now()
driver.get(f"https://bank.gov.ua/ua/markets/exchangerates?date={now.strftime('%d.%m.%Y')}&period=daily")
elem = driver.find_element_by_css_selector("#exchangeRates > tbody > tr:nth-child(8) > td:nth-child(5)")
cur = (str(elem.text)).replace(',', '.')
print(f"Today's course of euro is: {cur}")
driver.close()
file = open("data.txt", "r")
cont = file.readlines()
file.close()

last = cont[len(cont)-1].split()
file = open("data.txt", "a")

if last[0] != now.strftime("%d-%m-%Y"):
    file.write(f'\n{now.strftime("%d-%m-%Y")} {cur} ')
    cont.append(f'\n{now.strftime("%d-%m-%Y")} {cur} ')
file.close()

axis_x = []
axis_y = []
for i in cont:
    data = i.split()
    axis_x.append(data[0][:-5])
    axis_y.append(float(data[1]))
a11 = 0
a21 = 0
a22 = len(cont)
c1 = 0
c2 = 0
x = 1
for i in range(a22):
    a11 += x**2
    a21 += x
    c1 += x * axis_y[i]
    c2 += axis_y[i]
    x += 1
# a12 == a21
k = (c1 * a22 - a21 * c2) / (a11 * a22 - a21 * a21)
b = (a11 * c2 - c1 * a21) / (a11 * a22 - a21 * a21)

y1 = k * 0 + b
y2 = k * x + b

print(f"Tomorrow's prediction is: {round(y2, 4)}")
plt.plot([0, x], [y1, y2])
plt.plot(axis_x, axis_y, marker='o')
plt.legend(['Prediction', 'Rate'])
plt.title('Hryvnia exchange rate against Euro currence', fontsize=12, loc='center')
plt.xlabel(f"Tomorrow's prediction is: {round(y2, 4)}", fontsize=10)
plt.grid(True)
plt.show()









