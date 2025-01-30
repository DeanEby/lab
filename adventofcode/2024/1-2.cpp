#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int main() {
    // Open the text file
    std::ifstream file("1-1input.txt");

    std::string str;
    int count = 0;

    int listA[1000];
    int listB[1000];

    while (std::getline(file, str))
    {
        string strA = "";
        string strB = "";
        bool prespace = true;
        for (char i : str){
            if (i != ' '){
                if (prespace){
                    strA = strA + i;
                } else {
                    strB = strB + i;
                }
            } else {
                prespace = false;
            }
        }

        listA[count] = stoi(strA);
        listB[count] = stoi(strB);

        count ++;
    }
    
    count = 0;
    int total = 0;
    while (count != 1000){
        // an inloop temp counter
        int inCount = 0;
        int a = listA[count];
        int match = 0;
        while (inCount != 1000){
            if( a == listB[inCount]){
                match ++;
            }
            inCount ++;
        }
        std::cout << total << " in progress \n";
        total = total + (a * match);

        count ++;
    }

    std::cout << total;



    return 0;
}



