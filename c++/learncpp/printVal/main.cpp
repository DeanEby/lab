#include <iostream>

void doPrint() {
    std::cout << "In doPrint()\n";
}

void printValue(int x) {
    std::cout << x << '\n';
}

int add (int x, int y) {
    return x + y;
}

int main() {
    doPrint();
    printValue(77);

    std::cout << add(5, 5);
}