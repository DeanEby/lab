#include <iostream>

int main()
{

    std::cout << "Enter three numbers: ";
    int x{};
    std::cin >> x;

    int y{};
    std::cin >> y;

    int z{};
    std::cin >> z;

    std::cout << "You entered: " << x << ", " << y << ", and " << z << ".";
    return 0;
}
