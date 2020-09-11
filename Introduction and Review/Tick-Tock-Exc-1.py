def print_info(a):
    n = len(a) #O(1)
    avg = 0.0 #O(1)
    for i in range(n): #O(n)
        print("Element #%d is %d" % (i,a[i]))
        avg += a[i]
    avg /= n
    print("Average is %f" % avg)

print_info([10,21,42,53,94,35])

#big-O = O(n)