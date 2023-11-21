import numpy as np

def addAwgn(signal, SNR) :
    powerOfSignal = signal ** 2
    averagePower = np.mean(powerOfSignal)
    averagePowerDb = 10 * np.log10(averagePower)
    
    noiseAverageDb = averagePowerDb - SNR
    noiseAveragePower = 10 ** (noiseAverageDb / 10)
    # Generate an sample of white noise
    meanOfNoise = 0
    noise = np.random.normal(meanOfNoise, np.sqrt(noiseAveragePower), len(signal))
    # Noise up the original signal
    signalWithNoise = signal + noise
    return signalWithNoise
        
            
