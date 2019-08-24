#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
	FILE *in = fopen(argv[1],"r");
	FILE *out = fopen(argv[2],"w");
	char str[100];
	fgets(str,100,in);
	while (strstr(str,argv[3]) == NULL){
		fgets(str,100,in);}
	fgets(str,100,in);
	while (strstr(str,"*EL")==NULL){
		fprintf(out,"%s",str);
		fgets(str,100,in);
	}
	fclose(in);
	fclose(out);
	return 0;
}