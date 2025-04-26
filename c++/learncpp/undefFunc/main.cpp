#include <iostream>

int getValueFromUserUB() {
    std::cout << "Enter an Integer: ";
    int input {};
    std::cin >> input;
}



int main() {
    int num {getValueFromUserUB()};

    std::cout << num << " doubled is: " << num * 2 << '\n';

    return 0;
}