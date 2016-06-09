cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
car_pool_cap = cars_driven*space_in_a_car
avg_passengers_per_car = passengers/cars_driven
print "there are",cars,"cars available"
print "carpool capacity is",car_pool_cap
