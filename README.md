### Audio Time Stretching

### OLA

The easiest time stretching algorithm I've ever seen yet without
changing the pitch is OLA, but as much as you change the speed you
spoil the quiality. The idea behind it is the next: you chop the
audio file into constant size chunks, let's say the chunk size is X,
first chunks would be 0-X, second X/2-1.5X, third X-2X and etc. Then
you take each chunk and put it into new file two times meaning the first
chunk you'll put on 0-X and the same chunk X/2-1.5X, second chunk
second X/2-1.5X and then the same chunk on X-2X and etc. You'll notice
that it's the same as we take chunks but here we put the same chunks
twice, also you'll notice that the ditstance between chunks is X/2,
it's just for the example, in reality it depends on the speed change.

Let's count how much will be the distance between chunks for any speed:
If you want to speed up the audio let's say two times it means that
it'll become twice as short, if you want to slow it down it'll become
twice as large,