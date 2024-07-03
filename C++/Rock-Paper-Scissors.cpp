#include <bits/stdc++.h>
using namespace std;

void find_winner(int comp, int user) {
    map<int, string> options = {{0, "Rock"}, {1, "Paper"}, {2, "Scissors"}}; 
    if (comp == user) {
        cout << "It's a tie!" << endl;
    } else if (user == 2 && comp == 0) {
        cout << "I chose " << options[comp] << ". You Lost!" << endl;
    } else if (user == 0 && comp == 2) {
        cout << "I chose " << options[comp] << ". You Won!" << endl;
    } else if (user > comp) {
        cout << "I chose " << options[comp] << ". You Won!" << endl;
    } else {
        cout << "I chose " << options[comp] << ". You Lost!" << endl;
    }
}

int main()
{   
    int userChoice;
    
    srand(time(0));
    int compChoice = rand() % 4;
    
    cout << "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ";
    cin>>userChoice;
    
    find_winner(compChoice, userChoice);
    
}
