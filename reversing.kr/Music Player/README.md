
# Music Player
이 문제는 1분 듣기만 허용된 뮤직 플레이어를 우회하는 문제이다. (1분 이상)

&nbsp;
# 풀이

음악을 플레이하고 1분이 지나면, "1분 미리듣기만 가능합니다." 라는 메시지 박스를 출력한다.

메시지 박스를 호출하는 rtcMsgbox() 함수에 브레이크포인트를 걸면 비교를 통한 분기 구문이 있다고 가정하여 접근하였다.

"1분 미리듣기만 가능합니다." 를 출력하는 rtcMsgBox 함수 위쪽을 보면, 

``CMP EAX, 0EA60	// EA60(60000) = 60초``

와 같이 60초 비교 구문이 있다. 0xEA60 값을 좀 더 큰 값으로 수정하면 1분 제한을 우회할 수 있다. < 1.png 참조 >

![텍스트](1.png)

&nbsp;

정상적으로 FLAG 를 출력할거라 생각했지만, "Run-time error~" 라는 에러를 출력한다.

Call stack 을 통해 쫓아가보니 0x4046B9 함수를 호출하면서 예외가 발생한 것으로 보여진다. 

JGE -> JMP 로 수정하여 0x4046B9 함수의 호출을 무시하니 정상적으로 FLAG 를 출력한다. < 2.png 참조 >

![텍스트](2.png)

&nbsp;

FLAG : **LIstenCare**