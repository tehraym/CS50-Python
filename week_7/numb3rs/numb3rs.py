import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    #Matching the ip address with format (xxx.xxx.xxx.xxx)
    if re.match(r'^\d+\.\d+\.\d+\.\d+$', ip):
        #Using re.split to split "." into a list contains 4 elements
        result = re.split(r'\.', ip)
        count = 0
        #Using re.match to validate each element which are not > 255
        for i in result:
            if re.match(r'^25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2}$', i):
                count += 1
        if count == 4: return True
        else: return False
    else:
        return False

if __name__ == "__main__":
    main()
