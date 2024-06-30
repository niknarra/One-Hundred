#include <bits/stdc++.h>
using namespace std;

int main()
{
    char cityName[30], petName[30];
    
    cout<<"Welcome to Band Name Generator\n";
    
    cout<<"Let's get started. What's the name of the city you grew up in?\n";
    cin>>cityName;
    
    cout<<"Nice! Moving on, what's the name of your pet? \n";
    cin>>petName;
    
    cout<<"Awesome! Your band name could be " << cityName <<" " << petName << ".";
}
