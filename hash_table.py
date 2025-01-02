
#Hash Table Data Structure to deal with collission data using Separate Chaining
class HashTable:
    def __init__(self):
        self.max = 10
        self.array = [[] for i in range(self.max)]

    #Function to get the Hash Table index
    def get_hash(self,key):
        h = 0
        for c in key:
            h += ord(c)
        return (h % self.max)
    
    #Function to put the data in the table 
    def __setitem__(self, key, value):
        h_add = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.array[h_add]): #if the same key we entered fount in the table 
            if len(element) == 2 and element[0] == key:    
                self.array[h_add][idx] = (key, value)     #we overwrite it to new
                found = True
                break
        if not found:                                 #if the key not found we append this hash index
            self.array[h_add].append((key, value))      #with the same data of collision data
        
    #Function to get data
    def __getitem__(self, key):
        h_get = self.get_hash(key)
        for element in self.array[h_get]:
            if element[0] == key:
                return element[1]
        #return (self.array[h_get])  

    #Function to delete the data
    def __delitem__(self, key):
        h_del = self.get_hash(key)
        for idx, element in enumerate(self.array[h_del]):
            if element[0] == key:
                del self.array[h_del][idx]

        #self.array[h_del] = None  

