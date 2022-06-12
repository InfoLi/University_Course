#pragma once
#ifndef BinNode_H
#define BinNode_H
#include <iostream>
using namespace std;
template <typename E> class BinNode {
public:
  virtual ~BinNode() {} 
  virtual E& element() = 0;	//返回元素的值
  virtual void setElement(const E&) = 0;	//设置元素的值
  virtual BinNode* left() const = 0;	//返回左节点
  virtual void setLeft(BinNode*) = 0;	//设置左节点
  virtual BinNode* right() const = 0;	//返回右节点
  virtual void setRight(BinNode*) = 0;	//设置右节点
  virtual bool isLeaf() = 0;	//判断是否为叶子节点
};
#endif