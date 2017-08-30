#Built-in data types
print('___Data types___')
language = "Python" #str
print(language)

version = 3 #int
print(version)

sub_version = 0.1 #float
print(sub_version)

is_high_level_language = True #boolean
print(is_high_level_language)

#Addition
print('___Addition___')
print(5 + 5) #10
#print(5 + '5') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print('5' + 5) #TypeError: must be str, not int
print('5' + '5') #55
print(1.0 + 5) #6.0
print(-1 + 5) #4

#Subtraction
print('___Subtraction___')
print(-1 -5) #-6
print(6 - 1) #5
print(6.0 - 1) #5.0
#print(6 - '1') #TypeError: unsupported operand type(s) for -: 'int' and 'str'
#print('6' - 1) #TypeError: unsupported operand type(s) for -: 'str' and 'int'
#print('5' - '5') #TypeError: unsupported operand type(s) for -: 'str' and 'str'

#Multiplication
print('___Multiplication___')
print(2 * 5) #10
print(2.0 * 5) #10.0
print(-2 * 5 ) #-10
print(2 * -5 ) #-10
print(-2 * -5 ) #10
print('2' * 5) #22222
print('2' * -5) #
#print('2' * '5') #TypeError: can't multiply sequence by non-int of type 'str'

#Division
print('___Division___')
print(10 / 5) #2.0
print(10.0 / 5) #2.0
print(-10 / 5 ) #-2.0
print(10 / -5 ) #-2.0
print(-10 / -5 ) #2.0
#print('10' / 5) #TypeError: unsupported operand type(s) for /: 'str' and 'int'
#print('10' / -5) #TypeError: unsupported operand type(s) for /: 'str' and 'int'
#print('10' / '5') #TypeError: unsupported operand type(s) for /: 'str' and 'str'

#Floor Division / Quotient
print('___Floor Division / Quotient___')
print(11 // 5) #2
print(11.0 // 5) #2.0
print(-11 // 5 ) #-3
print(11 // -5 ) #-3
print(-11 // -5 ) #2
#print('10' // 5) #TypeError: unsupported operand type(s) for //: 'str' and 'int'
#print('10' // -5) #TypeError: unsupported operand type(s) for //: 'str' and 'int'
#print('10' // '5') #TypeError: unsupported operand type(s) for /: 'str' and 'str'

#Modulo / Remainder
print('___Modulo / Remainder___')
print(11 % 5) #1
print(11.0 % 5) #1.0
print(-11 % 5 ) #4
print(11 % -5 ) #-4
print(-11 % -5 ) #-1
#print('10' % 5) #TypeError: not all arguments converted during string formatting
#print('10' % -5) #TypeError: not all arguments converted during string formatting
#print('10' % '5') #TypeError: not all arguments converted during string formatting

#Exponent
print('___Exponent___')
print(2 ** 2) #4
print(2 ** -2) #0.25
print(-2 ** 2) #-4
print(-2 ** -2) #-0.25
#print(2 ** '2') #TypeError: unsupported operand type(s) for ** or pow(): 'int' and 'str'
#print('2' ** 2) #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
#print('2' ** '2') #TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'

