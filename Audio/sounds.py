# Sounds from this file are found from freesound.org and soundbible.com

def effects(sound):
    import pygame
    pygame.mixer.init()

    action = ["monster", "+", "-", "*", "ow", "ugh", "stab", "thunder", "squeak", "roar", "zeus", "bridge", "victory", "drinking", "kick", "uhhuh", "jab", "maniaclaugh"]
    assoc_sound = ["monster-growl.wav", "bag.ogg", "swipe.wav", "doh6.wav",
                   "ow.wav", "ugh.wav", "knife-stab.wav", "thunderstrike.wav",
                    "squeak.wav", "roar.wav", "zeus.wav", "bridge.wav", 
                    "victory.wav", "drinking.wav", "kick.wav", "uhhuh.wav", "jab.wav", "maniaclaugh.wav"]

    if sound in action:
        index = 0
        for i in action:
            if i == sound:
                break
            else:
                index += 1
        soundbyte = "pygame.mixer.Sound('Audio/effects/" + assoc_sound[index] + "')"
        exec(soundbyte + '.play()')
    else:
        playing = "Audio/music/" + sound + ".wav"
        pygame.mixer.music.load(playing)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.3)

       