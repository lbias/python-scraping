import requests

files = {'uploadFile': open('test_image.png', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php", files=files)
print(r.text)
