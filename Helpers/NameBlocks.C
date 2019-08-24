#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
	int elt;
	char str[100];
	struct node *next;
} Node;
	
Node *addOrdered (Node *list, int c, char string[100]) {
	Node *newOne = (Node *) malloc ( sizeof(Node) );
	newOne->elt = c;
	strcpy(newOne->str,string);
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

void printList(Node *list, FILE*fp) {
	while (list != NULL) {
		fprintf(fp,"*ELEMENT, type=CPS3, ELSET=S%d\n",list->elt);
		fprintf(fp,"%s", list->str);
		list = list->next;
	}
	return;
}


int main(int argc, char* argv[]){
	FILE *in = fopen(argv[1],"r");
	FILE *out = fopen(argv[2],"w");
	Node *head = NULL;
	char gotstr[100];
	char str[10];
	fgets(gotstr,100,in);
	while(!feof(in)){
		sscanf(gotstr,"%s",str);
		head = addOrdered(head,atoi(str),gotstr);
		fgets(gotstr,100,in);
	}
	printList(head,out);
	fclose(in);
	
	return 0;

}

