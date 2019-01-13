# fd
이 문제는 사용자로부터 길이가 20인 문자열을 입력받는다. check_password() 함수에서는 이 문자열을 정수형 타입의 포인터로 캐스팅하여 저장한다. 즉, 입력받은 문자열이 4byte 단위로 정수 값으로 변환되어 저장이되는데, 4byte 단위로 총 5개(20 byte)의 값을 더했을 때 "0x21DD09EC" 값이라면 플래그를 출력한다. <소스코드 참조>

0x21DD09EC / 5 = 0x6C5CEC8 이다. 0x6C5CEC8 을 5번 더하면 0x21DD09E8 이 되어 값이 맞지 않다. 
따라서, 16 byte 문자열은 0x6C5CEC8(4 byte)로 보내고, 나머지 4 byte 문자열을 "0x6C5CECC" 로 보내면, 문제에서 요구하는 0x21DD09EC 값으로 설정할 수 있다.

```c
#include <stdio.h>
#include <string.h>
unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]){
        if(argc<2){
                printf("usage : %s [passcode]\n", argv[0]);
                return 0;
        }
        if(strlen(argv[1]) != 20){
                printf("passcode length should be 20 bytes\n");
                return 0;
        }
		
        if(hashcode == check_password( argv[1] )){
                system("/bin/cat flag");
                return 0;
        }
		else
                printf("wrong passcode.\n");
        return 0;

```

최종 페이로드는 아래와 같다.

* ./col `perl -e 'print "\xc8\xce\xc5\x06"x4, "\xcc\xce\xc5\x06"'`