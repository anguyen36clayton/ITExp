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
		int multiplication = num1 * num2;
		
		// Check if num2 is not zero to avoid division by zero
        int division = num2 != 0 ? num1 / num2 : 0;
		
		// Check if num2 is not zero to avoid modulus by zero
        int modulus = num2 != 0 ? num1 % num2 : 0;

        System.out.println("Addition: " + addition);
        System.out.println("Subtraction: " + subtraction);
		System.out.println("Multiplication: " + multiplication);
		System.out.println("Division: " + division);
		System.out.println("Modulus: " + modulus);
        
        // Close the scanner to prevent resource leak
        scanner.close();
    }
}
