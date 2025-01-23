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
        // the count can be used to give us the right index
        // this way we don't overwrite
        // maybe manual sorting here is a good idea
        // cout << strA << "string A \n";
        // cout << stoi(strA) << "int A \n";

        listA[count] = stoi(strA);
        listB[count] = stoi(strB);

        
        //std::cout << listA[0] << "\n";


        // if(count == 0){
        //     std::cout << str;
        // }
        count ++;
    }
    int n = sizeof(listA) / sizeof(listA[0]);
    sort(listA, listA + n);
    sort(listB, listB + n);
    
    // for(int i : listA){
    //     cout << i << "List A \n";
    // }

    // for(int i : listB){
    //     cout << i << "List B \n";
    // }


    // for(int i = 0; i < 10; i++) {
    //     std::cout << '\n';
    // }
    
    // 1000 lines in file
    // std::cout << count;

    count = 0;
    int total = 0;
    while (count != 1000){
        
        int a = listA[count];
        int b = listB[count];
        if(a > b){
            total = total + (a - b);
        } else {
            total = total + (b - a);
        }

        count ++;
    }

    std::cout << total;



    return 0;
}



