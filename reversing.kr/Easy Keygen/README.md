
# Easy Keygen
이 문제는 사용자로부터 "Name" 및 "Serial" 값을 각각 입력받는다. 

문제 설명에서는 Serial 값이 "5B134977135E7D13" 일 때, Name 을 구하면 된다고 한다.

&nbsp;
# 풀이

아주 간단한 로직이다.

Serial 값을 2자리씩 끊으면, [5B, 13, 49, 77, 13, 5E, 7D, 13] 이 된다.



여기서 다시 3 등분을 하여 XOR 한다. 이 말인 즉슨,

* 0x5B xor 0x10	// ASCII "K"
* 0x13 xor 0x20	// ASCII "3"
* 0x49 xor 0x30	// ASCII "y"

&nbsp;
* 0x77 xor 0x10	// ASCII "g"
* 0x13 xor 0x20	// ASCII "3"

	&nbsp;
	.
	&nbsp;
	.

* 0x13 xor 0x20	// ASCII "3"

과 같다. <run.py 참조>


FLAG : **K3yg3nm3** 