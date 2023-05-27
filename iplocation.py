import requests

def get_location(ip):
    response = requests.get("https://ipapi.co/{}/json/".format(ip))
    data = response.json()
    return data

if __name__ == "__main__":
    ip = input("Enter an IP address: ")
    location = get_location(ip)
    print("The location of the IP address {} is: {}".format(ip, location))
