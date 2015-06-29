##################################################
# PSET 2
#
# Part 1
#
##################################################

'''
For each month print
  Month: 1
  Minimum monthly payment: 96.0
  Remaining balance: 4784.0
At end of year print
  Total paid: 96.0
  Remaining balance: 4784.0
  
  
Monthly interest rate= (Annual interest rate) / 12.0 --DONE
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

ex:
    Month: 1
    Minimum monthly payment: 168.52
    Remaining balance: 4111.89
    
round(num, 2) #number, digits after decimal
'''
balance = 4842.0
annualInterestRate = 0.2
monthlyPaymentRate = .04


paid = 0.0
monthlyinterest = annualInterestRate / 12
for m in range(1,13):
    prevbalance = balance
    minpay = (balance * monthlyPaymentRate)
    unpaybal = prevbalance - minpay
    balance = round((unpaybal + (monthlyinterest * unpaybal)),2)
    paid += minpay
    print('Month: ' + str(m))
    print('Minimum monthly payment: ' + str(round(minpay,2)))
    print('Remaining balance: '+ str(balance))
print('Total Paid: ' + str(round(paid,2)))
print('Remaining: ' + str(balance))


##################################################
# PSET 2
#
# Part 2
#
##################################################
'''
The program should print out one line: the lowest monthly payment that will pay 
off all debt in under 1 year, for example:

Assume that the interest is compounded monthly 
according to the balance at the end of the month 
(after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance
to become negative using this payment scheme, which is okay. 

A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''

balance = 4473
annualInterestRate = 0.2

monthlyInt = annualInterestRate / 12.0

fixed = balance / 12
#maxpay = balance + (balance * annualInterestRate)
origBalance = balance

while fixed % 10 != 0:
    fixed += 1

maxpay = 0.0 

for m in range(12):
    unpaid = balance - 1
    balance = unpaid + (monthlyInt * unpaid)
    maxpay = balance
print(unpaid)

while unpaid < maxpay:
    balance = origBalance
    for m in range(12):
        unpaid = balance - fixed
        print('unpaid : ' + str(unpaid))
        balance = unpaid + (monthlyInt * unpaid)
        print('fixed amount : '+ str(fixed) + ' balance: ' + str(balance))
    if unpaid  > 0:
        print('need to pay more than '+ str(fixed) + ' per month')
        fixed += 10
    else:
        break
print(fixed)


balance = 4842.0
annualInterestRate = 0.2
#monthlyPaymentRate = .04


paid = 0.0
monthlyinterest = annualInterestRate / 12
minpay = balance / 12
while paid <= balance:
    prevbalance = balance
    minpay = 
    unpaybal = prevbalance - minpay
    balance = round((unpaybal + (monthlyinterest * unpaybal)),2)
    paid += minpay







print('Lowest Payment: ' + str(round(fixed,2)))
#3329 => 310