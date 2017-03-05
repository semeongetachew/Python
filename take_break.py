import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on " +time.ctime())
while(break_count < total_breaks):
    time.sleep(3600);
    webbrowser.open("https://www.youtube.com/watch?v=DR3sU4bJ2dc&index=1&list=PLT3x3TYKFhW0743elXZ6_-5bLHYC0xA_A");
    break_count = break_count + 1 
