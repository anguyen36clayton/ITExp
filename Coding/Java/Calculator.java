import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Prompt the user to enter the first number
        System.out.print("Enter the first number: ");
        int num1 = scanner.nextInt();
        
        // Prompt the user to enter the second number
        System.out.print("Enter the second number: ");
        int num2 = scanner.nextInt();
        
        int addition = num1 + num2;
        int subtraction = num1 - num2;

        System.out.println("Addition: " + addition);
        System.out.println("Subtraction: " + subtraction);
        
        // Close the scanner to prevent resource leak
        scanner.close();
    }
}
