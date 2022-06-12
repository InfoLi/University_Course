#pragma once
#ifndef BinNode_H
#define BinNode_H
#include <iostream>
using namespace std;
template <typename E> class BinNode {
public:
  virtual ~BinNode() {} 
  virtual E& element() = 0;	//����Ԫ�ص�ֵ
  virtual void setElement(const E&) = 0;	//����Ԫ�ص�ֵ
  virtual BinNode* left() const = 0;	//������ڵ�
  virtual void setLeft(BinNode*) = 0;	//������ڵ�
  virtual BinNode* right() const = 0;	//�����ҽڵ�
  virtual void setRight(BinNode*) = 0;	//�����ҽڵ�
  virtual bool isLeaf() = 0;	//�ж��Ƿ�ΪҶ�ӽڵ�
};
#endif