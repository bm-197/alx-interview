"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 
and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
    """
    A method that determines if all the boxes can be
    opened.

    Args:
        boxes (List[List[int]]): the boxes holding the key
    Return:
        boolean: True if all can be open, False otherwise
    """
    from collections import deque

    visted = set()
    boxs = deque()
    boxs.append(0)

    while boxs:
        box = boxs.popleft()

        if box not in visted:
            visted.add(box)
            for key in boxes[box]:
                if key not in visted:
                    boxs.append(key)

    for i in range(len(boxes)):
        if i not in visted:
            return False
    
    return True #all boxes are opened

