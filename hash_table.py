
#Hash Table Data Structure to deal with colission data using Separate Chaining
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




v = HashTable()

v['march 1'] = 110
v['march 2'] = 220
v['march 3'] = 330
v['march 4'] = 440
v['march 5'] = 550
v['march 6'] = 660
v['march 7'] = 770
v['march 8'] = 880
v['march 9'] = 990
v['march 10'] = 1100
v['march 17'] = 1700
v['march 18'] = 1800

print(v["march 17"])
#del v["march 6"]
print(v["March 6"])
print(v.array)

print('*'*50)
print(v.get_hash('march 7'))
print(v.get_hash('march 18'))
print('*'*50)
print(v.get_hash('march 8'))
print('*'*50)
print(v.get_hash('march 9'))
print(v.get_hash('march 10'))
print(v.get_hash('march 1'))

#v['march 901'] = 90101
#

#

"""print(v["March 1"])
print(v["March 3"])
print(v["March 4"])
print(v["March 5"])
"""