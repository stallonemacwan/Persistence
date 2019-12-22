count = 0

def multiplicative_persistence(n):

    def an(n):
        val=n
        res=1
        while val>10:
            last = val%10
            val= val//10
            if val<10:
                res = res * val
            res = res * last
        global count
        count = count + 1
        return res


    ans = n
    while ans > 9:
        ans = an(ans)
    print(count)


multiplicative_persistence(6788)
