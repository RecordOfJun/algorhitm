#include <stdio.h>
#include <stdlib.h>
int compare (const void *a, const void *b){
	const int *x = (const int *)a;
	const int *y = (const int *)b;
	return (*x-*y);
}
int main(void){

	int N;
	scanf("%d",&N);
	
	int* arr=(int*)malloc(sizeof(int)*N);
	
	for(int i=0;i<N;i++){
		scanf("%d",&arr[i]);
	}
	
	qsort(arr,N,sizeof(int),compare);
	
	for(int j=0;j<N;j++){
		printf("%d\n",arr[j]);
	}
}	