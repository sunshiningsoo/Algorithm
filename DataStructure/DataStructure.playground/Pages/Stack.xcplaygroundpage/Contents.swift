import SwiftUI

struct Stack<T> {
    var stack: [T] = []
    
    var count: Int {
        return stack.count
    }
    
    var isEmpty: Bool {
        return stack.isEmpty
    }
    
    mutating func push(_ element: T) {
        stack.append(element)
    }
    
    mutating func pop() -> T? {
        return isEmpty ? nil : stack.popLast()
    }
}

var stack = Stack<Int>()

stack.push(1)
stack.push(2)

stack.pop()
stack.pop()
stack.pop()
