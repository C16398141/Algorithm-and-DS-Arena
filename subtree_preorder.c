// Create a Binary Search Tree from list A
// A containing N elements. Insert elements in the same order as given.
// Print the pre-order traversal of the subtree with root node data equal to
// Q (inclusive of Q), separating each element by a space.
// 
// 	input:
// 	size:	4
// 	array elements:2 1 3 4
// 	print from subtree: 3
// 
// 	output:
// 	3 4

#include<stdio.h>
#include<stdlib.h>
#define SIZE 5

struct node
{
    int data;
    struct node* left;
    struct node* right;
};

struct node* search(struct node* root, int value);
void insert(struct node**root,int value);
void pre_order(struct node* root);
void free_all(struct node *root);


int main(void)
{
    int array[SIZE]={2,1,3,4,5};
    struct node *root = NULL;
    struct node *found = NULL;
    int search_this = 0;

	for (int i=0; i<SIZE; i++)
		insert(&root, array[i]);
	
    printf("Enter a value to search\n>>");
    scanf("%d",&search_this);
    
    if((found= search(root, search_this)) != NULL)
	{
		pre_order(found);
		putchar('\n');
	}
    else
        fprintf(stderr,"%d not found in the tree\n", search_this);
        
    free_all(root);
    free(found);
    return 0;
}


struct node* search(struct node * root, int value)
{
    if (root != NULL)
    {
        if(root->data == value)
            return root;
        else if (root->data > value)
            return search(root->left,value);
        else
            return search(root->right, value);
    }
    return NULL;
}

void insert(struct node** root,int value)
{
    if(*root == NULL)
    {
        (*root) = (struct node*) malloc(sizeof(struct node));
        (*root)->data = value;
        (*root)->left = (*root)->right = NULL;
    }
    else if ((*root)->data > value)
        insert(&(*root)->left, value);
    else
        insert(&(*root)->right, value);
}


void pre_order(struct node* root)
{
    if(root != NULL)
    {
        printf("%d ",root->data);
        pre_order(root->left);
        pre_order(root->right);
    }
}

void free_all(struct node *root)
{
    if(root != NULL)
	{
        free_all((*root).left);
		free_all((*root).right);
        free(root);
    }
}
