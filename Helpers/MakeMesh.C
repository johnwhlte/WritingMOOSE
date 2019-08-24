#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
	FILE *in = fopen(argv[1],"r");
	FILE *blocks = fopen(argv[3],"r");
	FILE *out = fopen(argv[4],"w");
	char str[100];
	fgets(str,100,in);
	while (strstr(str,argv[2]) == NULL){
		fprintf(out,"%s",str);
		fgets(str,100,in);
	}
	fgets(str,100,blocks);
	while (!feof(blocks)){
		fprintf(out,"%s",str);
		fgets(str,100,blocks);
	}
	while (strstr(str,"*EL")==NULL){
		fgets(str,100,in);
	}
	while(!feof(in)){
		fprintf(out,"%s",str);
		fgets(str,100,in);
	}
fclose(in);
fclose(out);
fclose(blocks);
return 0;
}