import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    #Checks if string starts and ends with iframe
    if re.match(r"(<iframe)(.+?)(</iframe>)", s):
        #Searches for youtube URL
        url = re.search(r"https?://(www\.)?youtube\.com/embed/[a-zA-z0-9]{11}", s, re.IGNORECASE)
        if url:
            #If True to re-sub to the correct format
            result = re.sub(r"https?://(www\.)?youtube\.com/embed", "https://youtu.be", url.group())
            return result
        else: return None
    else: return None

if __name__ == "__main__":
    main()
