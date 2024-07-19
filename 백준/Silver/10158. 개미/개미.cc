#include <stdio.h>

int main(void) {
    int w, h, p, q;
    int t;

    // 입력 받기
    scanf("%d %d %d %d %d", &w, &h, &p, &q, &t);
    int t_x = p+t, t_y = q+t;   //t 시간 만큼 움직인 값을 변수에 저장
    int x = t_x/w, y = t_y/h;   //t 시간 만큼 움직인 값을 격자 크기 만큼 나누어 "벽에 튕긴 횟수" 를 변수에 저장.

    if(x%2==1){                 //x를 2로 나눈 나머지가 1이라면
        x=w-(t_x%w);            //위치를 조정하고 뒤집어 준다
    }else x=(t_x)%w;            //나누어 떨어진다면 뒤집지 않고 위치를 조정한다

    if(y%2==1){                 //위랑 똑같은 조건
        y=h-(t_y%h);
    }else y=(t_y)%h;

    printf("%d %d\n", x, y);    //출력
    return 0;
}
