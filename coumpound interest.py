#Compound Interest

p=int(input("principal amount: "))
r=int(input("rate of interest: "))
t=int(input("time in years: "))
n=int(input("number of times interest is compounded per year: "))
      
amount=p*(1+r/n)**n*t
print("amount: ",amount)
