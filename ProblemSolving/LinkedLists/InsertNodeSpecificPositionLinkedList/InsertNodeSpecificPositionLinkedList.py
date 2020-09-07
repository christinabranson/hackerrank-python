#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    print("insertNodeAtPosition(head,{},{})".format(str(data), str(position)))

    new_node = SinglyLinkedListNode(data)

    stop = False
    positionCounter = 0
    previous_node = None
    this_node = head
    while not stop and positionCounter <= position:
        print("counter: {} | value: {}".format(positionCounter, this_node.data))
        if positionCounter == position:
            print("inserting here")
            stop = True

            new_node.next = this_node
            previous_node.next = new_node

            #if this_node.next is not None:
            #    next_node = this_node.next
            #    new_node.next = next_node
            #    previous_node.next = new_node
            #else:
            #    previous_node.next = new_node
        positionCounter += 1
        previous_node = this_node
        this_node = this_node.next

    return head

if __name__ == '__main__':
    fptr = open(os.getenv('OUTPUT_PATH', 'InsertNodeSpecificPositionLinkedList.txt'), 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
