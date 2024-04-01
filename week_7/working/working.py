import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    #To check the input's format
    if re.match(r"(((\d{1,2}):?(\d{1,2})? (AM|PM)) to ((\d{1,2}):?(\d{1,2})? (AM|PM)))", s):
        #Splitting the input's time into a list
        list = re.split(r" to ", s)
        converted = []
        #Parsing through the list
        for i in list:
            #Using re.search to break HH:MM PM/AM into 3 groups
            time = re.search(r"(\d{1,2}):?(\d{1,2})? (AM|PM)", i)
            #Feed the groups into function parse_time and append it into a list
            converted.append(parse_time(time.group(1), time.group(2), time.group(3)))\
        #returning the result in 24HR format
        return(f"{converted[0]} to {converted[1]}")
    else:
        raise ValueError

#Function that contains conditions and calculation to return the correct time
def parse_time(hours, minutes, period):
    hours = int(hours)
    if minutes == None:
        minutes = 0
    else: minutes = int(minutes)

    if hours > 12 or minutes > 59:
        raise ValueError

    if hours != 12 and period == "PM":
        hours += 12
    elif hours == 12 and period =="AM":
        hours -= 12
    return(f"{hours:02d}:{minutes:02d}")


if __name__ == "__main__":
    main()
