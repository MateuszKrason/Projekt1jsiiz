#include <iostream>
#include <numeric>

int funct(int a, int b) {
    // int a = 462;
    // int b = 1071;
    int result = std::gcd(a, b);

    std::cout << result << std::endl;

    return result;
}
