import requests


def check():
     url = 'https://www.google.com'
     timeout = 5
     try:
        requests.get(url, timeout=timeout)
        return True
     except OSError as err:
      return False
     except ValueError:
      return False
     except BaseException as err:
      return False
    