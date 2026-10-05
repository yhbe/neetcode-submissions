class Node:
    def __init__(self, next=None, prev=None, value = None, key = None):
        self.next = next
        self.prev = prev
        self.setvalue = value
        self.setkey = key

class LRUCache:

    def __init__(self, capacity: int):
        # cap for maxcapacity and amntinstorage initialized to Zero
        self.maxcap = capacity
        self.amntinstorage = 0
        #new head and tail node pointing to eachother
        self.headnode = Node()
        self.tailnode = Node()
        self.headnode.prev = self.tailnode
        self.tailnode.next = self.headnode

        # Mapping for quicklookups key -> Node(next,prev,value)
        self.kvmap = {}

    def refreshnode(self, selectednode: Node):
        #breaking old relationships
        lnode = selectednode.prev
        rnode = selectednode.next
        lnode.next, rnode.prev = rnode,lnode


        #reestablishing relationship of the new selectednode.
        lnode = self.headnode.prev
        headnode = self.headnode
        lnode.next = selectednode
        headnode.prev = selectednode
        selectednode.prev = lnode
        selectednode.next = headnode

        

    def get(self, key: int) -> int:
        #Return the value corresponding to the key if the key exists, otherwise return -1.
        if key in self.kvmap:
            self.refreshnode(self.kvmap[key])
            return self.kvmap[key].setvalue
        return -1
        

    def put(self, key: int, value: int) -> None:
        #Update the value of the key if the key exists. 
        if key in self.kvmap:
            self.kvmap[key].setvalue = value
            self.refreshnode(self.kvmap[key])
            return
        else:
            #creating node and setting it inbetween head and the node previous to that
            nodecreation = Node()
            lnode = self.headnode.prev
            headnode = self.headnode
            lnode.next = nodecreation
            headnode.prev = nodecreation
            nodecreation.prev = lnode
            nodecreation.next = headnode
            #setting value and key relationship
            nodecreation.setkey = key
            nodecreation.setvalue = value
            #adding creatednode to the KVMAP
            self.kvmap[key] = nodecreation
            #incrementing amntinstorage because we added one
            self.amntinstorage += 1
            #taking last node thats least used and axeing it if amntinstorage > maxcapacity.
            if (self.amntinstorage > self.maxcap):
                todelete = self.tailnode.next
                lnode = todelete.prev
                rnode = todelete.next
                lnode.next,rnode.prev = rnode,lnode
                del self.kvmap[todelete.setkey]
                self.amntinstorage -= 1
            #Otherwise, add the key-value pair to the cache. 
            #If the introduction of the new pair causes the cache to exceed its capacity,
            #remove the least recently used key.

#A key is considered used if a get or a put operation is called on it.