dict = {'name':'Divya',2:'Age'}
print dict
print dict['name']
print dict[2]

dict[2]=21
dict[3] = 30

print dict
del dict[3]
print dict

def find_city(cities,city):
    if city in cities:
        return cities[city]
    else:
        return "Not found"


cities = {'CA':'SFO','NY':'New York'}
cities['OR']='Portland'
cities['_find'] = find_city
print cities
state = 'CB'

city_found = cities['_find'](cities,state)
print city_found