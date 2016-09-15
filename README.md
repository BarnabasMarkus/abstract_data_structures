# abstract_data_structures
implementation of abstract data structures // stack and queue

**Stack operations**
```Python
>>> stack_1 = Stack()                   # Create empty stack
>>> stack_2 = Stack([4,5,6,3,3,7], 7)   # Create stack with init content and max_size = 7
>>> 
>>> stack_1.is_empty()                  # Check if stack is empty
True
>>> stack_2.size                        # Get max_size of stack
7
>>> stack_2.is_full()                   # Check if stack is full
False
>>> stack_2.stack                       # Get content of stack
[4,5,6,3,3,7]
>>> stack_2.peek()                      # Get peek item of stack
7
>>> stack_2.push(100)                   # Push item into stack
>>> stack_2.stack
[4,5,6,3,3,7,100]
>>> stack_2.pop()                       # Pop last item from stack
100
```

**Queue operations**
```Python
>>> q = Queue([4,5,6,3,3,7], 7)         # Create queue with init content and max_size = 7
>>> q.is_full()                         # Check if queue is full
False
>>> q.is_empty()                        # Check if queue is empty
False
>>> 
>>> q.peek()                            # Get peek item of queue
4
>>> 
>>> q.enqueue(10)                       # Enqueue 10, it pops out 4
4
>>> q.queue                             # Show queue
[5, 6, 3, 3, 7, 10]
>>> 
>>> q.enqueue(12)                       # Enqueue 12, it pops out 5
5
>>> q.queue                             # Show queue
[6, 3, 3, 7, 10, 12]
>>>
>>> q.dequeue()                         # Dequeue
6
>>> q.dequeue()                         # Dequeue
3
>>> q.queue                             # Show queue
[3, 7, 10, 12]
```
