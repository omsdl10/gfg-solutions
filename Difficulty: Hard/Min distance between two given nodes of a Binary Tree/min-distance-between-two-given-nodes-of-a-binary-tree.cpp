class Solution {
  public:

    Node* Lca(Node* root, int a, int b) {
        if(root == NULL) return NULL;

        if(root->data == a || root->data == b)
            return root;

        Node* left = Lca(root->left, a, b);
        Node* right = Lca(root->right, a, b);

        if(left && right) return root;

        return (left != NULL) ? left : right;
    }

    int distance(Node* root, int value, int level) {
        if(root == NULL) return -1;

        if(root->data == value) return level;

        int left = distance(root->left, value, level + 1);
        if(left != -1) return left;

        return distance(root->right, value, level + 1);
    }

    int findDist(Node* root, int a, int b) {
        Node* lca = Lca(root, a, b);

        int d1 = distance(lca, a, 0);
        int d2 = distance(lca, b, 0);

        return d1 + d2;
    }
};