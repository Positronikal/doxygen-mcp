/**
 * @file calculator.cpp
 * @brief Implementation of the Calculator class
 */

#include "calculator.h"
#include <stdexcept>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <chrono>
#include <ctime>

namespace MathUtils {

    Calculator::Calculator() : lastResult(0.0) {
        // Initialize with welcome message in history
        history.push_back("Calculator initialized");
    }

    Calculator::~Calculator() {
        // Cleanup if needed
    }

    double Calculator::add(double a, double b) {
        lastResult = a + b;
        
        std::ostringstream oss;
        oss << formatNumber(a) << " + " << formatNumber(b) << " = " << formatNumber(lastResult);
        history.push_back(oss.str());
        
        return lastResult;
    }

    double Calculator::subtract(double a, double b) {
        lastResult = a - b;
        
        std::ostringstream oss;
        oss << formatNumber(a) << " - " << formatNumber(b) << " = " << formatNumber(lastResult);
        history.push_back(oss.str());
        
        return lastResult;
    }

    double Calculator::multiply(double a, double b) {
        lastResult = a * b;
        
        std::ostringstream oss;
        oss << formatNumber(a) << " * " << formatNumber(b) << " = " << formatNumber(lastResult);
        history.push_back(oss.str());
        
        return lastResult;
    }

    double Calculator::divide(double a, double b) {
        if (std::abs(b) < 1e-10) {
            throw std::invalid_argument("Division by zero is not allowed");
        }
        
        lastResult = a / b;
        
        std::ostringstream oss;
        oss << formatNumber(a) << " / " << formatNumber(b) << " = " << formatNumber(lastResult);
        history.push_back(oss.str());
        
        return lastResult;
    }

    double Calculator::getLastResult() const {
        return lastResult;
    }

    const std::vector<std::string>& Calculator::getHistory() const {
        return history;
    }

    void Calculator::clearHistory() {
        history.clear();
        lastResult = 0.0;
        history.push_back("History cleared");
    }

    double Calculator::power(double base, double exponent) {
        lastResult = std::pow(base, exponent);
        
        std::ostringstream oss;
        oss << formatNumber(base) << " ^ " << formatNumber(exponent) << " = " << formatNumber(lastResult);
        history.push_back(oss.str());
        
        return lastResult;
    }

    double Calculator::sqrt(double number) {
        if (number < 0) {
            throw std::invalid_argument("Square root of negative number is not allowed");
        }
        
        lastResult = std::sqrt(number);
        
        std::ostringstream oss;
        oss << "sqrt(" << formatNumber(number) << ") = " << formatNumber(lastResult);
        history.push_back(oss.str());
        
        return lastResult;
    }

    std::string formatNumber(double number, int precision) {
        std::ostringstream oss;
        oss << std::fixed << std::setprecision(precision) << number;
        return oss.str();
    }

} // namespace MathUtils
