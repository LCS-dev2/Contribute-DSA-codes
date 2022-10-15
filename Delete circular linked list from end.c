#include <stdio.h>
#include <stdlib.h>
struct node{
    int data;
    struct node *next;
};
int main(){
    struct node *newnode,*tail,*current,*prev;
    int choice;
    tail=0;
    while(choice){
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("Enter the data: ");
        scanf("%d",&newnode->data);
        newnode->next=0;
        if(tail==0){
            tail=newnode;
            tail->next=newnode;
        }
        else{
            newnode->next=tail->next;
            tail->next=newnode;
            tail=newnode;
        }
        printf("Do you wanna continue (0,1): ");
        scanf("%d",&choice);
    }

    current=tail->next;
    while(current->next!=tail->next){
        prev=current;
        current=current->next;
    }
    prev->next=tail->next;
    tail=prev;
    free(current);
    printf("After deleting element from emd the resultant elements in the list are: ");
    current=tail->next;
    do{
        printf("%d ",current->data);
        current=current->next;
    }while(current!=tail->next);
}
