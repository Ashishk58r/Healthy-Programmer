from pygame import mixer
from datetime import datetime
from time import time

def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    eyessecs = 10
    exsecs = 20

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            music_on_loop("Water.mp3", 'drank')
            init_water = time()
            log_now("Drank Water at ")

        if time() - init_eyes > eyessecs:
            print("Eyes Relaxing time. Enter 'doneeyes' to stop the alarm.")
            music_on_loop("Eyes.mp3", 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at ")

        if time() - init_exercise > exsecs:
            print("Exercising time. Enter 'donephy' to stop the alarm.")
            music_on_loop("Exercise.mp3", 'donephy')
            init_exercise = time()
            log_now("Done Exercise at ")

