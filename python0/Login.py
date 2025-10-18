user0=input('enter your name ')
user1= input('enter your age  your age must be +18')
try:
    if int(user1)>=18:
        print(f"hello {user0.capitalize() } your age is: {user1}")
    
    else:
        print("gooo away baby")
except Exception as e:
    print(f"error {e}")
