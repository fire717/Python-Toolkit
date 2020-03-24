def RGB2HSV(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240
    if mx == 0:
        s = 0
    else:
        s = m/mx
    v = mx
    return h, s, v

def RGB2HSL(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240

    l = (mx+mn)/2.0

    if mx == 0 or mx == mn:
        s = 0
    elif 0<l<0.5:
        s = (mx-mn)*1.0/(2*l)
    elif l>=0.5:
        s = (mx-mn)*1.0/(2-2*l)

    return h, s, l


def HSV2RGB(h,s,v):
    assert 0<=h<360
    assert 0<=s<=1
    assert 0<=v<=1
    c = v*s
    x = c*(1-abs((h/60)%2-1))
    m = v-c
    if h<60:
        r,g,b = c,x,0
    elif h<120:
        r,g,b = x,c,0
    elif h<180:
        r,g,b = 0,c,x
    elif h<240:
        r,g,b = 0,x,c
    elif h<300:
        r,g,b = x,0,c
    elif h<360:
        r,g,b = c,0,x

    r,g,b = (r+m)*255, (g+m)*255, (b+m)*255
    return r, g, b
