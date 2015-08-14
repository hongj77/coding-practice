/* Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself). */

#include <iostream>
#include <vector>

using namespace std;


struct Node {
  int key;
  struct Node *left, *right;
};


Node* newNode(int k) {
  Node *temp = new Node;
  temp->key = k;
  temp->left = NULL;
  temp->right = NULL;
  return temp;
}


int findLCA(Node* root, int n1, int n2) {
  if (root == NULL) {
    return -1;
  }
  if (root->key == n1 || root->key == n2) {
    return root->key;
  }
  int left = findLCA(root->left, n1, n2);
  int right = findLCA(root->right, n1,n2); 
  
  // one value in left side, one value in right side
  if (left != -1 && right != -1) {
    return root->key;
  }
  // both in left
  if (left != -1) {
    return left;
  }
  // both in right
  if (right != -1) {
    return right;
  }
  return -1;
}


int main() {
  Node* root = newNode(1);
  root->left = newNode(2);
  root->right = newNode(3);
  root->left->left = newNode(4);
  root->left->right = newNode(5);
  root->right->left = newNode(6); 
  root->right->right = newNode(7);

  cout<<findLCA(root,4,5) << endl;
  cout<<findLCA(root,3,6) << endl;
  cout<<findLCA(root,7,5) << endl;

  return 0;
}


