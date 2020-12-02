"""
In order to test the encoder and decoder together, we'll simulate a random signal being encoded and then decoded

The main steps are:
-generate a random signal
-encode it
-add noise to it
-decode it

"""
import Decoder
from Encoder import Encoder
import numpy as np

def generateRandomSignal(desired_length):
    """
    Create random binary signal with input length
    """
    #signal = np.random.randbytes(desired_length) # this only works with random 3.9
    signal = np.random.random((desired_length,)) #make random signal
    signal = np.where(signal > 0.5, 1, 0) #make binary
    #signal = str(signal).strip('[]')
    signal = ''.join(map(str, signal))
    return(signal)

def addNoise(encodedSignal):
    """
    takes in encoded signal and adds noise to it
    """
    noise = np.random.normal(0,1,len(encodedSignal)) #make normally distributed noise
    noise = np.where(noise > 0.5, 1, 0) #make binary
    noise = ''.join(map(str, noise))
    return(noise)

if __name__ == "__main__":
    sig = generateRandomSignal(100)
    enc_sig = Encoder(sig)
    noisy_sig = addNoise(sig)
    print("signal", sig)
    print("noisy signal", noisy_sig)
