count = 0

def additive_persistence(n):

    def an(n):
        val=n
        res=0
        while val>10:
            last = val%10
            val= val//10
            if val<10:
                res = res + val
            res = res +last
        global count
        count = count + 1
        return res

    ans = n
    while ans > 9:
        ans = an(ans)
    print(count)


additive_persistence(5734657)
additive_persistence(7)
additive_persistence(167)
additive_persistence(5897)
additive_persistence(123465)
additive_persistence(95428)
additive_persistence(13975)
