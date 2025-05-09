# # Homework:
# # Object-Oriented Programming (OOP) Exercises
# # 
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         return 3.14159 * self.radius ** 2
    
#     def calculate_perimeter(self):
#         return 2 * 3.14159 * self.radius


# circle = Circle(5)
# print(f"Area: {circle.calculate_area():.2f}")       
# print(f"Perimeter: {circle.calculate_perimeter():.2f}")  






# # # 2. Person Class
# # # Write a Python program to create a Person class. 
# # # Include attributes like name, country, and date of birth. Implement a method to determine the person's age.


# from datetime import datetime

# class Person:
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
    
#     def calculate_age(self):
#         today = datetime.today()
#         birthdate = datetime.strptime(self.date_of_birth, "%Y-%m-%d")  
#         age = today.year - birthdate.year

#         if (today.month, today.day) < (birthdate.month, birthdate.day):
#             age -= 1

#         return age 

# person1 = Person("Oygul", "Uzbekistan", "2002-08-17")   
# print(person1.calculate_age()) 

# 3. Calculator Class
# Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

# class Calculator:
#     def add(self, x, y):
#         return x + y
    
#     def subtract(self, x, y):
#         return x - y
    
#     def multiply(self, x, y):
#         return x*y
    
#     def divide(self, x, y):
#         if y  == 0:
#             return "Error"
#         return x/y
    
# calc = Calculator()

# print(f"Addition: 5+4 = {calc.add(5, 3)}")

# print("Addition:", calc.add(5, 3))          
# print("Subtraction:", calc.subtract(5, 3))   
# print("Multiplication:", calc.multiply(5, 3))
# print("Division:", calc.divide(6, 3))     

# 4. Shape and Subclasses
# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
#  Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the method")
    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius **2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s*(s- self.side1)*(s- self.side2)*(s- self.side3))
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
class Square(Shape):
    def __init__ (self, side):
        self.side = side

    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side
    
if __name__ == "__main__":
     circle = Circle(5)
print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")

triangle = Triangle(3, 4, 5)
print(f"Triangle - Area: {triangle.area():.2f}, Perimeter: {triangle.perimeter():.2f}")

square = Square(4)
print(f"Square - Area: {square.area():.2f}, Perimeter: {square.perimeter():.2f}")
# 5. Binary Search Tree Class
# Write a Python program to create a class representing a binary search tree. 
# Include methods for inserting and searching for elements in the binary tree.

class Node:
    """Node class for BST elements"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree implementation"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a new value into the BST"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, current_node):
        """Helper method for recursive insertion"""
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(value, current_node.right)
    

    def search(self, value):
        """Search for a value in the BST (returns True/False)"""
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, current_node):
        """Helper method for recursive search"""
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(value, current_node.left)
        else:
            return self._search_recursive(value, current_node.right)

    def inorder_traversal(self):
        """Return values in sorted order (left -> root -> right)"""
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, current_node, values):
        """Helper for inorder traversal"""
        if current_node:
            self._inorder_recursive(current_node.left, values)
            values.append(current_node.value)
            self._inorder_recursive(current_node.right, values)
        return values


if __name__ == "__main__":
    bst = BinarySearchTree()
    
    for num in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        bst.insert(num)
    
  
    print("Search for 6:", bst.search(6))    
    print("Search for 99:", bst.search(99))  
    
    
    print("Inorder Traversal:", bst.inorder_traversal()) 
   
