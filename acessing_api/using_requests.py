'''
this module uses the requests library to access end-poiunt APIs on the internet
We use exception handling to catch any exceptions that might occur
'''
import requests # remember - we may need to pip install the request library
import json # this is part of the python standard library

def getData(id):
    # we can inject parameters into the URL using string formatting
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    # url = 'https://nonsuch.nope' # this should make an exception
    try:
        results = requests.get(url) # make an API call to this url
        # results is json, and we need a dictionary
        results_d = results.json()
        print(results_d)
    except requests.ConnectionError as err: # catch specific exception
        print('oops - connection error {}'.format(err))
    except Exception as e: # this catehs any other exceptions that might occur
        print('there has been an exception {}'.format(e))

if __name__ == '__main__':
    getData(5) # call our function