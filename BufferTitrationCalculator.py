import numpy as np

TypeofSample=input("Is your sample strong or weak?")

if TypeofSample=="strong":
    VolumeofSample=float(input("What is the volume of your sample?"))
    MolarityofSample=float(input("What is the molarity of your sample?"))
    SampleKA=float(input("What is the K value of your sample?"))
    VolumeofTitrant=float(input("How much Titrant are you adding?"))
    MolarityofTitrant=float(input("What is the molarity of your Titrant?"))

    MolesofSample=VolumeofSample*MolarityofSample

    MolesofTitrant=VolumeofTitrant*MolarityofTitrant



if TypeofSample == "strong":
    Question1=input("Is your sample an acid or a base?")
    FinalMoles=MolesofSample-MolesofTitrant
    FinalVolume=VolumeofSample+VolumeofTitrant
    FinalMolarity=FinalMoles/FinalVolume
    if MolesofSample > MolesofTitrant:
        if Question1=="acid":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(-1*np.log(FinalMolarity)))
        if Question1=="base":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(-1*np.log((1.00*(10**-14))/FinalMolarity)))
    if MolesofSample < MolesofTitrant:
        if Question1=="acid":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(-1*np.log((1.00*(10**-14))/FinalMolarity)))
        if Question1=="base":
                print("Congratulations! You just completed a titration. The pH of your solution is", float(-1*np.log(FinalMolarity)))




if TypeofSample == "weak":
    VolumeofSample=input(float("What is the volume of your sample?"))
    MolarityofSample=input(float("What is the molarity of your sample?"))
    SampleKA=input(float("What is the K value of your sample?"))
    VolumeofTitrant=input(float("How much Titrant are you adding?"))
    MolarityofTitrant=input(float("What is the molarity of your Titrant?"))


    eq1=Eq((-1)*SampleKA+((x**2)/(MolarityofSample-x)))
    acidconcentration=int(solve(eq1, x))
    pH=(-1)*np.log(acidconcentration)
    print("The pH of your sample is originally", pH)

    MolesofSample=VolumeofSample*MolarityofSample

    MolesofTitrant=VolumeofTitrant*MolarityofTitrant

    if MolesofSample > MolesofTitrant:
        FinalMoles=MolesofSample-MolesofTitrant
        FinalVolume=VolumeofSample+VolumeofTitrant
        FinalMolarity=FinalMoles/FinalVolume

        pHWhenFinished=float((-1)*np.log(SampleKA)+np.log((MolesofTitrant/FinalVolume)/(FinalMolarity)))

        print("Congratulations!, the molarity of your existing sample is", round(FinalMolarity, 2), "and the pH is", round(pHWhenFinished, 2))

    if MolesofSample < MolesofTitrant:
        FinalMoles=MolesofTitrant-MolesofSample
        FinalVolume=VolumeofSample+VolumeofTitrant
        FinalMolarity=FinalMoles/FinalVolume
        pHWhenFinished=float((-1)*np.log(FinalMolarity))

        print("Congratulations!, you went past the equivalence point and the pH of your sample is", round(pHWhenFinished, 2))




