<<<<<<< HEAD
/**
 * COMPILING
 * 
 * FIRST:
 *      $ javac Solution.java
 *      this command will generate all .classes present in this file, then
 * SECOND:
 *      $ java Solution
 *      this command runs the Solution.class
 * 
 * SOURCE: https://www.youtube.com/watch?v=6uzR-d3Yttc
 * 
 */

=======
>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7
class Solution
{

    public static void main(String[] args)
    {
<<<<<<< HEAD
=======

>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7
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
<<<<<<< HEAD

    // Sobrescrita
    void bark()
    {
        System.out.println("Auuuuu!")
    }
=======
>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7
}

// Class father
class Dog
{
    void bark()
    {
<<<<<<< HEAD
        System.out.println("Woof Woof!");
=======
        System.out.println("Woof!");
>>>>>>> fce927b8a437975244a9e2a523fbc7aaea04f8a7
    }
}




