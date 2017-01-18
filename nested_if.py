num=int(input("enter number"))
if num%2==0:
        if num%3==0:
                print("num is divisible by both 2 & 3")
        else:
                print("num is divisible by 2 but not by 3")
else:
        if num%3==0:
                print("num is divisible by 3 but not by 2")
        else:
                print("num is not divisible by both")
