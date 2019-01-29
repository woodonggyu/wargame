# leg

이 문제는 사용자로부터 입력받은 값이 "key1, key2, key3" 함수의 리턴 값과 동일하면 플래그를 출력한다. (소스코드 참조)

여기서 핵심은 key1 함수의 "mov r3, pc" 이다. 일반적으로 pc 는 eip 와 동일하게 다음 실행될 주소를 가리키는 것으로 설명한다.

PC 는 항상 fetched 된 인스트럭션을 가지고 있다. 즉, 32bit 기준 +8 의 위치를 가리키고 있다.

그 외에는 각각 printf 를 이용해 key2(), key3() 의 값을 출력하여 알 수 있다.


```c
#include <stdio.h>
#include <fcntl.h>
int key1(){
        asm("mov r3, pc\n");
}
int key2(){
        asm(
        "push   {r6}\n"
        "add    r6, pc, $1\n"
        "bx     r6\n"
        ".code   16\n"
        "mov    r3, pc\n"
        "add    r3, $0x4\n"
        "push   {r3}\n"
        "pop    {pc}\n"
        ".code  32\n"
        "pop    {r6}\n"
        );
}
int key3(){
        asm("mov r3, lr\n");
}
int main(){
        int key=0;
        printf("Daddy has very strong arm! : ");
        scanf("%d", &key);
        if( (key1()+key2()+key3()) == key ){
                printf("Congratz!\n");
                int fd = open("flag", O_RDONLY);
                char buf[100];
                int r = read(fd, buf, 100);
                write(0, buf, r);
        }
        else{
                printf("I have strong leg :P\n");
        }
        return 0;
}
```