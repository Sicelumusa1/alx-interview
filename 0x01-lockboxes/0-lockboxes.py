#!/usr/bin/python3
"""
A module that detemines if all boxes in a list of boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Detemines if all boxes in a list of boxes can be unlocked

    Args:
        boxes (list[list[int]]): A list of boxes where each box contains
        a list list of keys

    Returns:
            bool: True if all boxes can be unlocked, False otherwise.
    """
    #  Initialize a set to keep track of boxes that can be unlocked
    unlocked_boxes = set([0])
    
    #  Initialize the boxes length
    n = len(boxes)

    #  Initialize a queue for BFS traversal
    queue = [0]

    #  BFS traversal
    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]
        for key in keys:
            if key not in unlocked_boxes:
                unlocked_boxes.add(key)
                queue.append(key)
        
        #  Check if all boxes are unlocked and exit early
        if len(unlocked_boxes) == n:
            return True

    return False
