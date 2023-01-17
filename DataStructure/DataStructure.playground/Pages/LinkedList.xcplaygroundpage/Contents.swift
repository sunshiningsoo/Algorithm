
import SwiftUI

class Node<T> {
    var data: T
    var next: Node?
    
    init(data: T, next: Node?) {
        self.data = data
        self.next = next
    }
    
    deinit {
        print("\(data) is deinit")
    }
    
}

class LinkedList<T: Equatable> {
    private var head: Node<T>?
    private var count: Int = 0
    
    func append(data: T) {
        if head == nil {
            head = Node(data: data, next: nil)
            count += 1
            return
        }
        
        var node = head // head의 위치를 직접 바꾸는 과정이 아님
        while node?.next != nil {
            node = node?.next
        }
        node?.next = Node(data: data, next: nil)
        count += 1
    }
    
    func insert(data: T, at index: Int) {
        if count == index {
            self.append(data: data)
            return
        }
        if count - 1 < index {
            print("Wrong Insert index!")
            return
        }
        if head == nil {
            head = Node(data: data, next: nil)
            count += 1
            return
        }
        
        if index == 0 {
            var node = Node(data: data, next: head)
            head = node
            count += 1
            return
        }
        
        var node = head
        for _ in 0..<index-1 {
            node = node?.next
        }
        var insertNode = Node(data: data, next: node?.next)
        node?.next = insertNode
        count += 1
    }
    
    func removeLast() {
        // 데이터가 없을때
        if head == nil {
            return
        }
        
        // 데이터가 head 하나 있을때
        if head?.next == nil {
            head = nil
            count -= 1
            return
        }
        
        var node = head
        while node?.next?.next != nil {
            node = node?.next
        }
        
        node?.next = node?.next?.next
        count -= 1
    }
    
    func remove(at index: Int) {
        if head == nil {
            return
        }
        if count - 1 < index {
            print("Wrong remove Index")
            return
        }
        if count - 1 == index {
            self.removeLast()
            return
        }
        if index == 0 {
            var node = head
            head = node?.next
            node?.next = nil
            count -= 1
            return
        }
        
        var node = head
        for _ in 0..<index-1 {
            node = node?.next
        }
        
        node?.next = node?.next?.next
        count -= 1
    }
    
    func searchNode(at data: T) -> Node<T>? {
        var node = head
        
        while node?.data != data {
            node = node?.next
            if node == nil {
                return nil
            }
        }
        
        return node
    }
    
    func printAllNode() {
        var node = head
        while node != nil {
            print(node?.data ?? "No Data", "count: \(count)")
            node = node?.next
        }
        print("----------")
    }
    
}

var linkedList = LinkedList<Int>()
