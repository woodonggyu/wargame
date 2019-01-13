# fd
이 문제는 사용자로부터 입력 값을 받고, 이 값을 read() 함수의 파일 디스크립터 인자로 사용한다. 그리고 변수(buf)에 저장된 값이 "LETMEWIN" 이라면 flag 를 출력한다. <코드 참조>

변수(buf) 값에 "LETMEWIN" 문자열을 입력하기 위해서, 파일 디스크립터를 표준입력(0) 값이 되도록 하면 flag 를 얻을 수 있다. 

argv[1] - 0x1234(4660) = 1, 따라서 입력 값은 4661 이 되어야 한다.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
                printf("pass argv[1] a number\n");
                return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
                printf("good job :)\n");
                system("/bin/cat flag");
                exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;

}
```