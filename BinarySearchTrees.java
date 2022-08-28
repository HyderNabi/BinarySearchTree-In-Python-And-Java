//Author : Hyder Nabi
//TODO : Implementation of BST
class Node
{
	int key;
	Node left;
	Node right;
}
class BST
{
	public Node root;
	
	public BST() {
		root = null;
	}
	
	public BST(int arr[]){
		for(int i = 0;i<arr.length;i++)
		{
			this.root = insert(this.root,arr[i]);
		}
	}
	
	public void create(int arr[]){
		for(int i = 0;i<arr.length;i++)
		{
			this.root = insert(this.root,arr[i]);
		}
	}
	
	
	public Node insert(Node root,int elem)
	{
		if(root == null)
		{
			root = new Node();
			root.key = elem;
			root.left = null;
			root.right = null;
		}else {
			if(elem>=root.key) {
				root.right =  insert(root.right,elem);
			}else {
				 root.left = insert(root.left,elem);
			}
		}
		return root;
	}
	
	public Node delete(Node root, int key) {
		if(root == null){
			System.out.println("Node Not found");
			return null;
		}else if(key > root.key){
			root.right = delete(root.right,key);			
			return root;
		}else if(key<root.key) {
			root.left = delete(root.left,key);
			return root;
		}else {
			//when key is equal to the root.key
			if(root.left != null && root.right != null)
			{
				Node largestNode = findLargest(root.left);
				root.key = largestNode.key;
				root.left = delete(root.left,largestNode.key);
				return root;
			}else if(root.left == null && root.right == null){
				return null;
			}else if(root.left != null){
				Node temp = root.left;
				root = null;
				return temp;
			}else {
				Node temp = root.right;
				root = null;
				return temp;
			}
		}
		
	}
	
	public Node findLargest(Node root)
	{
		if(root == null || root.right == null){
			return root;
		}else {
			return findLargest(root.right);
		}
	}
	
	public void inOrder(Node root) {
		if(root.left != null)
			inOrder(root.left);
		
		System.out.println(root.key);
		
		if(root.right != null)
			inOrder(root.right);
	}
	
	public void postOrder(Node root)
	{
		if(root == null)
		{
			return;
		}else {
			postOrder(root.left);
			postOrder(root.right);
			System.out.print(root.key+" ");
		}
	}
}
public class BinarySearchTrees {

	public static void main(String[] args) {
	//	int arr[] = new int[] {45, 39, 56, 12, 34, 78, 32, 10, 89, 54, 67, 81};
		int arr[] = new int[] {5,8,1,89,23,34,45,98,102,4,3};
		BST bst = new BST();
		bst.create(arr);
		bst.inOrder(bst.root);
		System.out.println();
		bst.delete(bst.root, 89);
		bst.inOrder(bst.root);
		bst.postOrder(bst.root);

	}

}
