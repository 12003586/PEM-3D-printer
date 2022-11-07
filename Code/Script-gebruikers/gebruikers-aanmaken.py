import requests
import json

url = "http://raspberrypi.local/api/access/users:80"
data = {"name":"Python","password":"123456","groups":["studenten"],"permissions":[],"active":'true',"admin":'false'}


headers = {'Host': 'raspberrypi.local', 'Content-Length': '103', 'Accept': 'application/json, text/javascript, */*; q=0.01', 'Cache-Control': 'no-cache', 'X-CSRF-Token': 'Ijc4Njg5Njc1NmU4NmU2Nzk5YjUwOGIwMGNmZTA0NmM2MGJhNDllZTIi.Y2jRyA.vugCGDTy5d7u6blj4UFBuhDGqjM', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36', 'Content-Type': 'application/json; charset=UTF-8', 'Origin': 'http://raspberrypi.local', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8', 'Cookie': 'remember_token_P80=Eclair4837|1666593353.791629|ee7253bb638946a249d1a0d27ddfb84bad22145bbe2f363ccefc06ab61f04877859895dce6d0ecf0b138345a419edf62e16453bfef3210e38e38dc482bbc053d; csrf_token_P80=Ijc4Njg5Njc1NmU4NmU2Nzk5YjUwOGIwMGNmZTA0NmM2MGJhNDllZTIi.Y2jRyA.vugCGDTy5d7u6blj4UFBuhDGqjM; session_P80=.eJxlkElOQzEQRO_iNUJ2D253dgnhHJGHNvlS-EF_WCDE3TFig2DZVXrVpfpwl77YenWHbdntwV2m5g5OAEwSN99CYq0GQYP46oN2QEoxG4bIhRTQWqacxJhizS1Ajl1VtEhryJ2BS42UkgJArcDe2uBTDr1LQY2sJIhdM1EugN7yCBQ3iuyrLT9tnustTwsl_NanZvM2be-Ped-ul-39zdxh3m-3X85_6HZ_mebLq9Vrnqf1ddjXbXsbxveT1dZ1us8_WDrp6SkEr6yBjuM40fmYKJyfno8h0vkPs04vc972ZZRwBTF6Je4eFSNlTiACCmoewpiIx2zQpEXsY0XByJS81RCE2HLJHqyHxrWgZ0Dw2BNpYsmxpSreC-tI7VZqa0WVOkQRgliDZ8Xk3ecXsUKFDw.Y2jR0w.iZhTyHygo22yk7bZ6ojY1fUDMvc', 'Connection': 'close'}


r = requests.post(url, data=json.dumps(data), headers=headers)

#data = r.json()
  
#print(data)