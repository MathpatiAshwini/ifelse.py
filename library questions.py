expecteddate=int(input("enter the expected date"))
expectedmonth=int(input("enter the expected month"))
expectedyear=int(input("enter the expected year"))
returndate=int(input("enter the return date"))
returnmonth=int(input("enter the return month"))
returnyear=int(input("enter the year"))
if expectedyear==returnyear:
    if expectedmonth==returnmonth:
        if expecteddate==returndate:
            print("no fine")
        else:
            print((returndate - expecteddate)*15)
    else:
        print((returnmonth - expectedmonth)*500)
else:
    print((returnyear - expectedyear)*10000)
                
# a=5-3+(3-5)//2-5+22%5
# print(a)