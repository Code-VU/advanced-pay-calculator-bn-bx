def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    othrs = float(hrs) - 40
    otrate = float(rate) * 1.5
    newhrs = float(hrs) - float(othrs)
    pay = float(newhrs)*float(rate)
    otpay = float(othrs) * float(otrate)
    totalpay = (pay) + (otpay)
    print (totalpay)
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()