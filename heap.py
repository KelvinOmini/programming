class Heap:
    def __init__(self, aSequence, childIndex):
        self.aSequence = aSequence
        self.childIndex = childIndex        

        # PHASE 1

        def buildFrom(self, aSequence):
            pass
            """ aSequence is an instance of a sequence collection which
            understands the comparison operators. The elements of 
            aSequence are copied into the heap and ordered to build
            a heap """

        def __siftUpFrom(self, childIndex):
            pass
            """childIndex is the index of a node in the heap. This method sifts
            that node up as far as necessary to ensure that the path to the root
            satisfies the heap condition. """


        def addTo(self, newObject):
            pass
            """if the heap is full, double its current capacity.
            Add the newObject to the heap, maintaining it as a
            heap of the same type. Answer newObject. """

        # PHASE 2

        def __siftDownFromTo(self, fromIndex, lastIndex):
            pass
            """fromIndex is the index of an element in the heap.
            Pre: data[fromIndex..lastIndex] satisfies the heap condition,
            except perhaps for the element data[fromIndex].
            post: That element is siftewd down as far as neccessary to
            maintain the heap structure for data[fromindex..lastIndex].
            """
        
                    