day=int(input('Enter the day'))
month=int(input('Enter the month'))
year=int(input('Enter the year'))
if(day>30):
    print('date is invalid')
else:
    if(month>13):
        print('date is invalid')
    else:
         print(day,'/',month,'/',year,'date is valid')
