#Lesson 60: Dictionary Comprehension
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Dictionary Comprehension = create dictionaries using an expression
# can replace for loops and certain lambda functions

# 1: dictionary = {key: expression for (key,value) in iterable}
# 2: dictionary = {key: expression for (key,value) in iterable if conditional}
# 3: dictionary = {key:(if/else) for (key,value) in iterable}
# 4: dictionary = {key: function(value) for (key,value) in iterable}

# Dictionary version 1
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C )

# Dictionary version 2
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles':"sunny", 'Chicago':"cloudy"}
sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
print(sunny_weather)

# Dictionary version 3
cities = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
desc_cities3 = {key:("Warm" if value >=40 else "Cold") for (key,value) in cities.items()}
print(desc_cities3)

# Dictionary version 4
def check_temp(value):
    if value>= 70:
        return "Hot"
    elif 69>=value >=40:
        return "Warm"
    else:
        return "Cold"
cities = {'New York': 32, 'Boston': 75, 'Los Angeles':100, 'Chicago':50}
desc_cities4  = {key:check_temp(value) for (key,value) in cities.items()}
print(desc_cities4)