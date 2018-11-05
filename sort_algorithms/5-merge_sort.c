// https://codereview.stackexchange.com/questions/69289/merge-sort-using-sentinels
#include<stdio.h>
#include<stdlib.h>
#include<limits.h>

void merge(int a[], int p, int q, int r)
{
    int n1,n2;
    int i,j,k;
    int *l,*m;

    n1 = q - p + 1;
    n2 = r - q;
    l = (int*)malloc(sizeof(int)*(n1+1));
    m = (int*)malloc(sizeof(int)*(n2+1));

    for(i=0; i<n1; i++)
        l[i] = a[p+i];
    for(j=0; j<n2; j++)
            m[j] = a[q+j+1];
    l[i] = INT_MAX;
    m[j] = INT_MAX;

    i = j = 0;
    for(k=p; k<r+1; k++)
    {
        if(l[i] <= m[j])
        {
            a[k] = l[i];
            i++;
        }

        else
        {
            a[k] = m[j];
            j++;
        }

    }
    free(l);
    free(m);
}

void merge_sort(int a[],int p, int r)
{
    int q;

    if(p<r)
    {
        q = p + (r-p)/2;
        merge_sort(a,p,q);
        merge_sort(a,q+1,r);
        merge(a,p,q,r);
    }
}
int main()
{
    int *num,n;
    int i;

    printf("Enter number of digits:");
    scanf("%d",&n);
    num = (int*)malloc(sizeof(int)*n);
    printf("Enter numbers:");   
    for(i=0 ; i<n; i++)
    {
        scanf("%d",&num[i]);
    }
    merge_sort(num,0,n-1);
    printf("Sorted array:\n");
    for(i=0; i<n; i++)
        printf("%d ",num[i]);
    free(num);
    return 0;
}