# mistake
이 문제는 pw_buf 값과 pw_buf2 의 값을 비교하여 동일하면 flag 를 출력한다. 힌트는 "연산자 우선순위" 라고 한다.

"fd=open("./password",O_RDONLY,0400) < 0" 소스코드가 문제가 있는 부분이다.
"=" 보다 "<" 우선순위가 높다. open 의 리턴 값과 "0" 의 값을 비교한다. open 의 리턴 값은 성공 시 양수의 값을 반환하기 때문에 "false(0)" 가 된다. 즉, fd = 0 이 된다. 

고로, pw_buf 값과 pw_buf2 의 값 모두 조작이 가능하다.

```c
#include <stdio.h>
#include <fcntl.h>

#define PW_LEN 10
#define XORKEY 1

void xor(char* s, int len){
	int i;
	for(i=0; i<len; i++){
		s[i] ^= XORKEY;
	}
}

int main(int argc, char* argv[]){
	
	int fd;
	if(fd=open("./password",O_RDONLY,0400) < 0){
		printf("can't open password %d\n", fd);
		return 0;
	}

	printf("do not bruteforce...\n");

	char pw_buf[PW_LEN+1];
	int len;
	if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
		printf("read error\n");
		close(fd);
		return 0;		
	}

	printf("pw_buf = %s\n", pw_buf);

	char pw_buf2[PW_LEN+1];
	printf("input password : ");
	scanf("%10s", pw_buf2);

	// xor your input
	xor(pw_buf2, 10);

	printf("pw_buf = %s\n", pw_buf);
	printf("pw_buf2 = %s\n", pw_buf2);

	if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
		printf("Password OK\n");
		system("/bin/cat flag\n");
	}
	else{
		printf("Wrong Password\n");
	}

	close(fd);
	return 0;
}
```