#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]){
	FILE *in = fopen(argv[1],"r");
	FILE *out = fopen(argv[2],"w");
	char str1[10],str2[10],str3[10];
	while(!feof(in)){
		fscanf(in,"%s %s %s",str1,str2,str3);	
		fprintf(out, "  [./%s_diff]\n",str1);
		fprintf(out, "    type=ExampleCoefDiffusion\n    variable=convected\n");
		fprintf(out,"    block = 'S%s_TRI3'\n",str1);
		fprintf(out,"    coef = %s\n",str2);
		fprintf(out, "  [../]\n  [./%s_conv]\n",str1);
		fprintf(out, "    type=ExampleConvection\n    variable=convected\n");
		fprintf(out,"    block = 'S%s_TRI3'\n",str1);
		fprintf(out,"    velocity = '%s 0 0'\n",str3);
		fprintf(out,"  [../]\n");
	}
fclose(in);
fclose(out);
return 0;
}
	
	