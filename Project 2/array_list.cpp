#include <exception>
#include <iostream>
#include <vector>

using namespace std;

class ArrayList {
   public:
    int size;

   private:
    int* data;
    int capacity;
    int growth;

    void resize() {
        capacity *= 2;
        int* tmp = new int[capacity];
        for (int i = 0; i < size; i++) {
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    }

   public:
    ArrayList() {
        size = 0;
        capacity = 1;
        growth = 2;
        data = new int[capacity];
    }
   // a vector constructor
    ArrayList(vector<int> my_vector){
      size = 0;
      capacity = 1;
      growth = 2;
      data = new int[capacity];
      for (int new_vector : my_vector) {
        append(new_vector);
      }
    }

    ~ArrayList() {
        delete[] data;
    }


    int length() {
      return size;
    }

    void append(int x) {
        if (size >= capacity) {
            resize();
        }
        data[size] = x;
        size++;
    }

    int& get(int i) {
        if ((i < size) && (i >= 0)) {
            return data[i];
        } else {
            throw out_of_range("Index out of range");
        }
    }

    int& operator[](int i) {
      return get(i);
    }

    void print(){
        cout << "[";
        for (int i=0; i < size-1; i++){
            cout << data[i]<< " , ";
        }
        cout << data[size-1] << "]" << '\n';


    }

    void insert(int val, int index){
      if (index < 0 || index > size) {
        throw out_of_range("IndexError");
      }
      size++;
      for(int i = size-1; i > index; i--){
        data[i]= data[i-1];
      }
      data[index]=val;


    }

    void remove(int index){
      if (index < 0 || index > size) {
        throw out_of_range("IndexError");
      }

      for(int i = index; i < size-1 ; i++){
        data[i]= data[i+1];
      }
      size--;
      if (size < 0.25 *capacity) {
        shrink_to_fit();
      }

    }


    int pop(int index){
      int x = data[index];

      if (index < 0 || index > size) {
        throw out_of_range("IndexError");
      }
      remove(index);
      return x;
  }

  int pop(){
    int x = data[size-1];
    for (int i =size-1; i > size-1; i--) {
      data[i] = data[i-1];
}
  size--;
  return x;
  }



bool is_prime(int x){
  if (x <= 1)
    return false;


  for (int i = 2; i < x; i++)
    if (x%i == 0)
        return false;

   return true;
}


void prime_test(){
  ArrayList primes;
  for (int i=0; i<15; i++) {
		if (is_prime(i)) {
			primes.append(i);
		}
	}
	primes.print();
}




int main() {
std::cout << "Test it" << '\n';


    return 0;
}
