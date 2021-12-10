loanamt = int(input("Enter amount of loan sanctioned: "))
ROI = int(input("Enter rate of interest: "))
dur = int(input("Enter duration(in years): "))
print("""Choose frequency:
1. Monthly
2. Quarterly
3. Half-Yearly
4. Yearly""")
freq = int(input("Enter frequency: "))
openprin = loanamt
if freq == 1:
    mthROI = ROI/12
    mthROIamt = round(((openprin*mthROI)/100),2)
    instnum = 12*dur
    print("Your Monthly interest will be: ",mthROIamt,"@",mthROI,"%")
    print("Your no. of installments will be: ",instnum)
    mthEMI = round((openprin*(mthROI/100)*((1+(mthROI/100))**instnum))/(((1+(mthROI/100))**instnum)-1),2)
    mthprin = round((mthEMI - mthROIamt),2)
    print("Your EMI is: ",mthEMI)
    print("Your Principal is: ",mthprin)
    closeprin = openprin-mthEMI
    print("Closing Principal: ",closeprin)
    openprin = closeprin
##elif freq == 2:
##    quarROI = ROI/3
##    quarROIamt = round(((openprin*quarROI)/100),2)
##    instnum = 3*dur
##    print("Your Quarterly interest will be: ",quarROIamt,"@",quarROI,"%")
##    print("Your no. of installments will be: ",instnum)
##    quarEMI = round((openprin*(quarROI/100)*((1+(quarROI/100))**instnum))/(((1+(quarROI/100))**instnum)-1),2)
##    quarprin = round((quarEMI - quarROIamt),2)
##    print("Your EMI is: ",quarEMI)
##    print("Your Principal is: ",quarprin)
##    closeprin = openprin-quarEMI
##    print("Closing Principal: ",closeprin)
##    openprin = closeprin
##elif freq == 3:
##    halfROI = ROI/2
##    halfROIamt = round(((openprin*halfROI)/100),2)
##    instnum = 2*dur
##    print("Your Half-Yearly interest will be: ",halfROIamt,"@",halfROI,"%")
##    print("Your no. of installments will be: ",instnum)
##    halfEMI = round((openprin*(halfROI/100)*((1+(halfROI/100))**instnum))/(((1+(halfROI/100))**instnum)-1),2)
##    halfprin = round((halfEMI - halfROIamt),2)
##    print("Your EMI is: ",halfEMI)
##    print("Your Principal is: ",halfprin)
##    closeprin = openprin-halfEMI
##    print("Closing Principal: ",closeprin)
##    openprin = closeprin
##elif freq == 4:
##    yearROI = ROI
##    yearROIamt = round(((openprin*yearROI)/100),2)
##    instnum = dur
##    print("Your Yearly interest will be: ",yearROIamt,"@",yearROI,"%")
##    print("Your no. of installments will be: ",instnum)
##    yearEMI = round((openprin*(yearROI/100)*((1+(yearROI/100))**instnum))/(((1+(yearROI/100))**instnum)-1),2)
##    yearprin = round((yearEMI - yearROIamt),2)
##    print("Your EMI is: ",yearEMI)
##    print("Your Principal is: ",yearprin)
##    closeprin = openprin-yearEMI
##    print("Closing Principal: ",closeprin)
##    openprin = closeprin
##else:
##    print("Invalid Choice!!!")
##    
