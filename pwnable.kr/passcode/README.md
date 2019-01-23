# passcode

이 문제는 passcode1 과 passcode2 값을 각각의 조건에 만족시키면 flag 를 출력한다. <소스코드 참조>

&nbsp;

처음 welcome() 함수에서 100byte 만큼 입력받은 후, login() 함수에서 passcode1 의 주소에 값을 입력받는다.

일반적으로 유효한 주소가 아닌 값이 저장되어 있기에 "Segmentation fault" 를 출력하며 종료된다. 

&nbsp;

해결 방법은 이 passcode1 에 저장된 값을 유효한 주소로 만들어주면 된다. 아래의 스택 구조를 참고하자.

welcome() 함수에서 입력받는 name 변수의 100 byte 중 마지막 4 byte 는 passcode1 의 값이다. 이 passcode1 의 값을 fflush() 의 got 주소를 저장한 후, passcode1 을 입력받을 때, system() 가 실행되는 주소를 입력해주면 플래그를 출력하게 될 것이다.

welcome() stack : | 96 byte | 4 byte (passcode1) |

&nbsp;

```c
#include <stdio.h>
#include <stdlib.h>

void login(){
        int passcode1;
        int passcode2;

        printf("enter passcode1 : ");
        scanf("%d", passcode1);
        fflush(stdin);

        // ha! mommy told me that 32bit is vulnerable to bruteforcing :)
        printf("enter passcode2 : ");
        scanf("%d", passcode2);

        printf("checking...\n");
        if(passcode1==338150 && passcode2==13371337){
                printf("Login OK!\n");
                system("/bin/cat flag");
        }
        else{
                printf("Login Failed!\n");
                exit(0);
        }
}

void welcome(){
        char name[100];
        printf("enter you name : ");
        scanf("%100s", name);
        printf("Welcome %s!\n", name);
}

int main(){
        printf("Toddler's Secure Login System 1.0 beta.\n");

        welcome();
        login();

        // something after login...
        printf("Now I can safely trust you that you have credential :)\n");
        return 0;
}
```

최종 페이로드는 다음과 같다.

* (perl -e 'print "\x90"x96, "\x48\x4a\xbb\xff", "134514147"') | ./passcode