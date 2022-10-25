# Code

## Burp Suite test

Host: raspberrypi.local
Port: 80

```
POST /api/access/users HTTP/1.1
Host: raspberrypi.local
Content-Length: 113
Accept: application/json, text/javascript, */*; q=0.01
Cache-Control: no-cache
X-CSRF-Token: ImM1Njc1MzRjNTNmYWI3M2Y4MjI2YmYwODY0MWIxMjBiM2ZhNzBhMTYi.Y1ZOag.wbxKpykso3F0Fq0FNADWNrUsFCU
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36
Content-Type: application/json; charset=UTF-8
Origin: http://raspberrypi.local
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: remember_token_P80=Eclair4837|1666593353.791629|ee7253bb638946a249d1a0d27ddfb84bad22145bbe2f363ccefc06ab61f04877859895dce6d0ecf0b138345a419edf62e16453bfef3210e38e38dc482bbc053d; csrf_token_P80=ImM1Njc1MzRjNTNmYWI3M2Y4MjI2YmYwODY0MWIxMjBiM2ZhNzBhMTYi.Y1ZOag.wbxKpykso3F0Fq0FNADWNrUsFCU; session_P80=.eJxlkUtuHDEMRO-idRCQFClKs_Mv1xhQEuVpYNw2-rMwgtw9CrwJki0fC1Us_gzXsfl-C5djO_1buC49XELqZkzMtTeCZD5cUAxlaMUiZpWjSSmD6mSjUIo2cLjFhk7QqTJmUvAEXuKQ1KK1zCZN1FErj55LnjvZyVOiilU49VJylNJJOcwg5-7bV5qXdrdl4xx1zpfu67Ecn9_tPG7X4_PDw2U97_e_yP-i-_vrsl7fvN1sXfa3iW_H8THBH5Pd9315X79k-kgZIZYH-IH8JPKITyDyDPSgSfQl_aPZl9fVjnObIUJxy4bNOkLh2GulkoZlZVS3ij1FnfdR7BKZQRVyqoqjCbMqV2yzP-HpPhRiK4kAhUlHSfMFEUhzQU_VHTBLAwWK0Vsizz0bdAi_fgMCqIYz.Y1ZOdg.G2luJ4Kli_AQEKsNOrEKONDDNfE
Connection: close

{"name":"gebruikertest123","password":"1234","groups":["studenten"],"permissions":[],"active":true,"admin":false}

```