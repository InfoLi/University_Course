#pragma once
#ifndef BSTNode_H
#define BSTNode_H
#include "BinNode.h"
#include <iostream>
using namespace std;
template <typename Key, typename E>
class BSTNode : public BinNode<E> {
private:
  //键值 值 左右指针
  Key k;                 
  E it;                   
  BSTNode* lc;           
  BSTNode* rc;           

public:
  BSTNode() { lc = rc = NULL; }
  BSTNode(Key K, E e, BSTNode* l =NULL, BSTNode* r =NULL)
    { k = K; it = e; lc = l; rc = r; }
  ~BSTNode() {} 
  //设置和返回 值和键值
  E& element() { return it; }
  void setElement(const E& e) { it = e; }
  Key& key() { return k; }
  void setKey(const Key& K) { k = K; }
  //设置和返回 左右指针
  inline BSTNode* left() const { return lc; }
  void setLeft(BinNode<E>* b) { lc = (BSTNode*)b; }
  inline BSTNode* right() const { return rc; }
  void setRight(BinNode<E>* b) { rc = (BSTNode*)b; }
  //判断
  bool isLeaf() { return (lc == NULL) && (rc == NULL); }
};
#endif