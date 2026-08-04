sub1= float(input("enter subject marks:"))
sub2= float(input("enter subject marks:"))
sub3= float(input("enter subject marks:"))
total= sub1+sub2+sub3
per=total/3
print(per)
if(per>=90) :
    print("A")
elif(per>=80) :
    print("B")
elif(per>=70) :
    print("C")
elif(per>=60) :
    print("D")
elif(per>=50) :
    print("E")
elif(per>=40) :
    print("F")
else:
    print("you are fail")


