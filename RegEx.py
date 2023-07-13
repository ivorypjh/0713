import re

# : 이나 % 를 , 로 치환
test = "abcd : ABCD  ERTG % ertg"
result = re.sub("[:,%]", ",", test)
print(result)

# 유효한 이메일 형식인지 검사
FF = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
emailFormat = ["whdekfdl3@naver.com", "afqefkagn@gmail.com", 
               "wrongmail.mail.com", "wrongmail2@gmail@com"]
for mail in emailFormat:
    print(FF.match(mail) != None)