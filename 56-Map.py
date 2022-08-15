#Lesson 56: Map
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# map() = applies a function to each itme in an iterable (list, tuple, etc.)
# map(function, iterable) so it accepts two arguments

#list of tuples
store = [("shirt", 20.00),
          ("pants", 25.00),
          ("jacket", 50.00),
          ("socks", 10.00)]

# one USD is 0.82 euros
to_euros = lambda  data:(data[0], data[1]*0.82)
to_dollars = lambda  data:(data[0], data[1]/0.82)

#store_euros = list(map(to_euros, store))
#for i in store_euros:
#    print(i)

store_dolalrs = list(map(to_dollars, store))
for i in store_dolalrs:
    print(i)