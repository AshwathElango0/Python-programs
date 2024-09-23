import numpy as np  # Necessary imports

# Defining the class used to create nodes in the compute graph
class Node:
    def __init__(self, value, grad=None):
        self.value = np.array(value, dtype=np.float32)
        self.grad = np.zeros_like(value).astype(np.float32 ) if grad is None else grad
        self.children = []
        self.op = None
        self.op_args = None

    def __add__(self, other):
        if isinstance(other, Node):
            result = Node(value=self.value + other.value)
            result.children = [self, other]
            result.op = 'add'
        else:
            result = Node(value=self.value + other)
            result.children = [self]
            result.op = 'add_const'
            result.op_args = other
        return result

    def __sub__(self, other):
        if isinstance(other, Node):
            result = Node(value=self.value - other.value)
            result.children = [self, other]
            result.op = 'sub'
        else:
            result = Node(value=self.value - other)
            result.children = [self]
            result.op = 'sub_const'
            result.op_args = other
        return result

    def __mul__(self, other):
        if isinstance(other, Node):
            result = Node(value=self.value * other.value)
            result.children = [self, other]
            result.op = 'mul'
        else:
            result = Node(value=self.value * other)
            result.children = [self]
            result.op = 'mul_const'
            result.op_args = other
        return result

    def __truediv__(self, other):
        if isinstance(other, Node):
            result = Node(value=self.value / other.value)
            result.children = [self, other]
            result.op = 'div'
        else:
            result = Node(value=self.value / other)
            result.children = [self]
            result.op = 'div_const'
            result.op_args = other
        return result

    def __pow__(self, other):
        if isinstance(other, Node):
            result = Node(value=self.value ** other.value)
            result.children = [self, other]
            result.op = 'pow'
        else:
            result = Node(value=self.value ** other)
            result.children = [self]
            result.op = 'exp_const'
            result.op_args = other
        return result

    def backward(self, grad=None):
        if grad is None:
            grad = np.ones_like(self.value).astype(np.float32)
        self.grad += grad

        if self.op == 'add':
            for child in self.children:
                child.backward(grad)
        elif self.op == 'add_const':
            self.children[0].backward(grad)

        elif self.op == 'sub':
            left, right = self.children
            left.backward(grad)
            right.backward(-grad)

        elif self.op == 'sub_const':
            self.children[0].backward(grad)

        elif self.op == 'mul':
            left, right = self.children
            left.backward(grad * right.value)
            right.backward(grad * left.value)

        elif self.op == 'mul_const':
            const = self.op_args
            self.children[0].backward(grad * const)

        elif self.op == 'div':
            left, right = self.children
            left.backward(grad / right.value)
            right.backward(-grad * left.value / right.value**2)

        elif self.op == 'div_const':
            const = self.op_args
            self.children[0].backward(grad / const)

        elif self.op == 'pow':
            base, exp = self.children
            base.backward(grad * exp.value * (base.value ** (exp.value - 1)))
            exp.backward(grad * self.value * np.log(base.value))

        elif self.op == 'exp_const':
            const = self.op_args
            self.children[0].backward(grad * const * (self.children[0].value ** (const - 1)))

# Example usage
a = Node(np.array([2, 3, 4]))
b = Node(np.array([3, 4, 5]))
c = a * 2 + b
d = c ** 3

# Run backward pass starting from the output node
d.backward()

# Printing gradients of d with respect to each of the previous arrays
print(f"Gradient at a: {a.grad}")
print(f"Gradient at b: {b.grad}")
print(f"Gradient at c: {c.grad}")
