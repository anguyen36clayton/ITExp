import java.util.InputMismatchException;
import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        boolean continueCalculating = true;
        while (continueCalculating) {
            try {
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

                System.out.println("Addition: " + num1 + " + " + num2 + " = " + addition);
                System.out.println("Subtraction: " + num1 + " - " + num2 + " = " + subtraction);
                System.out.println("Multiplication: " + num1 + " * " + num2 + " = " + multiplication);
                System.out.println("Division: " + num1 + " / " + num2 + " = " + division);
                System.out.println("Modulus: " + num1 + " % " + num2 + " = " + modulus);
            } catch (InputMismatchException e) {
                System.out.println("Please enter only numbers.");
                // Consume the invalid input
                scanner.next();
            }

            // Prompt the user to continue or exit
            System.out.print("Do you want to perform another calculation? (yes/no): ");
            String choice = scanner.next().toLowerCase();
            continueCalculating = choice.equals("yes");
        }

        // Close the scanner to prevent resource leak
        scanner.close();
    }
}
