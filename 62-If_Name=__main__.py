#Lesson 62:  if _name_ == '__main__'
# https://www.youtube.com/watch?v=XKHEtdqhLK8
# Python interpreter sets "special variables", one of which is __name__
# Python will assign the __name__ variable a value of '__main__' if it is
# the initial module being run.

def main():
    print("Hello")

if __name__ == '__main__':
    main()