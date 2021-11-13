import time

def calcProd_v1():
    '''
    calculate the product of the first 100,000 numbers.
    And get how long the time took via time.time()
    '''
    starttime = time.time()
    product = 1
    for i in range(1, 100000):
        product *= i
    endtime = time.time()
    print('The result of calcProd_v1() is %s digits long.' % (len(str(product))))
    print('Took %s seconds to calculate.' % (endtime - starttime))

def timer(func):
    def wrapper(*args, **kwds):
        tstart = time.time()
        func(*args, **kwds)
        tstop = time.time()
        print('耗时%0.9f秒'%(tstop-tstart,))
    return wrapper

@timer
def calcProd_v2():
    '''
    calculate the product of the first 100,000 numbers
    And get how long the time took via timer
    '''
    product = 1
    for i in range(1, 100000):
        product *= i
    print('The result of calcProd_v2() is %s digits long.' % (len(str(product))))

def main():
    calcProd_v2()
    calcProd_v1()

if __name__ == '__main__':
    main()