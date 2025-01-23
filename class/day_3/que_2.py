#variable-length args
def sum_all(*nums):
    return sum(nums)


#recursive func
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

#genrator func
def gen(limit):
    for i in range(limit):
        if i%2==0:
            yield i