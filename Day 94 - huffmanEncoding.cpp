// Given a string S of distinct character of size N and their corresponding frequency 
// Your task is to build the Huffman tree print all the huffman codes in preorder traversal of the tree
// Day 94 / 100


#include <bits/stdc++.h>
using namespace std;

class Solution
{

	struct Node
	{
		int freq;
		Node *left = NULL;
		Node *right = NULL;
		Node(int f)
		{
			freq = f;
		}
	};

	class comp
	{
	public:
		bool operator()(Node *l1, Node *l2)
		{
			return l1->freq > l2->freq;
		}
	};

	void preorder(Node *node, string s, vector<string> &res)
	{
		if (node == NULL)
			return;
		if (node->left == NULL && node->right == NULL)
		{
			res.push_back(s);
			return;
		}
		if (node->left)
			preorder(node->left, s + '0', res);
		if (node->right)
			preorder(node->right, s + '1', res);
	}

public:
	vector<string> huffmanCodes(string S, vector<int> f, int N)
	{
		priority_queue<Node *, vector<Node *>, comp> pq;
		for (auto it : f)
			pq.push(new Node(it));
		while (pq.size() > 1)
		{
			Node *first = pq.top();
			pq.pop();
			Node *second = pq.top();
			pq.pop();
			Node *newNode = new Node(first->freq + second->freq);
			newNode->left = first;
			newNode->right = second;
			pq.push(newNode);
		}
		vector<string> res;
		preorder(pq.top(), "", res);
		return res;
	}
};

// Driver Code Starts.
int main()
{
	int T;
	cin >> T;
	while (T--)
	{
		string S;
		cin >> S;
		int N = S.length();
		vector<int> f(N);
		for (int i = 0; i < N; i++)
		{
			cin >> f[i];
		}
		Solution ob;
		vector<string> ans = ob.huffmanCodes(S, f, N);
		for (auto i : ans)
			cout << i << " ";
		cout << "\n";
	}
	return 0;
}