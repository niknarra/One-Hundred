#include <bits/stdc++.h>
using namespace std;

int main() {
    // Seed the random number generator
    srand(time(0));

    // Define the symbols
    vector<char> symbols = {'~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', '<', '>', '?'};

    // Define the letters
    vector<char> letters;
    for (char i = 'a'; i <= 'z'; ++i) letters.push_back(i);
    for (char i = 'A'; i <= 'Z'; ++i) letters.push_back(i);

    // Print the letters for debugging
    for (char letter : letters) {
        cout << letter << " ";
    }
    cout << endl;

    cout << "Welcome to the C++Password Generator!" << endl;

    // Get the number of letters, symbols, and numbers from the user
    int numOfLetters, numOfSymbols, numOfNums;
    cout << "How many letters would you like in your password?" << endl;
    cin >> numOfLetters;

    cout << "How many symbols would you like?" << endl;
    cin >> numOfSymbols;

    cout << "How many numbers would you like?" << endl;
    cin >> numOfNums;

    int totalLen = numOfLetters + numOfNums + numOfSymbols;

    vector<char> password;

    // Add random letters to the password
    for (int i = 0; i < numOfLetters; ++i) {
        password.push_back(letters[rand() % letters.size()]);
    }

    // Add random symbols to the password
    for (int i = 0; i < numOfSymbols; ++i) {
        password.push_back(symbols[rand() % symbols.size()]);
    }

    // Add random numbers to the password
    for (int i = 0; i < numOfNums; ++i) {
        password.push_back('0' + rand() % 10);  // '0' + rand() % 10 generates a random digit
    }

    // Shuffle the password
    random_shuffle(password.begin(), password.end());

    // Convert the password vector to a string
    string finalPwd(password.begin(), password.end());

    cout << "Your password could be: " << finalPwd << endl;

    return 0;
}

