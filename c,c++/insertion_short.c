#include <stdio.h>

void scan_Arry(int a[], int n) {
    printf("Enter the elements of the array: \n"); 
    for(int i=0; i<n; i++)
        scanf("%d",&a[i]);
}

void print_Arry(int a[], int n) {
    printf("Array elements are: \n"); 
    for(int i=0; i<n; i++)
        printf("%d ",a[i]);
    printf("\n");
}

int main() {
    int a[100];
    int n, min;
    printf("Enter the size of the array: ");  
    scanf("%d",&n);
    scan_Arry(a, n);

    for(int i=1; i<n; i++) {
        min  = a[i];
        int j = i-1;
        while(j >= 0 && a[j] >min) {
            a[j+1] = a[j];
            j = j-1;
        }
        a[j+1] = min;
    }

    print_Arry(a, n);
    return 0;
}