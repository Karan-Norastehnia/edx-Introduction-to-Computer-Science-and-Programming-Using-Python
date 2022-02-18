balance = 320000
annualInterestRate = 0.2

#==========================================

lowestPay = 0
initialBalance = balance

while balance > 0:
    lowestPay += 10
    balance = initialBalance
    for i in range(1,13):
        balance -= lowestPay
        balance += annualInterestRate/12*balance

print('Lowest Payment: ', lowestPay)