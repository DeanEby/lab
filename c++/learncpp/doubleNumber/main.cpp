#include <iostream>

int doubleNumber(int x){
    return x * 2;
}

int main() {
    int input{};
    std::cout << "Enter a number: ";
    std::cin >> input;
    std::cout << doubleNumber(input);
    return 0;
}