banknots= [200, 100, 50, 20, 10, 5, 2, 1]


price = int (input("Products price : "))

given_money = int (input("Given money : "))

return_money = given_money - price

return_dict={}

for banknot in banknots:
    x = 0
    while banknot <= return_money:
        x+=1
        return_money -= banknot
    if x>0:
        print(f"{banknot} 'dan {x} adet verildi." )
