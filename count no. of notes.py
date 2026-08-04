#Count the total number of notes in the given amount
Amount=int(input("enter the amount:"))
Note=int(input("enter which note you want(100 or 200 or 500)"))

Note1=Amount//Note #using floor division
print("NOTES ARE:",Note1)

remaining_Note1 =Amount%Note #using floor division
print("The remaining RS:",remaining_Note1)
