"""
Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут показывать
показывать электронный часы в этот момент. Программа должна вывести два числа: количество часов
(от 0 до 23) и количество минут (от 0 до 59). Учтите, что число n может быть больше, чем количество минут в сутках.

"""


n=int (input ("Введите количество минут, прошедшее с начала суток:"))
while n>=1440:
   n=n-1440
print ("Время на часах -",(n//60),":",n-60*(n//60))

