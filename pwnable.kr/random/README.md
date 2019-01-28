# random
이 문제는 사용자로부터 key 값을 입력받는다. key ^ random == 0xdeadbeef 라면 flag 를 출력한다. <코드 참조>

random 값은 0x6b8b4567 값이 고정으로 들어가 있다. 즉, 0x6b8b4567 xor 0xdeadbeef 값이 key 값이 된다.


```c
#include <stdio.h>

int main(){
        unsigned int random;
        random = rand();        // random value!

        unsigned int key=0;
        scanf("%d", &key);

        if( (key ^ random) == 0xdeadbeef ){
                printf("Good!\n");
                system("/bin/cat flag");
                return 0;
        }

        printf("Wrong, maybe you should try 2^32 cases.\n");
        return 0;
}
```