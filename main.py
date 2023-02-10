import requests

def check_wordpress(domain):
    try:
        r = requests.get(domain)
        if "wp-content" in r.text:
            return "Yes"
        else:
            return "No"
    except:
        return "Error"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    domain = input("Enter a domain: ")
    print("Is the domain running on WordPress CMS? " + check_wordpress(domain))
