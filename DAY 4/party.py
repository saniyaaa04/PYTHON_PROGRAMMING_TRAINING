day=input("Enter the day :").strip().upper()
attendence=int(input("Enter the attendees :"))
def classifySuccessOfParty(day,attendence):
    weekdays=("MON","TUE","WED","THU")
    weekends=("FRI","SAT","SUN")
    if day not in weekdays and day not in weekends :
        return "INVALID"
    if day in weekdays:
        if 700<=attendence<=1000:
            return "Successful"
        else:
            return "Unsuccessful"
    
    if day in weekends:
        if attendence>=1500:
            return "Sucessful"
        else:
            return "Unsuccessful"
result=classifySuccessOfParty(day,attendence)

print(result)


