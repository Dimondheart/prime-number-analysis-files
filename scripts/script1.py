def le(x):
    return (x + abs(x)) / (2*x + 0**(abs(x)))
    
def ui(x):
    return (x - abs(x) + 0**(abs(x))) / (2*x + 0**(abs(x)))
    
def mu(n):
    return ((n-3)//2)*((((-1)**n)+3)/2) + ((n-3)-((n-3)//2))*((((-1)**(n-1))+3)/2) + 3
    
def bn(n):
    return le(n)*ui(n-2)*(n+1) + le(n-2)*ui(n-3)*(2*n-1) + le(n-3)*(2*mu(n)-1)

def val_to_n_in_bn(val):
    n = 1
    while True:
        if bn(n) == val:
            return n
        elif bn(n) > val:
            return -1
        n += 1
            
def cn(n):
    pos = 1
    val = 2
    while True:
        if pos == n:
            return val
        elif pos > n:
            print "ERROR in cn(n)"
            return -1
        # Find the next value
        check = val + 1
        while True:
            if check in (2,3,5):
                val -= val
                val += check
                break
            elif check % 2 != 0 and check % 3 != 0 and check % 5 != 0:
                val -= val
                val += check
                break
            check += 1
        pos += 1
        
max_n = 128
n_val = [n for n in xrange(1,max_n+1)]
print n_val
cn_for_n_val = [cn(n) for n in n_val]
print cn_for_n_val
cn_to_bn_pos = [val_to_n_in_bn(val) for val in cn_for_n_val]
print cn_to_bn_pos
delta_bn_pos = [cn_to_bn_pos[i] - cn_to_bn_pos[i-1] for i in xrange(1, len(cn_to_bn_pos))]
print delta_bn_pos
# with max_n = 128, delta_bn_pos is
#1, 1, 1, 1, 1, 1, 1, 1, # The first few values that are the same for the two
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1, 1,
#2, 1, 2, 1, 1, 1, 1

