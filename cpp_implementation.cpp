#include <iostream>
#include <numeric>

int main(int a, char* b[]) {
    
    int arg1 = std::atoi(b[1]);
    int arg2 = std::atoi(b[2]);

    int result = std::gcd(arg1, arg2);

    return result;
}
