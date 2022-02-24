from pydub import AudioSegment

# Hide data inside sound using binary
def generate(data, lower, higher):
    # Opening lower/higher sound
    lower = AudioSegment.from_file(lower, format="mp3")
    higher = AudioSegment.from_file(higher, format="mp3")
    # Converte data to binary
    binary = "".join([format(ord(x), "b") for x in data])
    # Generate the sound
    if binary[0] == "1":
        final_sound = higher
    else:
        final_sound = lower
    for digit in binary[1:]:
        if digit == "1":
            final_sound += higher
        else:
            final_sound += lower
    # Save the sound
    final_sound.export("challenge.mp3", format="mp3")


if __name__ == "__main__":
    generate("R2Lille{P3rF3cT_S0UnD}", lower="link.mp3", higher="navi.mp3")
