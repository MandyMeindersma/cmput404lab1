import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)
# print(dir(r)) #to print whole object attributes


a = requests.get("github url")
print(a.text)

# NOTES
# when using curl the -i shows headers
# -L this does location, it will automatically redirect you to where you are supposed to be
