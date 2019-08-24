#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
	FILE *in = fopen(argv[1],"r");
	FILE *blocks = fopen(argv[2], "r");
	FILE *moreblocks = fopen(argv[3],"r");
	FILE *newin = fopen(argv[4],"w");
	char str[100];
	fgets(str,100,in);
	while (strstr(str,"[Kernels]") == NULL){
		fprintf(newin,"%s",str);
		fgets(str,100,in);
	}
	fprintf(newin,"[Kernels]\n");
	while (!feof(blocks)){
		fgets(str,100,blocks);
		fprintf(newin,"%s",str);
	}
	fclose(blocks);
	while (!feof(moreblocks)){
		fgets(str,100,moreblocks);
		fprintf(newin,"%s",str);
	}
	fclose(moreblocks);
	fprintf(newin,"[]\n");
	fgets(str,100,in);
	while (strstr(str,"[BCs]")== NULL){
		fgets(str,100,in);
	}
	while (!feof(in)){
		fprintf(newin,"%s",str);
		fgets(str,100,in);
	}
		

	fclose(newin);
	fclose(blocks);
return 0;
}

	
