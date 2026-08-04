month=input("enter month name:")
if(month == "February") :
    print("28 or 29 days in a month")
elif(month in ["April","June","September","November"]):
    print("30 days in a month")
elif(month in ["January","March","May","July","August","October","December"]):
    print("31 days in a month")
