#include <iostream>

// This program will request two numbers from the user, add them together, and then print the result

int addTwoNums(int x, int y){
    return x + y;
}

int getUserInput() {
    int input {};
    std::cout << "Enter a number: ";
    std::cin >> input;
    return input;
}

int main() {
    int x {getUserInput()};
    int y {getUserInput()};

    std::cout << x << " + " << y << " is: " << addTwoNums(x, y);

    return 0;
}