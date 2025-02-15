from neopixel import NeoPixel
from machine import Pin, PWM
import random

from buzzer_music import music
from time import sleep
 
# Create a NeoPixel object
np = NeoPixel(Pin(21), 1)
buzzer = PWM(Pin(9))

song = '0 D#5 4 25;2 G#5 1 25;4 G#5 1 25;6 F5 1 25;7 D#5 1 25;8 C5 1 25;9 G#4 1 25;10 D#5 1 25;11 C5 1 25;12 F5 1 25;13 D#5 1 25;14 D#5 1 25;15 C5 1 25;16 A#4 1 25;17 G#4 1 25;20 G#4 1 25;21 A#4 1 25;22 C5 1 25;23 D#5 1 25;24 F5 1 25;25 D#5 1 25;31 D#5 1 25;33 D#5 1 25;32 F5 1 25;38 F5 1 25;39 D#5 1 25;40 C5 1 25;41 G#4 1 25;43 D#5 1 25;42 D#5 1 25;44 F5 1 25;45 F5 1 25;46 D#5 1 25;47 C5 1 25;48 A#4 1 25;49 G#4 1 25;50 D#5 1 25;52 D#5 1 25;53 D#5 1 25;54 G5 1 25;55 A#5 1 25;58 D#5 1 25;56 G5 1 25;26 G#5 1 25;34 G#5 1 25;36 G#5 1 25;63 D#5 1 25;65 F5 1 25;64 F5 1 25;66 G#5 1 25;68 G#5 1 25;70 G#5 1 25;72 G#5 1 25;74 G#5 1 25;77 F5 1 25;78 D#5 1 25;79 C5 1 25;81 G#4 1 25;76 G#5 1 25;80 A#4 1 25;82 C#5 1 25;84 C#5 1 25;86 C#5 1 25;88 C#5 1 25;90 E5 1 25;92 G#5 1 25;93 A#5 1 25;94 B5 1 25;95 G#5 1 25;98 C6 1 25;99 B5 1 25;100 C6 1 25;101 B5 1 25;102 C6 1 25;103 D#6 1 25;105 C6 1 25;106 D#6 1 25;107 C6 1 25;109 G#5 1 25;112 D#5 1 25;114 B5 1 25;115 G#5 1 25;116 F5 1 25;118 A#5 1 25;120 G#5 1 25;128 D#5 4 25;130 G#5 1 25;132 G#5 1 25;134 F5 1 25;135 D#5 1 25;136 C5 1 25;137 G#4 1 25;138 D#5 1 25;139 C5 1 25;140 F5 1 25;141 D#5 1 25;142 D#5 1 25;143 C5 1 25;144 A#4 1 25;145 G#4 1 25;148 G#4 1 25;149 A#4 1 25;150 C5 1 25;151 D#5 1 25;152 F5 1 25;153 D#5 1 25;159 D#5 1 25;161 D#5 1 25;160 F5 1 25;166 F5 1 25;167 D#5 1 25;168 C5 1 25;169 G#4 1 25;171 D#5 1 25;170 D#5 1 25;172 F5 1 25;173 F5 1 25;174 D#5 1 25;175 C5 1 25;176 A#4 1 25;177 G#4 1 25;178 D#5 1 25;180 D#5 1 25;181 D#5 1 25;182 G5 1 25;183 A#5 1 25;186 D#5 1 25;184 G5 1 25;154 G#5 1 25;162 G#5 1 25;164 G#5 1 25;191 D#5 1 25;193 F5 1 25;192 F5 1 25;194 G#5 1 25;196 G#5 1 25;198 G#5 1 25;200 G#5 1 25;202 G#5 1 25;205 F5 1 25;206 D#5 1 25;207 C5 1 25;209 G#4 1 25;204 G#5 1 25;208 A#4 1 25;210 C#5 1 25;212 C#5 1 25;214 C#5 1 25;216 C#5 1 25;218 E5 1 25;220 G#5 1 25;221 A#5 1 25;222 B5 1 25;223 G#5 1 25;226 C6 1 25;227 B5 1 25;228 C6 1 25;229 B5 1 25;230 C6 1 25;231 D#6 1 25;233 C6 1 25;234 D#6 1 25;235 C6 1 25;237 G#5 1 25;240 D#5 1 25;242 B5 1 25;243 G#5 1 25;244 F5 1 25;246 A#5 1 25;248 G#5 1 25;155 G#6 1 25;158 G#6 1 25;154 G#6 1 25;157 G#6 1 25'
#song = '0 D#5 4 0;4 G#5 0.5 0;6 G#5 1.5 0;8 F5 0.5 0;9 D#5 0.5 0;10 C5 0.5 0;11 A#4 0.5 0;12 D#5 0.5 0;13 C5 0.5 0;14 F5 1 0;15 D#5 0.5 0;16 D#5 0.5 0;17 C5 0.5 0;18 A#4 0.5 0;19 G#4 0.5 0;21 G#4 0.5 0;22 A#4 0.5 0;23 C5 0.5 0;24 D#5 0.5 0;26 D#5 0.5 0;25 F5 0.5 0;27 G#5 0.5 0;31 D#5 0.5 0;32 F5 0.5 0;33 D#5 0.5 0;34 G#5 0.5 0;36 G#5 1 0;37.5 F5 0.5 0;39.5 C5 0.5 0;38.5 D#5 0.5 0;41.5 D#5 0.5 0;42.5 D#5 0.5 0;43.5 F5 0.5 0;44.5 F5 0.5 0;45.5 D#5 0.5 0;40.5 A#4 0.5 0;54 G5 1 0;46.5 C5 0.5 0;47.5 A#4 0.5 0;48.5 D#5 0.5 0;50 D#5 0.5 0;51 D#5 0.5 0;52 G5 0.5 0;53 A#5 0.5 0;55.5 D#5 0.5 0;60 D#5 0.5 0;61 F5 0.5 0;62 F5 0.5 0;63 G#5 1 0;65 G#5 1 0;67 G#5 1 0;71 G#5 1 0;69 G#5 1 0;73 G#5 1.5 0;75 F5 0.5 0;76 D#5 0.5 0;77 C5 0.5 0;78 G#4 0.5 0;79 C#5 1 0;81 C#5 1 0;83 C#5 1 0;85 C#5 1 0;86.5 F5 1 0;88 G#5 0.5 0;89 A#5 0.5 0;90 B5 0.5 0;91 G#5 0.5 0;94 B5 0.5 0;93 C6 0.5 0;95 C6 0.5 0;96 B5 0.5 0;97 C6 0.5 0;98.5 D#6 2 0;101 C6 0.5 0;102 D#6 1 0;103.5 C6 0.5 0;104.5 G#5 1 0;105.5 G5 0.5 0;105.75 F5 0.5 0;106 E5 0.5 0;106.25 D5 0.5 0;106.75 C5 0.5 0;107 B4 0.5 0;107.25 A4 0.5 0;108.5 C6 0.5 0;109.5 G#5 0.5 0;111 F5 0.5 0;112 A#5 1 0;113 G#5 0.5 0;115 G#5 0.5 0'
#song = '0 G4 4 0;4 C5 8 0;12 D5 6 0;18 D#5 1 0;19 F5 1 0;20 D#5 8 0;28 G4 6 0;34 G4 2 0;36 C5 6 0;42 D5 2 0;44 D#5 2 0;46 G4 2 0;48 D#5 1 0;49.33000183105469 C5 1 0;50.66999816894531 G5 1 0;52 F5 12 0;64 G4 4 0;68 C5 6 0;74 D5 2 0;76 D#5 3 0;79 G4 1 0;80 G5 3 0;83 D#5 1 0;92 C5 4 0;96 D#5 1 0;97.33000183105469 D5 1 0;98.66999816894531 C5 1 0;100 G5 5 0;105.33000183105469 D#5 1 0;106.66999816894531 C5 1 0;108 G4 4 0;112 G4 3 0;115 G4 1 0;116 C5 12 0;128 G4 4 0;132 C5 8 0;140 D5 6 0;146 D#5 1 0;147 F5 1 0;148 D#5 8 0;156 G4 6 0;162 G4 2 0;164 C5 6 0;170 D5 2 0;172 D#5 2 0;174 G4 2 0;176 D#5 1 0;177.3300018310547 C5 1 0;178.6699981689453 G5 1 0;180 F5 12 0;192 G4 4 0;196 C5 6 0;202 D5 2 0;204 D#5 3 0;207 G4 1 0;208 G5 3 0;211 D#5 1 0;212 C6 8 0;212 D#5 8 0;220 C5 4 0;224 D#5 1 0;225.3300018310547 D5 1 0;226.6699981689453 C5 1 0;228 G5 5 0;233.3300018310547 D#5 1 0;234.6699981689453 C5 1 0;236 G4 4 0;240 G4 3 0;243 G4 1 0;244 C5 12 0;256 C5 4 0;260 C5 8 0;268 D5 4 0;272 D5 1 0;273.3299865722656 D#5 1 0;274.6700134277344 F5 1 0;277.3299865722656 D5 1 0;278.6700134277344 C5 1 0;280 D5 8 0;288 A#5 3 0;291 A#5 1 0;292 G5 4 0;296 C5 6 0;302 G#5 2 0;304 G5 1 0;305.3299865722656 D#5 1 0;306.6700134277344 C5 1 0;308 F5 12 0;320 G#4 4 0;324 F5 8 0;332 G5 5 0;337.3299865722656 G#5 1 0;338.6700134277344 A#5 1 0;340 G#5 1 0;341.3299865722656 F5 1 0;342.6700134277344 C6 1 0;344 G5 8 0;352 C5 1 0;353.3299865722656 C#5 1 0;354.6700134277344 D#5 1 0;356 F5 1 0;357.3299865722656 G5 1 0;358.6700134277344 G#5 1 0;360 G#5 5 0;365.3299865722656 A#4 1 0;366.6700134277344 C5 1 0;368 C#5 1 0;369.3299865722656 G5 1 0;370.6700134277344 F5 1 0;372 G#5 1 0;373.3299865722656 A#5 1 0;374.6700134277344 C6 1 0;376 C6 5 0;381.3299865722656 C5 1 0;382.6700134277344 D5 1 0;384 G#5 1 0;384 D5 1 0;385.3299865722656 G5 1 0;386.6700134277344 F5 1 0;388 A#5 1 0;389.3299865722656 C6 1 0;390.6700134277344 C#6 1 0;392 C#6 8 0;400 A#5 4 0;404 G5 12 0;416 G5 4 0;420 C6 8 0;428 D6 6 0;434 D#6 1 0;435 F6 1 0;436 D#6 8 0;444 G5 6 0;450 G5 2 0;452 C6 6 0;458 D6 2 0;460 D#6 2 0;462 G5 2 0;464 D#6 1 0;465.3299865722656 G5 1 0;466.6700134277344 G6 1 0;468 F6 12 0;480 G5 4 0;484 C6 6 0;490 D6 2 0;492 D#6 3 0;495 G5 1 0;496 G6 3 0;499 D#6 1 0;500 C7 8 0;508 C6 4 0;512 D#6 1 0;513.3300170898438 D6 1 0;514.6699829101562 C6 1 0;516 G6 5 0;521.3300170898438 D#6 1 0;522.6699829101562 C6 1 0;524 G5 16 0;540 G5 6 0;546 G5 2 0;564 C7 16 0;548 C6 32 0;84 C6 8 0;276 D#5 1 0'
mySong = music(song, pins=[Pin(9)])


def play_tone(frequency):
    buzzer.duty_u16(3000)
    buzzer.freq(frequency)
    
def be_quiet():
    buzzer.duty_u16(0)
 
def set_color(color):
    np[0] = color
    np.write()

def hsl_to_rgb(h, s, l):
    r, g, b = l, l, l
    if s != 0:
        def hue_to_rgb(p, q, t):
            if t < 0:
                t += 1
            if t > 1:
                t -= 1
            if t < 1/6:
                return p + (q - p) * 6 * t
            if t < 1/2:
                return q
            if t < 2/3:
                return p + (q - p) * (2/3 - t) * 6
            return p

        q = l * (1 + s) if l < 0.5 else l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1/3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1/3)

    return int(r * 255), int(g * 255), int(b * 255)

def int_to_rainbow_rgb(value):
    min_input, max_input = 50, 3000

    if not (min_input <= value <= max_input):
        raise ValueError(f"Value must be between {min_input} and {max_input}")
    
    normalized_hue = (value - min_input) / (max_input - min_input)
    
    return hsl_to_rgb(normalized_hue, 1.0, 0.5)

while True:
    #frequency_value = random.randint(50,600)
    #for frequency_value in range(50, 3000, 100):
    #set_color(int_to_rainbow_rgb(frequency_value))
    #play_tone(frequency_value)
    #sleep(0.2)
    #be_quiet()
    #sleep(0.20)
    mySong.tick()
    sleep(0.04)
    
