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


# stck1 = Stack()
# stck1.add_element(4)
# stck1.add_element(5)
# stck1.add_element(8)
# stck1.add_element(2)
# print(stck1.get_all_stack())
# stck1.remove_element(0)
# print(stck1.get_all_stack())
# print(stck1.pop_element(1))


class Queue:
    """ First-In-First-Off """
    _queue = []

    def __init__(self, item):
        self._item = item
        Queue._queue.append(item)

    def get_queue(self):
        return Queue._queue

    def append_to_queue(self, *args):
        for arg in args:
            Queue._queue.append(arg)
        return Queue._queue

    def remove_item(self, item):

        queue = Queue._queue
        if item in queue:
            queue.remove(item)
        else:
            print(f'{item} is not in queue.')

        result = queue

        return result

    def item_off(self):
        queue = Queue._queue
        queue.remove(queue[0])
        result = queue
        return result


q = Queue('first')
q.append_to_queue('second', 3, 'ff')
q.append_to_queue(999)
print(q.remove_item(999))
print(q.remove_item(0))
print(q.get_queue())
print(q.item_off())
print(q.item_off())



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

