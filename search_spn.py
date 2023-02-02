def spn(toponym):
    lC = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    uC = toponym["boundedBy"]["Envelope"]["upperCorner"].split()
    width = abs(float(lC[0]) - float(uC[0])) / 2
    height = abs(float(lC[1]) - float(uC[1])) / 2
    a = [str(width), str(height)]
    return a
