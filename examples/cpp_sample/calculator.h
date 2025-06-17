/**
 * @file calculator.h
 * @brief A simple calculator class demonstrating Doxygen documentation
 * @author Sample Developer
 * @date 2025-06-16
 * @version 1.0
 */

#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <string>
#include <vector>

/**
 * @namespace MathUtils
 * @brief Mathematical utility functions and classes
 */
namespace MathUtils {

    /**
     * @class Calculator
     * @brief A basic calculator class with arithmetic operations
     * 
     * This class provides basic mathematical operations including addition,
     * subtraction, multiplication, and division. It also maintains a history
     * of calculations performed.
     * 
     * @example
     * @code
     * Calculator calc;
     * double result = calc.add(5.0, 3.0);
     * std::cout << "Result: " << result << std::endl;
     * @endcode
     */
    class Calculator {
    private:
        std::vector<std::string> history; ///< History of calculations
        double lastResult;                ///< Last calculated result
        
    public:
        /**
         * @brief Default constructor
         * 
         * Initializes the calculator with empty history and zero result.
         */
        Calculator();
        
        /**
         * @brief Destructor
         */
        ~Calculator();
        
        /**
         * @brief Adds two numbers
         * @param a First operand
         * @param b Second operand
         * @return Sum of a and b
         * 
         * @note This operation is recorded in the calculation history
         */
        double add(double a, double b);
        
        /**
         * @brief Subtracts second number from first
         * @param a Minuend
         * @param b Subtrahend
         * @return Difference (a - b)
         */
        double subtract(double a, double b);
        
        /**
         * @brief Multiplies two numbers
         * @param a First factor
         * @param b Second factor
         * @return Product of a and b
         */
        double multiply(double a, double b);
        
        /**
         * @brief Divides first number by second
         * @param a Dividend
         * @param b Divisor
         * @return Quotient (a / b)
         * 
         * @throw std::invalid_argument if divisor is zero
         * @warning Division by zero will throw an exception
         */
        double divide(double a, double b);
        
        /**
         * @brief Gets the last calculated result
         * @return The most recent calculation result
         */
        double getLastResult() const;
        
        /**
         * @brief Retrieves calculation history
         * @return Vector of strings containing calculation history
         */
        const std::vector<std::string>& getHistory() const;
        
        /**
         * @brief Clears the calculation history
         * 
         * Removes all entries from the history vector and resets
         * the last result to zero.
         */
        void clearHistory();
        
        /**
         * @brief Calculates the power of a number
         * @param base The base number
         * @param exponent The exponent
         * @return base raised to the power of exponent
         * 
         * @since Version 1.0
         */
        double power(double base, double exponent);
        
        /**
         * @brief Calculates the square root of a number
         * @param number The number to find the square root of
         * @return Square root of the number
         * 
         * @throw std::invalid_argument if number is negative
         * @pre number must be non-negative
         * @post returns positive result
         */
        double sqrt(double number);
    };
    
    /**
     * @brief Mathematical constants
     */
    namespace Constants {
        const double PI = 3.14159265358979323846;    ///< Pi constant
        const double E = 2.71828182845904523536;     ///< Euler's number
        const double GOLDEN_RATIO = 1.61803398874989; ///< Golden ratio
    }
    
    /**
     * @brief Operation types enumeration
     */
    enum class OperationType {
        ADD,        ///< Addition operation
        SUBTRACT,   ///< Subtraction operation
        MULTIPLY,   ///< Multiplication operation
        DIVIDE,     ///< Division operation
        POWER,      ///< Power operation
        SQRT        ///< Square root operation
    };
    
    /**
     * @struct CalculationResult
     * @brief Structure to hold calculation results with metadata
     */
    struct CalculationResult {
        double value;                    ///< The calculated value
        OperationType operation;         ///< Type of operation performed
        std::string timestamp;           ///< When the calculation was performed
        bool success;                    ///< Whether the calculation succeeded
        std::string errorMessage;        ///< Error message if calculation failed
        
        /**
         * @brief Default constructor
         */
        CalculationResult() : value(0.0), operation(OperationType::ADD), 
                            success(false), errorMessage("") {}
    };
    
    /**
     * @brief Utility function to format numbers
     * @param number The number to format
     * @param precision Number of decimal places
     * @return Formatted string representation
     */
    std::string formatNumber(double number, int precision = 2);
    
} // namespace MathUtils

#endif // CALCULATOR_H
