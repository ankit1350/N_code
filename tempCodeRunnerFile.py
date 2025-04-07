def is_leap(year):
    leap = False
    
    if (year%400==0) and (year%4==0) and year<=100000 and year>=1900:
        return True
  
 
    
    return leap

try:
    year = int(input('Enter year: '))
    print('You entered:', year)
except ValueError:
    print('Invalid input! Please enter a valid number.')
print(is_leap(year))