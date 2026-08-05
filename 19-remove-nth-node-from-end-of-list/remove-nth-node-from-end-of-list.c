/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    int count=0;
    struct ListNode *temp=head;
    struct ListNode *temp1=temp;
    while(temp!=NULL)
    {
        count++;
        temp=temp->next;
    }
    if(count==n)
    {
        head=temp1->next;
        return head;
    }
    for(int i=1;i<count-n;i++)
    {
        temp1=temp1->next;
    }
    temp1->next = temp1->next->next;
    return head;
}