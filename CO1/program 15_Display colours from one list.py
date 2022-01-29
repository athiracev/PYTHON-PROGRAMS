# printout all colors from color list 1 not contained in color list 2

color1=["yellow","red","green","blue"]
color2=["green","orange","violet"]
print([i for i in color1 if i not in color2])
