#pragma once
#ifndef BSTNode_H
#define BSTNode_H
#include "BinNode.h"
#include <iostream>
using namespace std;
template <typename Key, typename E>
class BSTNode : public BinNode<E> {
private:
  //��ֵ ֵ ����ָ��
  Key k;                 
  E it;                   
  BSTNode* lc;           
  BSTNode* rc;           

public:
  BSTNode() { lc = rc = NULL; }
  BSTNode(Key K, E e, BSTNode* l =NULL, BSTNode* r =NULL)
    { k = K; it = e; lc = l; rc = r; }
  ~BSTNode() {} 
  //���úͷ��� ֵ�ͼ�ֵ
  E& element() { return it; }
  void setElement(const E& e) { it = e; }
  Key& key() { return k; }
  void setKey(const Key& K) { k = K; }
  //���úͷ��� ����ָ��
  inline BSTNode* left() const { return lc; }
  void setLeft(BinNode<E>* b) { lc = (BSTNode*)b; }
  inline BSTNode* right() const { return rc; }
  void setRight(BinNode<E>* b) { rc = (BSTNode*)b; }
  //�ж�
  bool isLeaf() { return (lc == NULL) && (rc == NULL); }
};
#endif