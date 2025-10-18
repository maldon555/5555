user0=input('enter word less then 15')
if len(user0) > 15:
    print("okay")
else:
    print('no')
user1= input('enter age 18 or bigger then')
try:
    if int(user1)>=18:
        print("okay")
    else:
        print("gooo baby")
except Exception as e:
    print(f"error {e}")