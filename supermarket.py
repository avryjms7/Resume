#SuperMarket

prices = {"banana":4 , "apple" : 2 , "orange" : 1.5, "pear" : 3}
stock = {"banana" : 6, "apple" : 0, "orange" : 32, "pear" : 15}



shopping_list = ["banana" , "orange" , "apple"]

def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
        return total

print (compute_bill(shopping_list))



