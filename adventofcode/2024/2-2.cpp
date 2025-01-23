// Unfinished! I wanted to do this all in c++ to brush up on my skills
// But this one is so much easier for me to do in python
#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int main() {
    // Open the text file
    std::ifstream file("2-1input.txt");

    std::string str;

    int count = 0;
    int total = 0;

    while (std::getline(file, str)){
        // cout << str << '\n';
        // count++;

        //20 is arbitrary but should be big enough
        int level[20];
        string number = "";
        bool prespace = true;
        int index = 0;
        //added end of line character, kinda lazy I think
        str = str + "e";
        
        // getting all of the numbers out of the txt and loaded into an array
        for (char i : str){
            // adds an end of line character so I can capture the last value
            if (i == 'e'){
                // convert to integer
                int tnum = stoi(number);
                level[index] = tnum;
                number = "";
                prespace = true;
                
            }
            if (i != ' '){
                // add chars to number until you hit a space
                if (prespace){
                    number = number + i;
                } else {
                    // convert to int
                    int tnum = stoi(number);
                    level[index] = tnum;
                    number = "";
                    number = number + i;
                    index++;
                    prespace = true;
                }
            } else {
                prespace = false;
            }
        }


        // We now have a full "report". We need to check each report if they would still be safe without at least one of their levels.

        // dampened level index. This level will be ignored
        //int dampLev = 0;
        for (int i = 0; i <= index; i++){
            std::cout << i << "\n";


            

            //Testing a instance of a report
            // loop count
            count = 0;
            //says if the report is safe so far
            bool safe = true;
            //direction (1 for positive -1 for negative 0 for nothing)
            int dir = 0;
            int valueA;
            int valueB;
            //loop though levels
            while (count <= index){

                // Dastardly if block incoming
                if (i == count && i == 0){
                    
                    count++;
                    int valueA = level[count];
                    int valueB = level[count + 1];

                } else if (i == count && i == index){
                    
                    break;
                } else if (i == count) {
                    int valueA = level[count - 1];
                    int valueB = level[count + 1];

                    count++;

                }


                if (count > index) {
                    break;
                }

                // needs to increase or decrease
                if (valueA == valueB){
                    cout << valueA << "should not equal" << valueB << "\n";
                    safe = false;
                } else if (valueA < valueB){ // if the values are increasing set direction to 1
                    if (dir == 0 || dir == 1){
                        dir = 1;
                    } else {
                        safe = false;
                        cout << valueA << valueB << "Direction issue \n";
                    }
                    if(valueB - valueA >= 1 && valueB - valueA <= 3){
                        //safe = true;
                        cout << valueA << " " << valueB << "good jump size \n";
                    } else {
                        safe = false;
                        cout << valueA << valueB << "Too big of a jump \n";
                    }
                } else if (valueA > valueB){
                    if (dir == 0 || dir == -1){
                        dir = -1;
                    } else {
                        safe = false;
                        cout << valueA << " " << valueB << "Direction issue \n";
                    }
                    if (valueA - valueB >= 1 && valueA - valueB <=3){
                        cout << valueA << " " << valueB << "good jump size \n";
                        //safe = true;
                    } else {
                        cout << valueA << valueB << "Too big of a jump \n";
                        safe = false;
                    }
                }



                


                // cout << level[count] << "\n";
                if (!safe){
                    cout << str << " unsafe \n";
                    break;
                }
            
            }
            if(safe){
                cout << str << " safe \n";
                total++;
                break;
            }
        }
        
        

        // cout << "NEXT LOOP \n \n \n";


    }
    cout << total << " total \n";

    return 0;
}