from pynput import keyboard

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='t')},
    {keyboard.Key.shift, keyboard.KeyCode(char='T')}
]

END_COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.f4}
]

current = set()

def increase_count():
    global count
    count += 1

def get_count():
    global count
    return count

def execute():
    increase_count()
    k = get_count()
    print('Pressed %d times' % k)

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
    elif any([key in COMBO for COMBO in END_COMBINATIONS]):
        current.add(key)
        if any([all(k in current for k in COMBO) for COMBO in END_COMBINATIONS]):
            listener.stop()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

count = 0

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()