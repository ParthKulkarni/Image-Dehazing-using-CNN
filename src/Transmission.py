import numpy;
import DarkChannel;


def estimate(imgar, A, w=0.95):
    """    
    Parameters
    -----------
    imgar:    an H*W RGB hazed image
    A:        the atmospheric light of imgar
    w:        the omega weight parameter, the amount of haze to be removed (default=0.95)

    Return
    -----------
    The transmission estimated in imgar, t (a H*W matrix).
    """ 
    #the normalized haze image
    nimg = numpy.zeros(imgar.shape)
    
    #calculate the normalized haze image 
    for c in range(0, imgar.shape[2]):
        nimg[:,:,c] = imgar[:,:,c]/A[c]
    
    #estimate the dark channel of the normalized haze image
    njdark = DarkChannel.estimate(nimg)
    
    #calculates the transmisson t
    t = 1-w*njdark+0.25
    
    return t
