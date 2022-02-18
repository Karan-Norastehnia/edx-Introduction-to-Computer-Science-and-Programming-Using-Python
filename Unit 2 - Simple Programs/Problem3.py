balance = 320000
annualInterestRate = 0.2

#==========================================

lowestPay = 0
initialBalance = balance
low = balance/12
high = balance*(1 + annualInterestRate/12)**12/12

print(low, high)

while True:
    lowestPay = (low + high)/2
    balance = initialBalance
    for i in range(1,13):
        balance -= lowestPay
        balance += annualInterestRate/12*balance
    balance = round(balance, 2)
    if balance > 0: low = lowestPay
    elif balance < 0: high = lowestPay
    else: break

print('Lowest Payment: ', round(lowestPay, 2))