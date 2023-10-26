print('----------Unit Converter----------')
print()

def convert(value:int,cnv_type):
    
    if type(value) != int and type(value) != float:
        return 'Please enter Degrees in numbers'
    elif int(value) < 0:
        return 'Enter greater than 0'
    elif cnv_type.upper() not in ['C', 'F']:
        return 'Please enter C or F'
  
    if cnv_type.upper() == 'C':
        calc = (value - 32) * 5/9
        return f'The Converted Value: {calc:.1f}°C'
    if cnv_type.upper() == 'F':
        calc = (value * 9/5) + 32
        return f'The Converted Value: {calc:.1f}°F'

    
value = int(input('Enter Degree: '))
cnv = input('Enter What you want to convert C or F: ')
        
x = convert(value,cnv)
print()
print(x)