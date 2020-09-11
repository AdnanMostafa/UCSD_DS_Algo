def tricky(n):
    operations = 0
    while n > 0:
        for i in range(n):
            print("Operations: %d" % operations)
            operations += 1
        n = int(n/2)
        

#takes in a single integer, while it is bigger than 0, say there are these many operations, it starts from the beginning and reiterates. it runs the operation n number of times after it reiterates until the number divided by 2 is = 0. Outer loop runs log(n) times. The inner loop runs O(n) times, n/2, n/4 and so on. This all adds up to 2n which is O(n)