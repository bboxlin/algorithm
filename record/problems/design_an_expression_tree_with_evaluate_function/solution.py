import abc, enum
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
    
class OpNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right 

    @abstractmethod
    def evaluate(self) -> int:
        pass

class Multiply(OpNode):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate() 
class Plus(OpNode):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate() 
class Minus(OpNode):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate() 
class Divide(OpNode):
    def evaluate(self):
        return self.left.evaluate() // self.right.evaluate() 
    
class Number(Node):
    def __init__(self, val):
        self.val = val
    def evaluate(self):
        return self.val 
        
"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        ops = {'*':Multiply, '+':Plus, '-':Minus, '/':Divide}
        stack = [] 
        for c in postfix:
            if c in ops:
                rightnode = stack.pop()
                leftnode = stack.pop() 
                opnode = ops[c](leftnode, rightnode)
                stack.append(opnode)
            else:
                numNode = Number(int(c))
                stack.append(numNode)
        return stack[0]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        