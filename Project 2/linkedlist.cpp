#include <iostream>

using namespace std;

struct Node {
    int value;
    Node *next;

    Node(int v) {
        value = v;
        next = nullptr;
    }
    Node(int v, Node *n) {
        value = v;
        next = n;
    }
};

class LinkedList {
   private:
    Node *head;
    int size;

    Node *get_node(int index) {
        int size = length();
        if (index < 0 or index >= size) {
            throw range_error("IndexError: Index out of range");
        }

        Node *current = head;
        for (int i = 0; i < index; i++) {
            current = current->next;
        }
        return current;
    }

   public:
    LinkedList() {
        size = 0;
        head = nullptr;
    }

    ~LinkedList() {
        size = 0;
        Node *current;
        Node *next;

        current = head;
        while (current->next != nullptr) {
            next = current->next;
            delete current;
            current = next;
        }
    }

    void push_front(int val) {
        head = new Node(val, head);
        size++;
    }

    void insert(int val, int index) {
        size++;
        if (index == 0) {
            push_front(val);
        } else {

            Node *prev = get_node(index - 1);
            Node *next = prev->next;
            Node *current = new Node(val, next);
            prev->next = current;
        }
    }

    void append(int value) {
        size++;
        if (head == nullptr) {
            head = new Node(value);
        } else {
            Node *current = head;
            while (current->next != nullptr) {
                current = current->next;
            }

            current->next = new Node(value);
        }
    }

    void print() {
        Node *current = head;

        cout << "[";
        while (current != nullptr) {
            cout << current->value;
            current = current->next;
            if (current != nullptr) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }

    int length() {
        int len = 0;

        Node *current = head;
        while (current != nullptr) {
            len++;
            current = current->next;
        }
        return len;
    }
    int storrelse(){
      return size;
    }

    int &operator[](int index) {
        Node *current = get_node(index);
        return current->value;
    }

    void remove(int index){
      if (index < 0 or index >= size) {
        throw range_error("IndexError: Index out of range");
    }
      size--;
      Node *tmp = head;
      if (index == 0) {
        head = tmp->next;
      }

      for (int i = 0; i < index-1; i++) {
        tmp = tmp->next;
      }

      tmp->next = tmp->next->next;

    }

    int pop(){
      Node *tmp = get_node(size-1);
      int x = tmp->value;
      remove(size-1);
      size--;
      return x;
    }
    int pop(int index){
      if (index < 0 or index >= size) {
        throw range_error("IndexError: Index out of range");
    }
    Node *tmp = get_node(index);
    int x = tmp->value;
    remove(index);
    size--;
    return x;
    }
};

int main() {
  std::cout << "Test it" << '\n';


    return 0;
}
