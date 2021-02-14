from pynput import keyboard

COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='t')},
    {keyboard.Key.shift, keyboard.KeyCode(char='T')}
]

END_COMBINATIONS = [
    {keyboard.Key.shift, keyboard.Key.f4}
]

current = set()

def execute():
    print('asd')

def end_program():
    listener.stop()

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
    elif any([key in COMBO for COMBO in END_COMBINATIONS]):
        current.add(key)
        if any([all(k in current for k in COMBO) for COMBO in END_COMBINATIONS]):
            end_program()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()