def dist(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            print("%d - %d = %d" % (a[j], a[i], a[j]-a[i]))

dist([10,20,90,80,70,60])

#there are two loops, it goes in loops subtracting two before it, until it reaches the last stage.the two for loops makes it O(n^2)