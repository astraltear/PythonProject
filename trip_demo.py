def hotel_cost(nights):
    return nights*140
    
def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475
        
        
def rental_car_cost(days):
    base=40
    if days ==0:
        return 0
    elif days >=1 and days <3:
        return days*base
    elif days >=3 and days <7:
        return (days*base) -20
    elif days >=7 :
        return (days*base) -50

def trip_cost(city,days,spending_money):
    hotel_sum = hotel_cost(days)
    car_cost=rental_car_cost(days)
    plane_cost = plane_ride_cost(city)
    return hotel_sum+car_cost+plane_cost+spending_money


print( trip_cost('Los Angeles',5,600))
