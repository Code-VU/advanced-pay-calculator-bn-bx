def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    if float(hrs) <=40 :
        print(float(rate) * float(hrs))
    else:
        print("Pay: ",(float(rate) * 40) + (float(rate) * 1.5 * (float(hrs)-40)))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()