/**
 * @file main.cpp
 * @brief Example usage of the Calculator class
 * @mainpage Calculator Documentation Example
 * 
 * @section intro_sec Introduction
 * 
 * This is a simple example project demonstrating how to use Doxygen
 * to generate documentation for C++ code. The project contains a
 * Calculator class with basic mathematical operations.
 * 
 * @section features_sec Features
 * 
 * - Basic arithmetic operations (add, subtract, multiply, divide)
 * - Advanced operations (power, square root)
 * - Calculation history tracking
 * - Error handling for invalid operations
 * 
 * @section usage_sec Usage Example
 * 
 * @code
 * #include "calculator.h"
 * 
 * int main() {
 *     MathUtils::Calculator calc;
 *     
 *     double result = calc.add(10.5, 5.3);
 *     std::cout << "Result: " << result << std::endl;
 *     
 *     // View calculation history
 *     auto history = calc.getHistory();
 *     for (const auto& entry : history) {
 *         std::cout << entry << std::endl;
 *     }
 *     
 *     return 0;
 * }
 * @endcode
 * 
 * @author Sample Developer
 * @date 2025-06-16
 * @version 1.0
 */

#include <iostream>
#include <exception>
#include "calculator.h"

/**
 * @brief Main function demonstrating calculator usage
 * @return 0 on success, 1 on error
 */
int main() {
    try {
        // Create calculator instance
        MathUtils::Calculator calc;
        
        std::cout << "=== Calculator Example ===" << std::endl;
        
        // Perform some calculations
        double result1 = calc.add(10.5, 5.3);
        std::cout << "Addition: " << result1 << std::endl;
        
        double result2 = calc.multiply(result1, 2.0);
        std::cout << "Multiplication: " << result2 << std::endl;
        
        double result3 = calc.divide(result2, 3.0);
        std::cout << "Division: " << result3 << std::endl;
        
        double result4 = calc.power(2.0, 8.0);
        std::cout << "Power: " << result4 << std::endl;
        
        double result5 = calc.sqrt(64.0);
        std::cout << "Square root: " << result5 << std::endl;
        
        // Display calculation history
        std::cout << "\n=== Calculation History ===" << std::endl;
        const auto& history = calc.getHistory();
        for (size_t i = 0; i < history.size(); ++i) {
            std::cout << (i + 1) << ". " << history[i] << std::endl;
        }
        
        // Demonstrate constants
        std::cout << "\n=== Mathematical Constants ===" << std::endl;
        std::cout << "Pi: " << MathUtils::Constants::PI << std::endl;
        std::cout << "E: " << MathUtils::Constants::E << std::endl;
        std::cout << "Golden Ratio: " << MathUtils::Constants::GOLDEN_RATIO << std::endl;
        
        // Test error handling
        std::cout << "\n=== Error Handling Test ===" << std::endl;
        try {
            calc.divide(10.0, 0.0);
        } catch (const std::exception& e) {
            std::cout << "Caught expected error: " << e.what() << std::endl;
        }
        
        try {
            calc.sqrt(-4.0);
        } catch (const std::exception& e) {
            std::cout << "Caught expected error: " << e.what() << std::endl;
        }
        
        std::cout << "\nLast result: " << calc.getLastResult() << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
