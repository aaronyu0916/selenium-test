click("1492762960765.png")
if exists("1492765644092.png"):
    click(Pattern("1492763524293.png").exact().targetOffset(-395,170))
if exists("1492764500632.png",20):
    click(Pattern("1492764513498.png").exact())
    wait("1492758880659.png",60)
exists("1492758842924.png")
click("1492758866646.png")
while not Region(59,14,1151,782).exists(Pattern("1492760677434.png").exact()):
    #click(Pattern("1492760648906.png").similar(0.80))
    click(Pattern("1492763198895.png").similar(0.80).targetOffset(7,0))
if exists(Pattern("1492762644058.png").exact()):
    print ('ready to Spin')
    hover("1492765789195.png")
    #click("1492762725754.png")
    
    







