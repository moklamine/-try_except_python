def computepay(hrs, rt):
    if hrs > 35 :
        sal = 35 * rt
        sal_sup = (hrs - 35) * 1.5 * rt
        p = sal + sal_sup
    else :
        p = hrs * rt
    return p

hours = input("Enter your hours: ")
rate = input("Enter your rate: ")

try:
    hrs = float(hours)
    rt = float(rate)
   
except:
    print("Error!")
    quit()

p = computepay(hrs,rt)
print("Pay", p)