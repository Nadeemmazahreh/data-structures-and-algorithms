
class Node:
  def __init__(self, value):
      self.value = value
      self.next = None

class LinkedList:
  def __init__(self):
      self.head = None

  def insert(self,value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node

  def includes(self,str):
    current = self.head
    string =""

    while current.value != None:
      if current.value != str:
       current = current.next
       string = "No value"

      else:
        string = "Value present"
        break

    return string

  def append(self,value):

      node = Node(value)
      current = self.head
        
      while current.next:
          current = current.next
      current.next = node




  def __str__(self):

    string = ""
    current = self.head

    while current:
      string += f"{str(current.value)} -> "
      current = current.next
    string += "None"
    return string


if __name__ == "__main__":
  ll = LinkedList()
  ll.insert("a")
  ll.insert("b")
  ll.insert("c")
  print(ll)
  ll.includes("d")



