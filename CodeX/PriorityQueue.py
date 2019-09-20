# Priorty Queue using Queue

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return self.queue == []

    def insert(self, val):
        self.queue.append(val)

    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item

        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())






# S-H-O-R-T-C-U-T-S

# # priority queue using list
# q = []
# q.append((2, 'cow'))
# q.append((3, 'dog'))
# q.append((1, 'py'))
# print(q)
# q.sort(reverse = True)
# print(q)
# print(q.pop())
# print(q)


# # priorty queue uising queue
# from queue import PriorityQueue
# q = PriorityQueue()
# # show status of queue
# print(q.empty())
# q.put((2, 'cow'))
# q.put((3, 'dog'))
# q.put((1, 'py'))
# q.put((4, 'apple'))
# # show status of queue
# print(q.empty())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# # show status of queue
# print(q.empty())