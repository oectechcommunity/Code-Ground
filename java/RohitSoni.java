package dataStructure;
// Program to create a linkedList using the basic logic.

public class LinkedList 
{
	Node head;
	static class Node
	{
		int data;
		Node next;
		Node(int d)
		{
			data = d;
			next = null;
		}
		
	}
	
	public static void main(String[] args) 
	{
		LinkedList list = new LinkedList();
		list.head = new Node(1);
		Node second = new Node(2);
		Node third = new Node(3);
		Node fourth = new Node(4);
		
		list.head.next = second;
		second.next = third;
		third.next = fourth;
		
		list.push(0);
		list.push(-1);
		
		list.insertAfter(third, 10);
		
		list.append(11);
		list.append(12);
		
		list.deleteNode(12);
		
		list.printList();
		
		
	}
	
     //method is used to print the list.
	
	public void printList() 
	{
		Node n = head;
		while(n != null)
		{
			System.out.println(n.data+" ");
			n = n.next;
		}
		
	}
	
	// The method to insert a new node at the front of the linked list.
	
	public void push(int new_data)
	{
		Node new_node = new Node(new_data);
        //Assign next of new node as head.
		new_node.next = head;
		// Move the head to point the new node
		head = new_node;
		
	}
	
	//This method is used to addd the element after the given node, in place of prev_node we have to write the variable used for the Node. 
	
	public void insertAfter(Node prev_node, int new_data) 
	{
		if(prev_node == null)
		{
			System.out.println("The given node can not be null.");
			return;
		}
		// Allocate the node and put the data into it.
		
		Node new_node = new Node(new_data);
		
		// make next of new_node as the next of prev_node.
		
		new_node.next = prev_node.next;
		
		// make next of prev_node as new node.
		
		prev_node.next = new_node;
		
	}
	
	// This method is used to add the element at the last of the node.
	
	public void append(int new_data) 
	{
		Node new_node = new Node(new_data);
		
		//Check whether the LinkedList is empty then make the new node as head.
		
		if(head == null)
		{
			head = new Node(new_data);
			return;
			
		}
		
		// make the next of new_node as null as it is the last node.
		
		new_node.next = null;
		
		// take a temporary node last and make it head.
		
		Node last = head;
		
		// iterate the node to find the last node.
		
		while(last.next != null)
		{
		    last = last.next;
		}
		
		// assign the next of last node as new_node.
		
		last.next = new_node;
		return;
    }
	
	// This method is used to delete the node from the linkedList by using the entred data.
	
	public void deleteNode(int key)
	{
		// store the head into the temp.
		Node temp = head, prev = null;
		
		//If the head node itself is the key.
		if (temp != null && temp.data == key) 
		{
			head = temp.next;
			return;
		}
		
		//Search for the key to be deleted.
		while (temp != null && temp.data != key) 
		{
			prev = temp;
			temp =  temp.next;
		}
		
		//if key is not present in the linked list.
		if (temp == null) 
		{
			return;
		}
		// Unlink the node from the linked list.
		prev.next = temp.next;
	}
	
	
	
	

}
