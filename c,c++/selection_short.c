#include <stdio.h>

void scan_Arry(int a[], int n) {
    printf("Enter the elements of the array: \n"); 
    for(int i=0; i<n; i++){
        scanf("%d",&a[i]);
    }
}

void print_Arry(int a[], int n) {
    printf("Array elements are: \n"); 
    for(int i=0; i<n; i++){
        printf("%d ",a[i]);
    printf("\n");
    }
}

int main() {
    int a[100];
    int n, min_idx;
    printf("Enter the size of the array: ");  
    scanf("%d",&n);
    scan_Arry(a, n);

    for(int i=0; i<n-1; i++) {
        min_idx = i;
        for(int j=i+1; j<n; j++) {
            if(a[j] < a[min_idx])
                min_idx = j;
        }
        int temp = a[min_idx];
        a[min_idx] = a[i];
        a[i] = temp;
    }

    print_Arry(a, n);
    return 0;
}