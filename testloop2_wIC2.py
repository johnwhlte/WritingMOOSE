import pandas as pd
import numpy as np
import os
from subprocess import call

#insert your bashProfile (or other directory) into the os.chdir inputs
#you have to write it all out the "~" shortcut doesn't work

os.chdir("/home/bashProfile/projects/moose/examples/ex05_amr/Helpers") #change directory to the one containing the C files
call(["gcc","CopyBlock.C","-o","CopyBlock"])
call(["./CopyBlock","161.inp","Surface1.txt","Surface1"])
call(["./CopyBlock","161.inp","Surface2.txt","Surface2"]) #runs the CopyBlock.C

call(["gcc","NameBlocks.C","-o","NameBlocks"])
call(["./NameBlocks","Surface1.txt","Surface1Blocks.txt"])
call(["./NameBlocks","Surface1.txt","Surface2Blocks.txt"]) #runs NameBlocks.C

call(["gcc","MakeMesh.C","-o","MakeMesh"])
call(["./MakeMesh","161.inp","Surface1","Surface1Blocks.txt","newmesh.inp"])
call(["./MakeMesh","newmesh.inp","Surface2","Surface2Blocks.txt","trialmesh.inp"]) #runs MakeMesh.C

call(["gcc","MakeCSV.C","-o","MakeCSV"])
call(["./MakeCSV","Surface1.txt","Surface1Props.txt"])
call(["./MakeCSV","Surface2.txt","Surface2Props.txt"]) #runs MakeCSV.C

call(["cp","-r","Surface1Props.txt","/home/bashProfile/projects/moose/examples/ex01_inputfile"]) #Copies the necessary files into the directory to run the input file
call(["cp","-r","Surface2Props.txt","/home/bashProfile/projects/moose/examples/ex01_inputfile"])
call(["cp","-r","trialmesh.inp","/home/bashProfile/projects/moose/examples/ex01_inputfile"])

os.chdir("/home/bashProfile/projects/moose/examples/ex01_inputfile") #changes directory to the one with the input file

#reads the two surface txt files which contain the element ids, coefficient of diffusion, and x-velocity
numofRowscsv = pd.read_csv('Surface1Props.txt',sep=" ",header=None) 
numofRowscsv2 = pd.read_csv('Surface2Props.txt',sep=" ",header=None)
#reads the first column of the files to determine how many element blocks there are.
numofElemSet = numofRowscsv[0][:]
numofElemSet2 = numofRowscsv2[0][:]
numofElem = len(numofElemSet)
numofElem2 = len(numofElemSet2)
#main script for running the input file (this would be the start of the loop when doing multiple iterations)
with open('TEST.i','w') as f:       #open and write the input file
    f.write('[Mesh]\n')
    f.write('  file = trialmesh.inp\n')
    f.write('[]\n')
    f.write('[Variables]\n')
    f.write('  [./diffused]\n')
    f.write('    order = FIRST\n')
    f.write('    family = LAGRANGE\n')
    f.write('  [../]\n')
    f.write('  [./convected]\n')
    f.write('    order = FIRST\n')
    f.write('    family = LAGRANGE\n')
    f.write('  [../]\n')
    f.write('[]\n')
    f.write('[Kernels]\n')
    for i in range (0,(numofElem)): #loop for writing the kernel from csv file
            f.write('  [./conv' + str(i) + '] \n')
            f.write('    type = ExampleConvection \n')
            f.write('    Variable = convected \n')
            f.write('    test = '+ (str(numofRowscsv[0][i]) + ' \n'))
            f.write('    velocity = '+ "'" + (str(numofRowscsv[2][i]) +  " 0.0 0.0'" + ' \n'))
            f.write('  [../] \n')
            f.write('  [./diff' + str(i) + '] \n')
            f.write('    type = ExampleCoefDiffusion \n')
            f.write('    Variable = diffused \n')
            f.write('    block = '+ (str(numofRowscsv[0][i]) + ' \n'))
            f.write('    coef = '+ (str(numofRowscsv[1][i]) + ' \n'))
            f.write('  [../] \n')
    for i in range (0,numofElem2): #loop for writing the kernel from csv file
            f.write('  [./conve' + str(i) + '] \n')
            f.write('    type = ExampleConvection \n')
            f.write('    Variable = convected \n')
            f.write('    block = '+ (str(numofRowscsv2[0][i]) + ' \n'))
            f.write('    velocity = '+ "'" + (str(numofRowscsv2[2][i]) +  " 0.0 0.0'" + ' \n'))
            f.write('  [../] \n')
            f.write('  [./diffu' + str(i) + '] \n')
            f.write('    type = ExampleCoefDiffusion \n')
            f.write('    Variable = diffused \n')
            f.write('    block = '+ (str(numofRowscsv2[0][i]) + ' \n'))
            f.write('    coef = '+ (str(numofRowscsv2[2][i]) + ' \n'))
            f.write('  [../] \n')
    f.write('[]\n')
    f.write('[ICs]\n')
    for i in range (0,(numofElem)): #loop for writing the ICs from csv file
        f.write('  [./mat_' + str(i) + '] \n')
        f.write('    type = ExampleIC \n')
        f.write('    Variable = convected \n')
        f.write('    block = '+ (str(numofRowscsv[0][i]) + ' \n'))
        f.write('    coefficient = 1.0' + '\n')
        f.write('  [../] \n')
        f.write('  [./mat-' + str(i) + '] \n')
        f.write('    type = ExampleIC \n')
        f.write('    Variable = diffused \n')
        f.write('    block = '+ (str(numofRowscsv[0][i]) + ' \n'))
        f.write('    coefficient = 1.0' + ' \n')
        f.write('  [../] \n')
    for i in range (0,numofElem2): #loop for writing the ICs from csv file
        f.write('  [./mate_' + str(i) + '] \n')
        f.write('    type = ExampleIC \n')
        f.write('    Variable = convected \n')
        f.write('    block = '+ (str(numofRowscsv[0][i]) + ' \n'))
        f.write('    coefficient = 1.0' + '\n')
        f.write('  [../] \n')
        f.write('  [./mate-' + str(i) + '] \n')
        f.write('    type = ExampleIC \n')
        f.write('    Variable = diffused \n')
        f.write('    block = '+ (str(numofRowscsv[0][i]) + ' \n'))
        f.write('    coefficient = 1.0' + ' \n')
        f.write('  [../] \n')
    f.write('[]\n')   
    f.write('[BCs]\n')
    f.write('  [./bottom]\n')
    f.write('    type = DirichletBC\n')
    f.write('    variable = diffused\n')
    f.write('    boundary = "bottom"\n')
    f.write('    value = 1\n')
    f.write('  [../]\n')
    f.write('  [./top]\n')
    f.write('    type = DirichletBC\n')
    f.write('    variable = diffused\n')
    f.write('    boundary = "top"\n')
    f.write('    value = 0\n')
    f.write('  [../]\n')
    f.write('[]\n')
    f.write('[Executioner]\n')
    f.write('  type = Steady\n')
    f.write('  solve_type = "PJFNK"\n')
    f.write('  file_base = "out"\n')
    f.write('[]\n')
    f.write('[Outputs]\n')
    f.write('  execute_on = "timestep_end"\n')
    f.write('  exodus = true\n')
    f.write('[]\n')

#script for executing commands in the terminal               
    call(["make","-j8"])
    call(["./ex01-opt","-i","TEST.i"])      #executing moose
    os.system("ncdump TEST_out.e > TEST_out.txt")   #converting exodus to text file
    data_from_run = np.genfromtxt('TEST_out.txt',delimiter=',',skip_header=78 ,usecols=np.arange(0,2),invalid_raise=False) #parsing the text file
    IC = float(data_from_run[0][1])      #setting the new initial condition
#statements for copying the single output into the overall output
    with open('TEST_out.txt') as f:
        with open('output.txt','a') as f1:
            for line in f:
                f1.write(line)
#remove the single output files, last part of the loop
    call(["rm","-rf","TEST_out.e"])
    call(["rm","-rf","TEST_out.txt"])
#making sure the code is running, also could be implemented to show loop is over
    print(str(IC))
    print('done')

#just for testing the code, will be removed
call(["cp","-r","TEST.i","/mnt/c/Users/johnw/OneDrive/Desktop/Academics/Research/Vuggy_Porous_Media/python"])
#change directory back to the original one (may not be necessary)
os.chdir("/mnt/c/Users/johnw/OneDrive/Desktop/Academics/Research/Vuggy_Porous_Media/python")