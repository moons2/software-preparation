# Object Orientation Programming

ia a programming paradigm that relies on the concept of
_class_ and _objects_. It is used to structure a sotware program into
simple reusable pieces of code, usually called classes.

Some languaes objected oriented are

> C++
> JavaScript
> Java
> Python

**Benefits**

- Object Orientation Programmim models complex problems/things as reproducible,
  simple structures.

- Reusable, OOP can be used cross programs

- Allows for class-specific behavior through **polymorphism**

- Easier to debug, classes often contain all applicable information to them

- Its more secure, protects information through **encapsulation**

## Class/Super Classe/Base Class

An abstract of a object in the real world, **or a user defined data type**. Classes often represents broad
categories, like _Car_ or _Dog_ that shares attributes. These classe define
what attributes an instance of that type will have, like _color_, _wheight_,
_height_ and so on, but not its values.

Classes also decribe some functions, called **methods**, available only to
objects of that type. These functions are defined within the class and perform
some actions.

`for example, Car class may have a method called _repaint_ that changes the color attribute of our car. This function is helpful only for objects of type Car, so we declare it within our car class making it a method. `

Child classes are also know as derived class or extended class.

## Object

An instantiated from a class, and represent an individual real world thing.

## Attribute

The information stored by a class. The attribute are defined in the class template.

## State

State references to the values stored in the objects's attribute fields. For example, puppy and dogs may be treated different. The birthday could define the state of an object, and allow the software to handle dogs of different ages differently.

## Methods

Methods apply behavior to objects, methods represent actions, methods are implemented in a class template and can modify, update and delete object's data.

Methods often modify, update or delete data, but methods don't necessarily need to retrieve information.

`bark()` method junst bark, without any return.

Methods are how programmers promote reusability, it's an easy manner to keep functionality encapsulated inside an object.

Some informations about practices in the oop: `_attendance` the underscore in the beggining denotes that the variable is protected.

# 2. FOUR PRINCIPLES OF THE OBJECT ORIENTATION PROGRAMMING

The four pillars of object oriented programming are Inheritance, Encapsulation, Abstraction and Polymorphism

## 2.1. Inheritance

Child classes inherit data and behavior from parent classes.

Inheritance allows classes to inherit features of other classes. Or, child classes inherit attributes and features from parents classes. **inheritance supports the reusability**.

## 2.2. Encapsulation

Encapsulating means containing all important information **inside an object** and exposing only selected ones.
Attributes and behaviors (methods) are implemented inside the class template.

Then when an object is instantiated from a class the data and methods are incapsulated inside that object. Encapsulation **hides** the internal software implemetation of the methods and data inside the objects.

Encapsulation requires the access level definition through

> Private/Internal Interface: methods and properties accessible by methods of the same class.

> Public/External Interface: methods and properties acessible also from outside the class.

**Public**, accessible by the outside world.

**Protected**, accessible only by child classes.

**Private**, accessible only from inside the same class

## 2.3. Abstraction

## 2.4. Poliorphism

Desenhar objetos para **compartilhar comportamentos** using inheritance, objects can **override**(sobrescrever) behaviors shared by parent classes, with specific child behaviors. Polimorphism allow the same method to execute defferent behaviors in two ways: **method overriding** and **method overloading**.

### 2.4.1. Method Overriding (Sobrescrita de método)

In method overriding, a child class can provide a different implementation than its parent class.

```java
// Parent class
Class Dog
{
    public static void bark()
    {
        System.out.println("Woof");
    }
}

// Wolf is a special race of dog
Class Wolf extends Dog
{
    // this method overrides the default bark from the
    // parent class Dog, because its type and params
    // are the same but the behavior is different
    public static void bark()
    {
        System.out.println("Auuuuuu!");
    }
}
```

### 2.4.2. Method Overloading (Sobrecarga de método)

Method Overloading (Sobrecarga de método) occures when the method
from the child class has the same name of the parent class
but with number / type different of arguments

## Agragação

## Composição

```Java
Class Dog
{
    public static void bark()
    {
        System.out.println("Woof!");
    }
}

Class Wolf extends Dog
{
    // this is an example of method overloading
    // the original method doesn't have any arguments
    // but the child class
    public static void bark(String bark)
    {
        System.out.println(bark);
    }
}

// Considering the bellow chunk of code
Class main
{
    Wolf myWolf = new Wolf;
}

```

- Inheritance

- Parenc Class vs Child Class

## Dog Sitting Camp

> imagine you were asked to make a simple reusable OOP software
> of a Dog Sitting Camp with hundred of pets, and you have
> to keep track of the names, ages, and days attended for each pet.

**SOLUTION**

Gouping informations together:

1.  **Create a parent and generic class to represent any dog** as a blueprint
    of information and behaviors(methods), that all dogs have in common, regardless
    of race.

2.  **Create child classes** to represent different subcategories of dogs under the
    generic parent class

3.  **Add unique attributes and behavior** to the child classes to represent differences

4.  **Create object from the child classes** to represent dog within that subgroup

### Bibliography

[](https://stackabuse.com/object-oriented-programming-in-python)
[](https://www.educative.io/blog/object-oriented-programming)
