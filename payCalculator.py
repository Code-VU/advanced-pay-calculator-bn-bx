def calculatePay():
    
    # This first line is provided for you, thanks.
    hrs = input("Enter Hours: ")
    rate = input("Enter Rate: ")
    hrsf = float(hrs)
    ratef = float(rate)
    if hrsf <= 40:
        pay = hrsf * ratef
    else:
        pay = (hrsf - 40) * (ratef * 1.5) + (40 * ratef)
    print("Pay: " + str(pay))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()