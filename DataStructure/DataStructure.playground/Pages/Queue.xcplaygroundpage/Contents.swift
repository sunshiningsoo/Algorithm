
import SwiftUI

struct Queue<T> {
    var queue: [T] = []
    
    var count: Int {
        return self.queue.count
    }
    
    var isEmpty: Bool {
        return self.queue.isEmpty
    }
    
    mutating func enqueue(_ element: T) {
        self.queue.append(element)
    }
    
    mutating func dequeue() -> T? {
        return isEmpty ? nil : self.queue.removeFirst()
    }
    
}

var queue = Queue<Int>()

queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
queue.dequeue()
