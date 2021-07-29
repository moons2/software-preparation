class Solution
{

    public static void main(String[] args)
    {

        Wolf dog = new Wolf();
        dog.bark();
    }
}

// Class child
// Inherits from Dog parent class
class Wolf extends Dog
{
    // Polymorphism, the caracteric of a child class
    // assume multiple phorms, i.e., different behaviors
    // in this case method overloading
    // when the child class changes the
    // natural behavior by changin the parameters
    void bark(String barkSound)
    {
        System.out.println(barkSound);
    }
}

// Class father
class Dog
{
    void bark()
    {
        System.out.println("Woof!");
    }
}




