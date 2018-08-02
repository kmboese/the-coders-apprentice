def pop(queue):
    ret = None
    if not queue:
        print("Error: cannot pop an empty queue!")
        return ret
    else:
        ret = queue[0]
        queue.remove(queue[0])
        return ret