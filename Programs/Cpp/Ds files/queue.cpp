#include <iostream>
#include <queue>
using namespace std;

void display_queue(queue<string>q);

int main()
{
    queue<string>animals;
    animals.push("Cat");
    animals.push("Dog");
    animals.push("Fox");

    cout << "Initial Queue:";
    display_queue(animals);
    animals.pop();

    cout << "Final Queue:";
    display_queue(animals);
    return 0;
}

void display_queue(queue<string>q)
{
    queue<string> temp = q;

    while (!temp.empty()) {
        cout << temp.front() << ",";
        temp.pop();
    }

    cout << endl;
}
