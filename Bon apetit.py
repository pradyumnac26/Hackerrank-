def bonAppetit(bill, k, b):
    su=0
    y=sum(bill)
    diff=y-bill[k]
    z=diff/2
    if(z==b):
        print("Bon Appetit")
    else:
        print(int(b-z))
