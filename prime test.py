x=int(input("Enter integer: "))
devs =[]
def prime(x):
    if x<2:
        print("{} is not a prime number.".format(x))
    else:
        for dev in range(2,x):
           if x%dev==0:
              devs.append(dev)
        if len(devs)==0:
          print("{} is a prime number.".format(x))
        else: 
          print("{} is not a prime number.".format(x))            
    return print
print(prime(x))



def perfect(x):
    
    if x<2:
        print("{} is not a perfect number.".format(x))
    total=1
    for multiple in range(2,int(x**0.5)+1):
        if x%multiple==0:
            total+=multiple
            if multiple != x//multiple:
                total+=x//multiple
    if total==x:
        print("{} is a perfect number.".format(x))
    else:
         print("{} is not a perfect number.".format(x))
    return print
print(perfect(x))

def armstrong(x):
    if x==4 or x==6 or x==8:
        print("{} is not an arm strong number.".format(x))
    else:
      digits=str(x)
      num=len(digits)
    
      total = sum(int(digit)**num for digit in digits)
      if total==x:
        print("{} is an arm strong number.".format(x))
      else:
        print("{} is not an arm strong number.".format(x))
    return print
print(armstrong(x))



