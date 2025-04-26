#include <iostream>

int main() {
    int input{};

    std::cout << "Enter an integer: ";

    std::cin >> input;

    std::cout << "Double " << input << " is: " << input * 2 << '\n';

    std::cout << "Triple " << input << " is: " << input * 3 << '\n';

}