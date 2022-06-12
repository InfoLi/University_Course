#pragma once
#ifndef BST_H
#define BST_H
#include "BSTNode.h"
#include "dictionary.h"
#include <iostream>
using namespace std;
template <typename Key, typename E>
class BST : public Dictionary<Key,E> {
private:
  BSTNode<Key,E>* root;   
  int nodecount;          //树节点数
  void clearhelp(BSTNode<Key, E>*);
  BSTNode<Key,E>* inserthelp(BSTNode<Key, E>*,const Key&, const E&);
  BSTNode<Key,E>* deletemin(BSTNode<Key, E>*);
  BSTNode<Key,E>* getmin(BSTNode<Key, E>*);
  BSTNode<Key,E>* removehelp(BSTNode<Key, E>*, const Key&);
  E findhelp(BSTNode<Key, E>*, const Key&) const;
  void printhelp(BSTNode<Key, E>*, int) const;

  int countsumhelp(BSTNode<Key, E>*) const;
public:
  BST() { root = NULL; nodecount = 0; }  
  ~BST() { clearhelp(root); }            

  void clear()  //初始化树
    { clearhelp(root); root = NULL; nodecount = 0; }

  void insert(const Key& k, const E& e) {   //插入节点
    root = inserthelp(root, k, e);
    nodecount++;
  }

  E remove(const Key& k) {  //删除节点
    E temp = findhelp(root, k); 
    if (temp != NULL) {
      root = removehelp(root, k);
      nodecount--;
    }
    return temp;
  }

  E removeAny() {  //删除最大值的节点
    if (root != NULL) {
      E temp = root->element();
      root = removehelp(root, root->key());
      nodecount--;
      return temp;
    }
    else return NULL;
  }

  E find(const Key& k) const { return findhelp(root, k); }

  int size() { return nodecount; }

  void print() const {  //输出树
    if (root == NULL) cout << "The BST is empty.\n";
    else printhelp(root, 0);
  }

  int countsum() const { //求节点数
      if (root == NULL) cout << "The BST is empty.\n";
      else return countsumhelp(root);
  }
};

template <typename Key, typename E>
void BST<Key, E>::clearhelp(BSTNode<Key, E>* root) {
  if (root == NULL) return;
  clearhelp(root->left());
  clearhelp(root->right());
  delete root;
}

template <typename Key, typename E>
BSTNode<Key, E>* BST<Key, E>::inserthelp(BSTNode<Key, E>* root, const Key& k, const E& it) {
  if (root == NULL)  
    return new BSTNode<Key, E>(k, it, NULL, NULL);
  if (k < root->key())
    root->setLeft(inserthelp(root->left(), k, it));
  else root->setRight(inserthelp(root->right(), k, it));
  return root;     
}

template <typename Key, typename E>
BSTNode<Key, E>* BST<Key, E>::getmin(BSTNode<Key, E>* rt) {
  if (rt->left() == NULL)
    return rt;
  else return getmin(rt->left());
}

template <typename Key, typename E>
BSTNode<Key, E>* BST<Key, E>::deletemin(BSTNode<Key, E>* rt) {
  if (rt->left() == NULL) 
    return rt->right();
  else {                     
    rt->setLeft(deletemin(rt->left()));
    return rt;
  }
}

template <typename Key, typename E>
BSTNode<Key, E>* BST<Key, E>::removehelp(BSTNode<Key, E>* rt, const Key& k) {
  if (rt == NULL) return NULL;    
  else if (k < rt->key())
    rt->setLeft(removehelp(rt->left(), k));
  else if (k > rt->key())
    rt->setRight(removehelp(rt->right(), k));
  else {                            
    BSTNode<Key, E>* temp = rt;
    if (rt->left() == NULL) {     
      rt = rt->right();        
      delete temp;
    }
    else if (rt->right() == NULL) { 
      rt = rt->left();       
      delete temp;
    }
    else {                    
      BSTNode<Key, E>* temp = getmin(rt->right());
      rt->setElement(temp->element());
      rt->setKey(temp->key());
      rt->setRight(deletemin(rt->right()));
      delete temp;
    }
  }
  return rt;
}

template <typename Key, typename E>
E BST<Key, E>::findhelp(BSTNode<Key, E>* root,const Key& k) const {
  if (root == NULL) return NULL;         
  if (k < root->key())
    return findhelp(root->left(), k);   
  else if (k > root->key())
    return findhelp(root->right(), k);  
  else return root->element();  
}

template <typename Key, typename E>
void BST<Key, E>::printhelp(BSTNode<Key, E>* root, int level) const {
  if (root == NULL) return;           
  printhelp(root->left(), level+1);   
  for (int i=0; i<level; i++)         
    cout << "  ";
  cout << root->key() << "\n";       
  printhelp(root->right(), level+1); 
}

template <typename Key, typename E>
int BST<Key, E>::countsumhelp(BSTNode<Key, E>* root) const {
    int sum1,sum2;
    if (root == NULL) return(0);
    sum1 = countsumhelp(root->left());
    sum2 = countsumhelp(root->right());
    return(sum1+sum2+root->key());
}

#endif