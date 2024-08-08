#include <iostream>
#include <conio.h>

using namespace std;

class Queue {
private:
    int queue1[5];
    int front, rear;

public:
    Queue() {
        front = -1;
        rear = -1;
    }

    bool isFull() {
        return rear == 4;
    }

    bool isEmpty() {
        return front == rear;
    }

    void enqueue(int x) {
        if (isFull()) {
            cout << "Queue overflow" << endl;
            return;
        }
        queue1[++rear] = x;
        cout << "Inserted: " << x << endl;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Queue underflow" << endl;
            return;
        }
        cout << "Deleted: " << queue1[++front] << endl;
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue empty" << endl;
            return;
        }
        for (int i = front + 1; i <= rear; i++) {
            cout << queue1[i] << " ";
        }
        cout << endl;
    }
};

int main() {
	
    Queue qu;
    int ch, x;

    while (true) {
        cout << "\n1. Insert \n2. Delete \n3. Display \n4. Exit \nEnter your choice: ";
        cin >> ch;

        switch (ch) {
            case 1:
                cout << "Enter the element: ";
                cin >> x;
                qu.enqueue(x);
                break;
            case 2:
                qu.dequeue();
                break;
            case 3:
                qu.display();
                break;
            case 4:
                exit(0);
            default:
                cout << "Invalid choice" << endl;
        }
    }
    return 0;
}
