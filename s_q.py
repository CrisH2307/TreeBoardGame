#    Main Author(s): Cris Huynh
#    Main Reviewer(s): Sean Muniz, Cris Huynh

class Stack: 
    
    def __init__(self, cap=10): 
        
        # We must create a list that will have a size of 10
        self.cap = cap
        self.count = 0
        self.stack = [None] * cap
    
    def capacity(self): 
        return self.cap
    
    def push(self, data): 
        
        # we are adding to the back. increment the count
        self.count += 1
        
        #check if we reach the capacity
        if self.count > self.cap: 
            
            # double the size
            self.cap *= 2
            
            # create a new list with the new size
            newStack = [None] * self.cap
            
            # copy contents into new list
            for i in range(0, len(self.stack)): 
                newStack[i] = self.stack[i]
                
            # set new list 
            self.stack = newStack
        
        self.stack[self.count -1] = data            
    
    def pop(self):
        if self.count == 0: 
            raise IndexError('pop() used on empty stack')
        else: 
            self.count -= 1
            
            # store popped value so we can return it
            popped = self.stack[self.count]
            
            # set to empty state
            self.stack[self.count] = None
            
            return popped

    
    def get_top(self):
        if self.count == 0: 
            return None
        else: 
            return self.stack[self.count -1]
    
    def is_empty(self):
        if self.count == 0:
            return True
        
        return False
    
    def __len__(self): 
        return self.count
        
class Queue: 
    
    def __init__(self, cap=10): 
        self.count = 0
        self.cap = cap
        self.queue = [None] * self.cap
    
    def capacity(self):
        return self.cap
    
    def enqueue(self, data): 
        self.count += 1
        
        if self.count > self.cap: 
            
            # Double size
            self.cap *= 2
            
            newQueue = [None] * self.cap   
            
            for i in range(0, len(self.queue)): 
                newQueue[i] = self.queue[i]
            
            self.queue = newQueue
            
        self.queue[self.count -1] = data
        
    def dequeue(self): 
        if self.count == 0: 
            raise IndexError('dequeue() used on empty queue')
        else: 
            
            self.queue.append(None)
            
            self.count -= 1
                        
            popped = self.queue.pop(0)
            
            return popped

    def get_front(self): 
        if self.count == 0: 
            return None
        else: 
            return self.queue[0]
    
    def is_empty(self): 
        if self.count == 0: 
            return True
        
        return False
    
    def __len__(self): 
        return self.count

class Deque:
    def __init__(self, cap=10):
        """
        Initializes a deque with a given capacity.
        
        Parameters:
        - cap (int): Initial capacity of the deque, default is 10.
        """
        self.count = 0               # Number of elements currently in the deque
        self.cap = cap               # Maximum number of elements before resizing
        self.deque = [None] * self.cap  # Internal list for storing elements
        self.head = 0                # Index of the front element
        self.tail = 0                # Index of the next position for push_back

    def capacity(self):
        """
        Returns the current maximum capacity of the deque.
        
        Returns:
        - int: Capacity of the deque.
        """
        return self.cap

    def push_front(self, data):
        """
        Adds an element to the front of the deque.
        
        Parameters:
        - data: The data to be added to the front of the deque.
        
        Raises:
        - Doubles the capacity if the deque is full.
        """
        if self.count == self.cap:   # Deque is full, so resize
            self._resize()

        # Move head backward to insert the new front
        self.head = (self.head - 1) % self.cap  # Wrap around using modulo
        self.deque[self.head] = data
        self.count += 1

    def push_back(self, data):
        """
        Adds an element to the back of the deque.
        
        Parameters:
        - data: The data to be added to the back of the deque.
        
        Raises:
        - Doubles the capacity if the deque is full.
        """
        if self.count == self.cap:   # Deque is full, so resize
            self._resize()

        # Insert data at tail position and move tail forward
        self.deque[self.tail] = data
        self.tail = (self.tail + 1) % self.cap  # Wrap around using modulo
        self.count += 1

    def pop_front(self):
        """
        Removes and returns the element from the front of the deque.
        
        Returns:
        - popped_data: The element removed from the front of the deque.
        
        Raises:
        - IndexError: If the deque is empty.
        """
        if self.count == 0:
            raise IndexError('pop_front() used on empty deque')

        # Retrieve data at head, reset position, and move head forward
        popped_data = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.cap  # Wrap around using modulo
        self.count -= 1
        return popped_data

    def pop_back(self):
        """
        Removes and returns the element from the back of the deque.
        
        Returns:
        - popped_data: The element removed from the back of the deque.
        
        Raises:
        - IndexError: If the deque is empty.
        """
        if self.count == 0:
            raise IndexError('pop_back() used on empty deque')

        # Move tail backward, retrieve data, and reset position
        self.tail = (self.tail - 1) % self.cap  # Wrap around using modulo
        popped_data = self.deque[self.tail]
        self.deque[self.tail] = None
        self.count -= 1
        return popped_data

    def get_front(self):
        """
        Returns the element at the front of the deque without removing it.
        
        Returns:
        - Element at the front, or None if the deque is empty.
        """
        return None if self.count == 0 else self.deque[self.head]

    def get_back(self):
        """
        Returns the element at the back of the deque without removing it.
        
        Returns:
        - Element at the back, or None if the deque is empty.
        """
        return None if self.count == 0 else self.deque[(self.tail - 1) % self.cap]

    def is_empty(self):
        """
        Checks if the deque is empty.
        
        Returns:
        - bool: True if empty, False otherwise.
        """
        return self.count == 0

    def __len__(self):
        """
        Returns the number of elements currently in the deque.
        
        Returns:
        - int: Number of elements in the deque.
        """
        return self.count

    def __getitem__(self, index):
        """
        Enables indexing to access elements in the deque.
        
        Parameters:
        - index (int): The index of the element to retrieve.
        
        Returns:
        - The element at the specified index.
        
        Raises:
        - IndexError: If the index is out of range.
        """
        if index < 0 or index >= self.count:
            raise IndexError('Index out of range')
        return self.deque[(self.head + index) % self.cap]

    def _resize(self):
        """
        Resizes the deque by doubling its capacity, preserving the order of elements.
        
        This method is called when the deque reaches full capacity. It creates a new internal
        list with twice the capacity, copies elements to maintain order, and resets head and tail.
        """
        new_deque = [None] * (self.cap * 2)
        
        # Copy existing elements to the new deque
        for i in range(self.count):
            new_deque[i] = self.deque[(self.head + i) % self.cap]
        
        # Update deque with new resized list
        self.deque = new_deque
        self.head = 0               # Reset head to the beginning
        self.tail = self.count      # Tail now points to the next free slot
        self.cap *= 2               # Double the capacity
