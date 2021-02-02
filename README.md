# 내가 필요해서 만든 파이썬 로거
 English explaination is down below!

## 이게 뭐하는 거죠

파이썬 기록 장치입니다. 맨날 프로그램 짜다가 이런 거 필요한데, 필요한데 하다가 생각나는 기능들 최대한 모아서 만든 물건입니다. [logging](https://docs.python.org/3/howto/logging.html) 는 뭔가 쓰기 불편해서..

대충

- 타임스탬프, 지금까지 걸린 시간을 찍어서 화면에 표시합니다.
- 프린트 할 때 간단하게 글자색, 배경색을 입힐 수 있습니다.
- 옵션을 설정할 경우, 자동으로 `./logs` 디렉토리에 날짜-시간으로 로그 파일을 기록합니다.
- 출력 레벨을 설정할 수 있습니다.
- 파이썬의 `print()`의 대부분의 인자를 똑같이 쓸 수 있습니다 (sep는 지원 안 합니다)
- 설정을 바꾸거나 파일을 만들거나 하면, 메세지가 뜹니다 (설정으로 끌 수 있어요)

## 그래서 어떻게 쓰나요

위에 있는 `log.py`를 작업하시는 디렉토리에 넣고, `from log import Log`를 하신 뒤, `Log.Print("Message")`로 시작하시면 됩니다. ~~와!~~

### 파일 기록하기

`Log.Print()` 쓰기 전에, `Log.SetLogFile(True)`를 해 주세요.

그러면 `Log.Print()`로 쓰는 내용이 다 기록됩니다. 함수에 인자를 추가로 줘서 (예시: `Log.SetLogFile(True, "Mylog.log")`) 원하는 파일로 넣을 수 있습니다만은 이 경우 필요한 폴더는 만들어 주셔야 합니다.

만약에 아무것도 기록 안 된다면, 파일은 안 만들어져요 ㅠㅠ

### 다양한 기능들!

저는 타임스탬프 필요 없는데요 = `Log.Print("Message", current=False)`
    `Log.SetPrintCurrentTime(False)` 를 입력하면 그 뒤부터는 현재 타임스탬프는 안 찍힙니다.

저는 실행 시간도 필요 없는데요 = `Log.Print("Message", current=False, elapsed=False)`
    `Log.SetPrintCurrentTime(False)` , `Log.SetPrintElapsedTime(False)` 둘 다 해주면 계속 안 나와요

저는 밀리세컨드는 필요 없어요 = `Log.SetMSPrecision(0)` / 저는 더 자세히 보고 싶어요 `Log.SetMSPrecision(5)`

저는 **빨간 글씨**가 필요해요 = `Log.Print("Message", col='r')`

파란색 배경이 필요해요 = `Log.Print("Message", bg='b')`

다음 줄로 안 넘어갈래요 = `Log.Print("Message", end="")`
    다음에 표시되는 메세지에 current=False랑 elapsed=False 안 해주면 타임 스탬프 여러 번 찍힙니다

프린트 되는 레벨을 설정하고 싶어요 = `Log.Print("Message", level=2)`
     `Log.PrintLevel`보다 작은 레벨만 출력됩니다.  `Log.SetPrintLevel('value')` 값을 변경하는 것으로 설정할 수 있어요

이번에만 파일에 기록 안 할래요 = `Log.Print("Message", file=False)`

이번에 쓴 줄을 flush 할래요 = `Log.Print("Message", flush=True)`
    그래도 파일에는 기록됩니다. `file=False` 옵션을 주면 현명하게 사용 가능하겠죠

Logger가 말하는게 시끄러워요 (ㅠㅠ...) = `Log.SetMessages(False)`
    이러면 조용해 집니다... ㅠㅠ

### 색 코드

- 검정 = `b`, `black`
- 빨강 = `r`, `red`
- 초록 = `g`, `green`
- 노랑 = `y`, `yellow`
- 파랑 = `b`, `blue`
- 마젠타 = `m`, `magenta`
- 시안 = `c`, `cyan`
- 하양 = `w`, `white`
- 밝은 빨강 = `br`, `brightred`
- 밝은 초록 = `bg`, `brightgreen`
- 밝은 노랑 = `by`, `brightyellow`
- 밝은 파랑 = `bb`, `brightblue`
- 밝은 마젠타 = `bm`, `brightmagenta`
- 밝은 시안 = `bc`, `brightcyan`
- 밝은 하양 (???) = `bw`, `brightwhite`



# English version

## What this thing do?
Prints log as very effective way + automatically records file.

- Prints log with timestamps, elapsed time!
- Print with colors! and backgrounds!
- Print with specific levels!
- Automatically record to log file, on `./logs/` directory!
- Basic python's `print()` arguments works! (except for sep)
- Pops messages on doing something (You can turn it off, by the way...)

## How to use this thing?
Put this file to directory, just `from log import Log` to your desired file, and `Log.Print("Message")` to print. ~~such simple~~

### Record as file

You have to "Log.SetLogFile(True)" at first of the every other Log.Print() to record to file.

If you enter specific file location, then it will record on target. (You have to create directory by your own this case) "Log.SetLogFile(True, "Mylog.log")"

If there is nothing to record, then file will not created. ;_;

### More features!
I don't want current timestamp! = `Log.Print("Message", current=False)`
    Or `Log.SetPrintCurrentTime(False)` will do.

I don't want elapsed timestamp either! = `Log.Print("Message", current=False, elapsed=False)`
    Or `Log.SetPrintCurrentTime(False)` and `Log.SetPrintElapsedTime(False)` will do, again.

I don't need millisecond = `Log.SetMSPrecision(0)` / I want to look more `Log.SetMSPrecision(5)`

I want red message! = `Log.Print("Message", col='r')`

I want blue background! = `Log.Print("Message", bg='b')`

I don't want to go next line! = `Log.Print("Message", end="")`
    You have to set the timestamps to false if you don't want several timestamps on one line though...

I want to set level! = `Log.Print("Message", level=2)`
    Prints levels which is same or lower than `Log.PrintLevel`. this can be set by `Log.SetPrintLevel('value')`

I don't want to record to file THIS ONLY time! = `Log.Print("Message", file=False)`

I want to FLUSH this line! = `Log.Print("Message", flush=True)`
    Still it will record every line, so use wisely! or just add `file=False`

I want logger to be shut up (;_;) = `Log.SetMessages(False)`
    This makes logger to be quiet... ㅠㅠ



# Bug report

버그... 가 있을 수 있는데 있으면 말해주세요.

위에 issue 파 주시면 감사하겠습니다.

기능 추가도 필요하시면 말해 주세요. 제가 필요하면 추가함 히히