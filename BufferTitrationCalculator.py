import numpy as np
import sympy
from sympy import solve, symbols, Eq

TypeofSample=input("Is your sample strong or weak?")

if TypeofSample=="strong":
    VolumeofSample=float(input("What is the volume of your sample in Liters?"))
    MolarityofSample=float(input("What is the molarity of your sample?"))
    VolumeofTitrant=float(input("How much Titrant are you adding in Liters?"))
    MolarityofTitrant=float(input("What is the molarity of your Titrant?"))

    MolesofSample=VolumeofSample*MolarityofSample

    MolesofTitrant=VolumeofTitrant*MolarityofTitrant



if TypeofSample == "strong":
    Question1=input("Is your sample an acid or a base?")
    FinalMoles=abs(MolesofSample-MolesofTitrant)
    FinalVolume=VolumeofSample+VolumeofTitrant
    FinalMolarity=FinalMoles/FinalVolume
    if FinalMoles==0:
        print("You have reached the equivalence point, your pH is 7")
    if MolesofSample > MolesofTitrant:
        if Question1=="acid":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(-1*np.log(FinalMolarity)))
        if Question1=="base":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(14-(-1*np.log(FinalMolarity))))
    if MolesofSample < MolesofTitrant:
        if Question1=="acid":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(14-(-1*np.log(FinalMolarity))))
        if Question1=="base":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(-1*np.log(FinalMolarity)))




if TypeofSample == "weak":
    VolumeofSample=float(input("What is the volume of your sample in Liters?"))
    MolarityofSample=float(input("What is the molarity of your sample?"))
    SampleKA=float(input("What is the K value of your sample?"))
    VolumeofTitrant=float(input("How much Titrant are you adding in Liters?"))
    MolarityofTitrant=float(input("What is the molarity of your Titrant?"))

    
    acidconcentration=((SampleKA)-np.sqrt((SampleKA**2)-(4*(-1)*(MolarityofSample*SampleKA))))/(-2)
    pH=(-1)*np.log10(acidconcentration)
    print("The pH of your sample is originally", pH)

    MolesofSample=VolumeofSample*MolarityofSample

    MolesofTitrant=VolumeofTitrant*MolarityofTitrant

    if MolesofSample > MolesofTitrant:
        FinalMoles=MolesofSample-MolesofTitrant
        FinalVolume=VolumeofSample+VolumeofTitrant
        FinalMolarity=FinalMoles/FinalVolume

        if .11<MolesofTitrant/FinalMoles<10.01:

            pHWhenFinished=float((-1)*np.log(SampleKA)+np.log((MolesofTitrant/FinalVolume)/(FinalMolarity)))

            print("Congratulations!, the molarity of your existing sample is", round(FinalMolarity, 2), "and the pH is", round(pHWhenFinished, 2))

        newacidconcentration=((SampleKA)-np.sqrt((SampleKA**2)-(4*(-1)*(FinalMolarity*SampleKA))))/(-2)
        finalpH=(-1)*np.log10(newacidconcentration)
        print("Congratulations!, the molarity of your existing sample is", round(FinalMolarity, 2), "and the pH is", round(finalpH, 2))

    if MolesofSample < MolesofTitrant:
        FinalMoles=MolesofTitrant-MolesofSample
        FinalVolume=VolumeofSample+VolumeofTitrant
        FinalMolarity=FinalMoles/FinalVolume
        pHWhenFinished=float((-1)*np.log(FinalMolarity))

        print("Congratulations!, you went past the equivalence point and the pH of your sample is", round(pHWhenFinished, 2))




