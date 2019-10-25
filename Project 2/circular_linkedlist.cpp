#include <iostream>
#include <stdexcept>
#include <vector>

using namespace std;

struct Node{
    int value;
    Node* next;
    Node* prev;

};

class CircularLinkedlist{

private:
  int size;
  Node* head;



public:

  CircularLinkedlist(){

  head = nullptr;
  size = 0;
}


CircularLinkedlist(int c){

  head = nullptr;
  size = 0;
  for (int i = 0; i <= c; i++) {
    append(i);
  }
}
CircularLinkedlist(vector<int> v){
    for (int val : v){
        append(val);
    }
}
int length(){
  return size;
}


  Node* get_node(int index){

      if (head == nullptr){
          throw range_error("IndexError:");
      }
      int step = index % size;
      if (step < 0){
          step = length()+step;
      }


        Node* current = head;
        for (int i=0; i< step; i++) {
            current = current->next;
        }
        return current;

}


int& operator[](int index){
  return get_node(index)->value;
}


void append(int index){

  Node *ny = new Node;
  ny->value = index;
  if(head == NULL){
      head =ny;
      ny->next = ny;
      return;
  }
  else{
    Node *tmp = head;
    ny->next = head;
    while (tmp->next != head) {
      tmp = tmp->next;
    }
    tmp->next = ny;

}
  size++;

}
void remove(Node* tmp){
Node* first = tmp->prev;
Node* last = tmp->next;
last->prev = first;
first->next = last;
if (tmp == head){
    head = tmp->next;
}
size--;
}

void remove(int index){
  Node* tmp = get_node(index);
  remove(tmp);

}



void print() {

    Node *current = head;
    cout << "[ ";
    for (int i=0; i< size;i++) {
        cout << current->value << ',';
        current = current->next;

    }
    cout << current->value << "...]" << endl;
}
vector<int> j_sequence(int k){
        Node* tmp = head;
        Node* after;
        vector<int> r;

        while (length() != 0){
            for(int i = 1; i< k; i++){
                tmp = tmp->next;
            }
            r.append(tmp->value);
            after = tmp->next;
            remove(tmp);
            tmp = after;

        }
        return r;
    }


};
int last_man(int n, int k){
    CircularLinkedlist cc(n);
    vector<int> kill = cc.j_sequence(k);
    return kill.back();
}
int main() {
std::cout << " TEST IT" << '\n';
  return 0;
}
