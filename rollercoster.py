def minimum_bribes(q):
    bribes = 0
    q = [i-1 for i in q]
    for i, o in enumerate(q):
        cur = i

        if o - cur > 2:
            print("Too chaotic")
            return
        
        for k in q[max(o - 1, 0):i]:
            if k > o:
                bribes += 1

    return bribes


n=int(input("Enter number of people in queue = "))
queue = []

print("Enter the current position of people after bribes : ")
for i in range(0, n):
    ele = int(input())
  
    queue.append(ele)
min=0
min=minimum_bribes(queue)
print("Minimum number of possible bribes in the current situation of the queue : ",min)






