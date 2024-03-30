import ctypes
class MyList:

    def __init__(self):
        self.size = 1
        self.num = 0
        #lests create a C type array with size=self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n
    
    def __str__(self):
        result =''
        for i in range(self.n):
            result = result+ str(self.A[i]) + ','
        return '['+ result + ']'  

    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'IndexError - Index out of range'

    def append(self,item):
        if self.n == self.size:
          self. __resize(self.size*2)

        self.A[self.n] = item
        self.n = self.n + 1 

    def __resize(self, new_capacity):
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __make_array(self,capacity):
        #creates a c types array with size capacity
        return(capacity*ctypes.py_objects)()
    
L = MyList()

    