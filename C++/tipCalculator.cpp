#include <bits/stdc++.h>
using namespace std;

int main()
{
    int tipPercent, numOfPeople, totalAmt, finalAmount, totalWithTip;
    
    float billTotal;
    
    cout<<"Welcome to the tip calculator!\n";
    
    cout<<"What was the total bill? ";
    cin>>billTotal;
    
    cout<<"How much tip would you like to give? 10, 12, or 15? ";
    cin>>tipPercent;
    
    cout<<"How many people to split the bill? ";
    cin>>numOfPeople;
    
    totalWithTip = billTotal + (billTotal * tipPercent / 100);
    
    finalAmount = ceil(totalWithTip / numOfPeople);
    
    cout<<"Each person should pay: " << finalAmount << ".";
}
