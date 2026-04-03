/*
class Node {
  public:
    int data;
    Node* left;
    Node* right;

    // Constructor to initialize a new node
    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};
*/

class Solution {
public:

    bool isleaf(Node* node) {
        return node->left == NULL && node->right == NULL;
    }

    void addLeft(Node* root, vector<int>& res) {
        Node* curr = root->left;
        while (curr) {
            if (!isleaf(curr))
                res.push_back(curr->data);

            if (curr->left)
                curr = curr->left;
            else
                curr = curr->right;
        }
    }

    void addLeaves(Node* root, vector<int>& res) {
        if (isleaf(root)) {
            res.push_back(root->data);
            return;
        }
        if (root->left)
            addLeaves(root->left, res);
        if (root->right)
            addLeaves(root->right, res);
    }

    void addRight(Node* root, vector<int>& res) {
        Node* curr = root->right;
        vector<int> temp;

        while (curr) {
            if (!isleaf(curr))
                temp.push_back(curr->data);

            if (curr->right)
                curr = curr->right;
            else
                curr = curr->left;
        }

        // reverse right boundary
        for (int i = temp.size() - 1; i >= 0; i--) {
            res.push_back(temp[i]);
        }
    }

    vector<int> boundaryTraversal(Node* root) {
        vector<int> res;
        if (root == NULL)
            return res;

        if (!isleaf(root))
            res.push_back(root->data);

        addLeft(root, res);
        addLeaves(root, res);
        addRight(root, res);

        return res;
    }
};
