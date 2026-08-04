Basic_salary=float(input("enter basic salary:"))
if(Basic_salary<=10000):
    HRA=(Basic_salary*100)/20
    DA=(Basic_salary*100)/80
    print("\n Gross salary: ",Basic_salary+HRA+DA)
elif(Basic_salary<=20000):
    HRA=(Basic_salary*100)/25
    DA=(Basic-salary*100)/90
    print("\n Gross salary:",Basic-salary+HRA+DA)
elif(Basic_salary>20000):
    HRA=(Basic_salary*100)/30
    DA=(Basic_salary*100)/95
    print("\n Gross salary:",Basic_salary+HRA+DA)
else:
    print("\n Please enter valid basic salary")
