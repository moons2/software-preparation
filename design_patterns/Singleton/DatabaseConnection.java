/**
 * Pattern name: Singleton
 * 
 * A class is a template for creating objects. If a client
 * has access to a constructor for a class
 * the client can create any number of objects
 * from the class. Sometimes you want more control over
 * the construction of a class.
 * 
 * Consider the Singleton pattern if you want only
 * one instance  of a class and want all clients
 * to share the same instance.
 * 
 */

/**
 * Solution: 
 */
public class DatabaseConnection 
{
    // vars
    private static DatabaseConnection instance = null;
    private static Object LOCK = new Object();

    // methods
    
    // private constructor method
    private DatabaseConnection()
    {
        // establish connection
    }

    /**
     * in a multi-thread environment, a race condition occurs when
     * multiple thread attempt to update the same mutable shared variable.
     * 
     * Java offers mecanisms to avoid race conditions by synchronizing
     * thread access to shared data
     * 
     * a piece of logic marked with synchronized becomes a syncronized block
     * allowing only one thread to execute at any given time
     */
    public synchronized static DatabaseConnection instance() throws InterruptedException
    {
        System.out.println("sync static DatabaseConnection invoked");
        if (instance == null)
        {
            instance = new DatabaseConnection();
        }

        LOCK.wait(4000);

        return instance;
    }

    public synchronized String getAssignmentGrade(String student, String course, String assignment)
    {
        return "pass";
    }
}