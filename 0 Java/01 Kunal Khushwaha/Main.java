
import java.util.*; 
// public means this class or function/method can be access from anywhere

public class Main 
{
//  class name should be same as that of file name in java

// If we want to execute the main function without creating the object of the Main class
// then we need to make the main method 'static' the reason being we want this main 
// method to be executed before anything else Hence we cannot make Main class object 
// before theexecution of  main method . 
// 
    public static void main(String [] args)
    {
        // String [] args is Command line argument , means whatever arguments we will give
        // in Terminal those will store as an Array of string names args
        // System.out.println(args[0]);
        // Thus above statement would print the first Entry of String Array
        System.out.println("Hello World");
        // System is a class , out is a variable of type printstream and this out variable
        // has a method called println which is used to display the content in out(by default out is Command Line)
        // we can change the out to "File" then in will display the content in file instead of Terminal
        Scanner input = new Scanner(System.in);
        // new keyword is creating a new object of the class Scanner, System.in means standard input keyboard
        // we can also read from Files
        
        System.out.println("Enter the First Number");
        
        int first_num = input.nextInt();

        System.out.println("Enter the Second Number");
        int second_num = input.nextInt();


        System.out.print("First Number is -->");
        System.out.println(first_num);
        System.out.print("Second Number is -->");
        System.out.println(second_num);


    }
}