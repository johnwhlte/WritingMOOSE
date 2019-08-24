#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
	int elt;
	struct node *next;
} Node;
	
Node *addOrdered (Node *list, int c) {
	Node *newOne = (Node *) malloc ( sizeof(Node) );
	newOne->elt = c;
	newOne->next = NULL;

	if (list == NULL) return newOne;
	if (c < list->elt) {
		newOne->next = list;
		return newOne;
	}

	Node *current = list, *after = list->next;
	while (after!=NULL && after->elt < c) {
		current = after;
		after = after->next;
	}

	current->next = newOne;
	newOne->next = after;
	return list;
}
void printList(Node *list, FILE* fp) {
	while (list != NULL) {
		fprintf(fp,"%d 0.9 1.3\n", list->elt);
		list = list->next;
	}
	return;
}


int main(int argc, char* argv[]){
	FILE *in = fopen(argv[1],"r");
	FILE *out = fopen(argv[2],"w");
	Node *head = NULL;
	char str[10];
	while (!feof(in)){
		fscanf(in,"%s\n",str);
		if (strlen(str)==5){
		head=addOrdered(head,atoi(str));
		}
	}
	
	printList(head,out);
	fclose(in);
	fclose(out);
	return 0;

}