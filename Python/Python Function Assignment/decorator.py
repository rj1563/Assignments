from time import time

# Decorator function to calculate and display the time taken by a function to execute
def execution_time(func):

    def wrapper(*args,**kwargs):
        before_time = time()      #before the func time
        res=func(*args,*kwargs)   #execute function
        after_time = time()       #after the func runs
        print(f"Time of execution {after_time-before_time}")  #give time taken by func
        return res
    return wrapper