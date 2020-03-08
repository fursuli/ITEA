"""
Створити клас структури даних Стек, Черга.
Створити клас комплексного числа і реалізувати для
нього арифметичні операції.
 """


class Stack:

    def __init__(self):
        self._items = []

    def get_all_stack(self):
        return self._items

    def clear_stack(self):
        return self._items == []

    def add_element(self, item):
        self._items.append(item)

    def pop_element(self, indx):
        elements = self._items
        element = elements[indx]
        new_stack = elements.remove(element)
        return new_stack

    def remove_element(self, element):
        if element in self._items:
            return self._items.remove(element)
        else:
            return print('Element is not in the stack, anyway')


stck1 = Stack()
stck1.add_element(4)
stck1.add_element(5)
stck1.add_element(8)
stck1.add_element(2)
print(stck1.get_all_stack())
stck1.remove_element(0)
print(stck1.get_all_stack())
print(stck1.pop_element(1))


class Queue:
    '''Create a queue object with a given maximum size.

    If maxsize is <= 0, the queue size is infinite.
    '''

    def __init__(self, maxsize=0):
        self.maxsize = maxsize
        self._init(maxsize)

        self.mutex = threading.Lock()

        # Notify not_empty whenever an item is added to the queue; a
        # thread waiting to get is notified then.
        self.not_empty = threading.Condition(self.mutex)

        # Notify not_full whenever an item is removed from the queue;
        # a thread waiting to put is notified then.
        self.not_full = threading.Condition(self.mutex)

        # Notify all_tasks_done whenever the number of unfinished tasks
        # drops to zero; thread waiting to join() is notified to resume
        self.all_tasks_done = threading.Condition(self.mutex)
        self.unfinished_tasks = 0

    def task_done(self):
        '''Indicate that a formerly enqueued task is complete.

        Used by Queue consumer threads.  For each get() used to fetch a task,
        a subsequent call to task_done() tells the queue that the processing
        on the task is complete.

        If a join() is currently blocking, it will resume when all items
        have been processed (meaning that a task_done() call was received
        for every item that had been put() into the queue).

        Raises a ValueError if called more times than there were items
        placed in the queue.
        '''
        with self.all_tasks_done:
            unfinished = self.unfinished_tasks - 1
            if unfinished <= 0:
                if unfinished < 0:
                    raise ValueError('task_done() called too many times')
                self.all_tasks_done.notify_all()
            self.unfinished_tasks = unfinished

    def join(self):
        '''Blocks until all items in the Queue have been gotten and processed.

        The count of unfinished tasks goes up whenever an item is added to the
        queue. The count goes down whenever a consumer thread calls task_done()
        to indicate the item was retrieved and all work on it is complete.

        When the count of unfinished tasks drops to zero, join() unblocks.
        '''
        with self.all_tasks_done:
            while self.unfinished_tasks:
                self.all_tasks_done.wait()

    def qsize(self):
        '''Return the approximate size of the queue (not reliable!).'''
        with self.mutex:
            return self._qsize()

    def empty(self):
        '''Return True if the queue is empty, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() == 0
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can grow before the result of empty() or
        qsize() can be used.

        To create code that needs to wait for all queued tasks to be
        completed, the preferred technique is to use the join() method.
        '''
        with self.mutex:
            return not self._qsize()

    def full(self):
        '''Return True if the queue is full, False otherwise (not reliable!).

        This method is likely to be removed at some point.  Use qsize() >= n
        as a direct substitute, but be aware that either approach risks a race
        condition where a queue can shrink before the result of full() or
        qsize() can be used.
        '''
        with self.mutex:
            return 0 < self.maxsize <= self._qsize()

    def put(self, item, block=True, timeout=None):
        '''Put an item into the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until a free slot is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Full exception if no free slot was available within that time.
        Otherwise ('block' is false), put an item on the queue if a free slot
        is immediately available, else raise the Full exception ('timeout'
        is ignored in that case).
        '''
        with self.not_full:
            if self.maxsize > 0:
                if not block:
                    if self._qsize() >= self.maxsize:
                        raise Full
                elif timeout is None:
                    while self._qsize() >= self.maxsize:
                        self.not_full.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                else:
                    endtime = time() + timeout
                    while self._qsize() >= self.maxsize:
                        remaining = endtime - time()
                        if remaining <= 0.0:
                            raise Full
                        self.not_full.wait(remaining)
            self._put(item)
            self.unfinished_tasks += 1
            self.not_empty.notify()

    def get(self, block=True, timeout=None):
        '''Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).
        '''
        with self.not_empty:
            if not block:
                if not self._qsize():
                    raise Empty
            elif timeout is None:
                while not self._qsize():
                    self.not_empty.wait()
            elif timeout < 0:
                raise ValueError("'timeout' must be a non-negative number")
            else:
                endtime = time() + timeout
                while not self._qsize():
                    remaining = endtime - time()
                    if remaining <= 0.0:
                        raise Empty
                    self.not_empty.wait(remaining)
            item = self._get()
            self.not_full.notify()
            return item

    def put_nowait(self, item):
        '''Put an item into the queue without blocking.

        Only enqueue the item if a free slot is immediately available.
        Otherwise raise the Full exception.
        '''
        return self.put(item, block=False)

    def get_nowait(self):
        '''Remove and return an item from the queue without blocking.

        Only get an item if one is immediately available. Otherwise
        raise the Empty exception.
        '''
        return self.get(block=False)

    # Override these methods to implement other queue organizations
    # (e.g. stack or priority queue).
    # These will only be called with appropriate locks held

    # Initialize the queue representation
    def _init(self, maxsize):
        self.queue = deque()

    def _qsize(self):
        return len(self.queue)

    # Put a new item in the queue
    def _put(self, item):
        self.queue.append(item)

    # Get an item from the queue
    def _get(self):
        return self.queue.popleft()


class ComplexNumber:

    def __init__(self, real=0.0, img=0.0):
        self._real = real
        self._img = img

    def __repr__(self):
        result = f'Complex number = {self._real}, {self._img}.'
        return result

    def __str__(self):
        if self._img == 0:
            result = f'Complex number = {self._real}.'
            return result
        elif self._real == 0:
            if self._img == 1 or self._img == -1:
                result = 'Complex number = i.'
            else:
                result = f'Complex number = {self._img}i.'
            return result
        else:
            if self._img > 0:
                result = f'Complex number = ({self._real}+{self._img}i).'
            else:
                result = f'Complex number = ({self._real}{self._img}i).'
            return result

    def __add__(self, other):
        count_real = self._real + other._real
        count_img = self._img + other._img
        if count_img > 0:
            result = f'{count_real} + {count_img}i'
        else:
            result = f'{count_real}{count_img}i'
        return result

    def __sub__(self, other):
        count_real = self._real - other._real
        count_img = self._img - other._img
        if count_img > 0:
            result = f'{count_real} + {count_img}i'
        else:
            result = f'{count_real}{count_img}i'
        return result

    def __mul__(self, other):
        count_real = self._real * other._real # -> real
        count_real_img = self._real * other._img # -> img

        count_img = self._img * other._real # -> img
        count_img_real = -(self._img * other._img) # -> real: i**2 = -1

        mul_real = count_real + count_img_real
        mul_img = count_real_img + count_img

        if mul_img > 0:
            result = f'{mul_real} + {mul_img}i'
        else:
            result = f'{mul_real}{mul_img}i'
        return result

    def __truediv__(self, other):
        count_real = (self._real*other._real + self._img*other._img) / (other._real**2 + other._img**2) # -> real
        count_img = (self._img*other._real - self._real*other._img) / (other._real**2 + other._img**2) # -> img

        if count_img > 0:
            result = f'{count_real}+{count_img}i'
        else:
            result = f'{count_real}{count_img}i'

        return result


# numb1 = ComplexNumber(2.73, -12.14)
# print(numb1.__repr__())
# print(numb1.__str__())
# numb2 = ComplexNumber(0, -1)
# print(numb2.__str__())
# numb3 = ComplexNumber(-6, 7)
# print(numb3.__str__())

# numb2 = ComplexNumber(-2, 1)
# numb3 = ComplexNumber(1, -1)
#
# print(numb2.__add__(numb3))
# print(numb2.__sub__(numb3))
# print(numb2.__mul__(numb3))
# print(numb2.__truediv__(numb3))

