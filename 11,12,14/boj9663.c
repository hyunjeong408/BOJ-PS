#include <stdio.h>
#include <stdlib.h>
int n;
int cnt = 0;
int cols[15] = {0, };

int isPossible(int lv){
    for (int i = 0; i<lv; i++){
        if (cols[i] == cols[lv]) return 0;//같은 열
        else if (abs(cols[i]-cols[lv]) == abs(i-lv)) return 0;//대각선
    }
    return 1;
}
void nQueen(int lv){
    if (lv == n){
        cnt++;
        return;
    }
    else{ //현재 lv에서
        for (int i = 0; i<n; i++){ //가능한 열 위치
            cols[lv] = i;
            if (isPossible(lv)) nQueen(lv+1);
                         }
        }
}                   
int main(){
    scanf("%d", &n);
    nQueen(0);
    printf("%d", cnt);
    return 0;
}