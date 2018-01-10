#/usr/bin/env bfi

push output
push find
push input
push init
while top:
    switch pop:
        case init:
            init heap
        case get:
            pop x
            pop y
            get at y x
        case set:
            pop value
            pop x
            pop y
            get at y x
        case input:
            for y in H:
                for x in W:
                    getchar
                    set y x c
        case find:
            for y in H:
                for x in W:
                    if get y x == 2:
                        sy = y
                        sx = x
                        break
            go sy sx 0
        case go:
            pop stage
            pop x
            pop y
            c = get y x
            if c == stage:
                increment stage
            if stage == 4:
                found
            else:
                for i in 4:
                    let ny
                    let nx
                    go ny nx stage
        case found:
            go heap
            increment
        case output:
            go heap
            print

symbols:
    exit 0
    pop 1
    nop 2
    get 3
    get2 4
    set 5
    swap 6
    found 7
    go 8
    go1 9
    go2 10
    init 11
    input 12
    find 13
    output 14

heap structure:
    first track:
        0 0 result f00 f01 f02   f017 f10 f11   f1717
    second track:
        empty

>> exit
++++++++++++++> output
++> stage = 2
++++++++> go
> i = 0
> value = 0
+++++++++++++> find
++++++++++++> input
+++++++++++> init
<[ switch
    >+<
    [-
        [-
            [-
                [-
                    [-
                        [-
                            [-
                                [-
                                    [-
                                        [-
                                            [-
                                                [-
                                                    [-
                                                        [-
                                                            [-
                                                            ]

                                                            >[-< output
#
go to heap
>
->+[->+]
move to stack
>>>>>[
    <
    -<+[-<+]
    <+>
    ->+[->+]
    >
-]<<<<<
go to stack
-<+[-<+]
<
put result in decimal
[>>>>++++++++++<<<<[->+>>+>-[<-]<[->>+<<<<[->>>+<<<]>]<<]>+[-<+>]>>>[-]>[-<<<<+>>>>]<<<<]<[>++++++[<++++++++>-]<-.[-]<]
                                                            >]<
                                                        ]

                                                        >[-< cont i value find /
if value /= 2
+<--[++[-]
    <[>+>+<<-]>+[<+>-] cont i' *0 i'
    +++++++++++++>> find
    +++> get
]>[- else
    cont i 0 *0
    <<[>+<-]
    <[>+<-]
    >>[<<+>>-] i cont *0
    >
]<
                                                        >]<
                                                    ]

                                                    >[-< input /
go to heap
->+[->+]
mark
->
>>>>
18 sentinels
+++++ +++++ +++++ +++[[>>+<<-]>>-]
>>
read data
>>,----------[
    ++++++++++
    >>+++++ +++++ +++++[[>>+<<-],>>-]
    <++++++[
        <[<<]
        >>[-------->>]
        <
    -]>
    >> 2 sentinels
>>,----------]
go to mark
>+[-<+]
go to stack
-<+[-<+]
                                                    >]<
                                                ]

                                                >[-< init
stack size
+++++++[>+++++++[>+++++++<-]<-] 7**3
mark heap header
->>[[>>>>>>>+<<<<<<<-]>>>>>>>-]-
go to stack
<+[-<+]
                                                >]<
                                            ]

                                            >[-< nop
                                            >]<
                                        ]

                                        >[-< stage 0 0 i value go1 /
if value
<[
    stage 0 0 i *value
    <<<<[>+>+<<-] *0 stage stage i value
    >>>>[<<<-<+>>>>-] value delta stage i *0
    <<+<[>-<+++++[-]] value *0 stage' i
    >[>>+>+<<<-] value 0 *0 i stage' stage'
    +>>-----[[+]
        value 0 1 i *0 stage'
        >[<+>>>+>>>+>>>+<<<<<<<<-] value 0 1 i stage' *0 0 stage' 0 0 stage' 0 0 stage' 0 0
        ++++++++[>+>>>+>>>+>>>+<<<<<<<<<<-] value 0 1 i stage' *0 go stage' 0 go stage' 0 go stage' 0 go
        <<[<<+>>>>+>>>+>>>+>>>+<<<<<<<<<<<-] value i 1 *0 stage' i go stage' i go stage' i go stage' i go
        ++ nop
        <-+++++ set
        >>> value i set nop stage' *i go stage' i go stage' i go stage' i go
        ->>>+>>>------------------>>>++++++++++++++++++
        >>>> go 0 0 *0
    ]
    <<[
         value 0 *1 i 0 stage'
         -+++++ set
         >[<<+>>-] value i set *0 0 stage'
         ++> nop
         ++> nop
         ++> found
    ]
>>>>]<[-]<<<[-]
                                        >]<
                                    ]

                                    >[-< stage i go / stage 0 0 i go1 0 i swap
#
<[>>+>>>+<<<<<-]
>>>+++++++++ go1
>>> ++++++ swap
>
                                    >]<
                                ]

                                >[-< found
#
go to heap
->+[->+]
increment result
>>>>>+<<<<<
go to stack
-<+[-<+]
                                >]<
                            ]

                            >[-< cont value i swap / value' cont
move i to heap
<[>
    ->+[->+]
    >>+<<
    -<+[-<+]
<-]
move value to heap
<[>
    ->+[->+]
    >>>+<<<
    -<+[-<+]   _1 0 i value 0 result 0 a 0 a 0
<-]
move cont to top
<[>+<-]
go to heap
>>->+[->+]  0 cont _1
lookup
-
>>++[[>>+<<-]>>-]
move the old value
>[<
    -<<+[-<<+]
    >+<
    ->>+[->>+]
>-]<
move the new value
-<<+[-<<+]
>>>[<<<
    ->>+[->>+]
    >+<
    -<<+[-<<+]
>>>-]<<<
remove mark
->>+[->>+]
<<+[-<<+]
move the old value to stack
>[<
    -<+[-<+]
    <<+>>
    ->+[->+]
>-]<
go to stack
-<+[-<+]
                            >]<
                        ]

                        >[-< value i set /
>++++++< swap
<[>+<-]
<[>+<-]
+ pop
>>>>
                        >]<
                    ]

                    >[-< cont i value get2 / value cont pop value i swap
>>++++++ swap
<<<<[>>>+<<<-] i
<[>+<-] cont
>>[<<+>>>+<-] value
+ pop
>>>>
                    >]<
                ]

                >[-< cont i get / cont i get2 0 i swap
<[>+<-]>[<+>>>+<<-] share i
++++ get2
>>>++++++> swap
                >]<
            ]

            >[-< nop /
            >]<
        ]

        >[-< value pop /
            <[-]
        >]<
    ]

    >[-< exit
        >
    >]<
<]
