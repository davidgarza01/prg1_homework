def decode_whale_speak(letter):
    space = ((letter) /8 len(letter))
    if( space ==letter):
        return space
    else:
        return decode_whale_speak(letter - space)
    
decode_whale_speak("Pizza")
