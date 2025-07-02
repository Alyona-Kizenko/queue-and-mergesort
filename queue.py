from typing import Any, List


class Queue:
    
    def __init__(self) -> None:
        self._items: List[Any] = [] 
    
    def enqueue(self, item: Any) -> None:
        self._items.append(item)
    
    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError()
        return self._items.pop(0)
    
    def is_empty(self) -> bool:
        return not self._items
    
    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError()
        return self._items[0]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)

if __name__ == "__main__":
    queue = Queue()
    
    print(queue.is_empty())
    queue.enqueue(30)
    queue.enqueue(12)
    queue.enqueue(5)
    
    print(queue)
    print(queue.peek())
    print(len(queue))
    print(queue.dequeue())
    print(queue)