#include <bits/stdc++.h>
using namespace std;

int main()
{
    const char* logo = 
        "*******************************************************************************\n"
        "          |                   |                  |                     |\n"
        " _________|________________.=\"\"_;=.______________|_____________________|_______\n"
        "|                   |  ,-\"_,=\"\"     =.|                  |\n"
        "|___________________|__\"=._o\"-._        =.______________|___________________\n"
        "          |                \"=._o\"=._      _\"=._                     |\n"
        " _________|_____________________:=._o \"=._.\"_.-=\"'=.__________________|_______\n"
        "|                   |    __.--\" , ; \"=._o.\" ,\"\"\"-._ \".   |\n"
        "|___________________|_._\"  ,. .  ` ,  \"-._\"-._   \". '__|___________________\n"
        "          |           |o\"=._ , \" ; .\". ,  \"-._\"-._; ;              |\n"
        " _________|___________| ;-.o\"=._; .\"  '.\"\\ . \"-._ /_______________|_______\n"
        "|                   | |o;    \"-.o\"=._`  ' \" ,__.--o;   |\n"
        "|___________________|_| ;     (#) -.o \"=._.--\"_o.-; ;___|___________________\n"
        "____/______/______/___|o;._    \"      \".o|o_.--\"    ;o;____/______/______/____\n"
        "/______/______/______/_=._o--._        ; | ;        ; ;/______/______/______/_\n"
        "____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____\n"
        "/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_\n"
        "____/______/______/______/______/____\"=.o|o_.--\"\"___/______/______/______/____\n"
        "/______/______/______/______/______/______/______/______/______/______/_____ /\n"
        "*******************************************************************************\n";
    
    cout << logo;
    
    string res, res2, door;

    cout << "Welcome to Treasure Island." << endl;
    cout << "Your mission is to find the treasure." << endl;
    cout << "You're at a cross road. Where do you want to go?" << endl;
    cout << "     Type \"left\" or \"right\"" << endl;
    getline(cin, res);

    if(res == "left") {
        cout << "You've come to a lake. There is an island in the middle of the lake." << endl;
        cout << "Type \"wait\" to wait for a boat. Type \"swim\" to swim across." << endl;
        getline(cin, res2);
        if(res2 == "wait") {
            cout << "You arrive at the island unharmed. There is a house with 3 doors." << endl;
            cout << "One red, one yellow and one blue. Which colour do you choose?" << endl;
            getline(cin, door);
            if(door == "yellow") {
                cout << "You found the treasure! You Win!" << endl;
            } else if(door == "red") {
                cout << "The room is full of fire! Game Over!" << endl;
            } else if(door == "blue") {
                cout << "You were eaten by beasts. Game Over!" << endl;
            } else {
                cout << "Game Over!" << endl;
            }
        } else {
            cout << "Attacked by trout. Game Over!" << endl;
        }
    } else {
        cout << "Fall into a hole. Game Over!" << endl;
    }

    return 0;
}

