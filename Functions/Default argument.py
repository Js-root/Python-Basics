#Default Arguments in a function are values that we can set to be constant even if user provides a parameter or not 

def net_Price(price,discount,tax=0.05): #Here we set tax as default so now if user doesnt provide any value for tax we will assume it to be 0.05 by default

    return (price * (1-discount) * (1+tax))

#We need to send 3 values otherwise it gives error but with default arguments we can send only one value aswell

print(net_Price(500,0.1)) #We dont send tax value