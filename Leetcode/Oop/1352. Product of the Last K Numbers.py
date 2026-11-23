'''Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 

Example:

Input
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output
[null,null,null,null,null,null,20,40,0,null,32]

Explanation
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 
'''

class ProductOfNumbers:

    def __init__(self):
        self.lst=[]
        self.ind=-1
        self.zero_track=-1

    def add(self, num: int) -> None:
        if not self.lst or (num!=0 and self.lst[-1]==0):
            self.lst.append(num)
        else:
            self.lst.append(self.lst[-1]*num)
        self.ind+=1
        if num==0:
            self.zero_track=self.ind

    def getProduct(self, k: int) -> int:
        t=self.ind-k
        if self.zero_track>t:
            return 0
        else:
            if t==-1 or self.lst[t]==0:
                return self.lst[-1]
            return self.lst[-1]//self.lst[t]
        

obj = ProductOfNumbers()

operations = [
    "add", "add", "add", "add", "add",
    "getProduct", "getProduct", "getProduct",
    "add", "getProduct"
]

values = [
    [3], [0], [2], [5], [4],
    [2], [3], [4],
    [8], [2]
]

results = []

for operation, value in zip(operations, values):

    if operation == "add":
        obj.add(value[0])
        results.append(None)

    elif operation == "getProduct":
        result = obj.getProduct(value[0])
        results.append(result)

print(results)