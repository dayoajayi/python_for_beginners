import requests

get_payload = {'page':2, 'count': 25}
post_payload = {'username': 'dayo', 'password': 'testing' }

r = requests.get('https://httpbin.org/post', params=get_payload)
print(r.url)

# form-based authentication
r = requests.post('https://httpbin.org/post', data=post_payload)
r_dict = r.json()
print(r_dict['form'])


# basic authentication
# create a GET request that goes to the route in the browser:
r = requests.get('https://httpbin.org/basic-auth/dayo/testing', auth=('dayo', 'testing'))
print (r)

