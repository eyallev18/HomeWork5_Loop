"""
HomeWork#5
This is Exercise in Basic Loop
written by Eyal Lev
Date March 25st 2019
"""

for i in range(1,101):    #All numbers until 100 include
    if  i==3:             # 3 is prime Number
        print ("Fizz  Prime")
        continue
    elif i%3==0:          # if number is multiply of 3 and not equal 3
        print ("Fizz")
        continue
    elif  i==5:           # 5 is prime Number
        print ("Buzz  Prime")
        continue
    elif i%5==0:           # if number  is multiply of 5 and not equal 5
        print ("Buzz")
        continue
    elif i%3==0 and i%5==0:  # if number is multiply of 3 and multiply of 5
        print ("FizzBuzz")
        continue
    else:
        prime=True            # Number is prime until we find that he is not prime
        for j in range(2,i//2+1):  # going all numbers from 2 until i div2 +1
            if i%j==0  :       # if the number (i) divided by one of the numbers from 2 to (i//2+1) w/o reminder
                prime=False    # The number is not prime
        if prime:
            print (i,"Prime")
        else:
            print (i)







