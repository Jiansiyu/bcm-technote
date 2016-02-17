#!/usr/bin/env python
import os
from beampackage import bcmconst

const=bcmconst()
row={}
row["left"]=[1,2,3,4,5,6,7,8,9,10,22,23,24,26,27,29,30,32,33,35,36,38,39,41,42,44,45]
row["right"]=[1,2,3,4,11,12,13,14,15,16,47,48,49,51,52,54,55,57,58,60,61,63,64,66,67,69,70]
row["third"]=[1,2,3,4,17,18,19,20,72,73,74,76,77,79,80,82,83]
cols=[[0,2,3,4,5,6],[0,7,8,9,10,11],[0,12,13,14,15]]

texfile=open("table.tex","w")
texfile.write("\\begin{landscape}\n")
for arm in ["left","right","third"]:
    for col in cols:
        texfile.write("\\begin{table}\n")
        texfile.write("\\begin{tabular}{%s|}\n"%"".join(["|c"]*(len(col)+1)))
        for r in row[arm]:
            texfile.write("\\hline\n")
            content=[]
            for c in col:
                v=const.values[r-1][c]
                if "need to check" in v:
                    v="not avail"
                if "use" in v:
                    v=""
                content.append(v)
            texfile.write(" & ".join(content))
            texfile.write("\\tabularnewline\n")
        texfile.write("\\hline\n")
        texfile.write("\\end{tabular}\n")
        texfile.write("\\protect\\caption{BCM calibration constant for %s arm}\n"%(arm))
        texfile.write("\\end{table}\n")
texfile.write("\\end{landscape}\n")
texfile.close()