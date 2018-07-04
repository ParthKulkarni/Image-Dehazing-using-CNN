import numpy;

def estimate(imgar, jdark, px=1e-3):
       
    #reshape both matrix to get it in 1-D array shape
    imgavec = numpy.resize(imgar, (imgar.shape[0]*imgar.shape[1], imgar.shape[2]))
    jdarkvec = numpy.reshape(jdark, jdark.size)
    
    #the number of pixels to be considered
    numpx = numpy.int(jdark.size * px)
    
    #index sort the jdark channel in descending order
    isjd = numpy.argsort(-jdarkvec)

    asum = numpy.array([0.0,0.0,0.0])
    for i in range(0, numpx):
        asum[:] += imgavec[isjd[i], :]
  
    A = numpy.array([0.0,0.0,0.0])
    A[:] = asum[:]/numpx

    #returns the calculated airlight A    
    return A
    
