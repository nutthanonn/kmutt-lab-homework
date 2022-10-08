#include <iostream>
using namespace std;


class Node 
{
    public:
        string filename;
        int file_sizes;
        Node *parent;
        Node *leftChild;
        Node *rightSibling;
};

Node *createRoot(string filename, int file_sizes)
{
    Node *node = new Node();
    node->filename = filename;
    node->file_sizes = file_sizes;
    node->leftChild = NULL;
    node->rightSibling = NULL;
    node->parent = NULL;
    return node;
}


Node *createNode(string filename,int file_sizes, Node *parent)
{
    Node *node = new Node();
    node->filename = filename;
    node->file_sizes = file_sizes;
    node->parent = parent;
    node->leftChild = NULL;
    node->rightSibling = NULL;
    if(node->parent != NULL) {
        if(node->parent->leftChild != NULL) {
            Node *child = node->parent->leftChild;

            while(child->rightSibling != NULL)
                child = child->rightSibling;

            child->rightSibling = node;
        }
        else  
            node->parent->leftChild = node;
    }

    return node;
}

Node *getParent(Node *node)
{   
    return node->parent;
}

Node *getChild(Node *node, int k)
{
    Node *child = node->leftChild;
    for(int i=1; i<k; i++)
        child = child->rightSibling;
    return child;
}

void inExternal(Node *node)
{
    if(node->leftChild == NULL)
        printf("Yes\n");
    else
        printf("No\n");
}



void postorder(Node *T, Node *r)
{
    if(r == NULL)
        return;

    int i = 0;
    while (getChild(r, i) != NULL)
    {
        postorder(T, getChild(r, i));
        i++;
    }

    r->parent->file_sizes += r->file_sizes;
    cout << r->filename << "  " << r->file_sizes << endl;
}

int main()
{
    Node *node1 = createRoot("user", 10);
    Node *node2 = createNode("cs016", 2, node1);
    Node *node3 = createNode("cs252", 1, node1);
    Node *node4 = createNode("grades", 8, node2);
    Node *temp = getChild(node1, 0);
    // cout << temp->filename;
    postorder(node1, node1);
    return 0;
}