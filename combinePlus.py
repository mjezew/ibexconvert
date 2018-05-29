#New Plan: Take another optional argument of -s to specify self paced reading
#PLAN: take two input files, and an output name(3 args). The first input is the original experiment file, the second is
#the experiment results.
#plan to adjust new  stuff:
#If controllertype=form, store the rest of the cells in the row in special screeningData structure of some kind?
import sys
import re
import json

originalExperiment=sys.argv[1]
trialDataFile=sys.argv[2]
outputFileName=sys.argv[3]
isSelfPaced=False
if len(sys.argv)>4:
    if sys.argv[1]=="-s":
        isSelfPaced=True
        originalExperiment=sys.argv[2]
        trialDataFile=sys.argv[3]
        outputFileName=sys.argv[4]

f=open(originalExperiment)

experimentData=re.split(r"(?:\r\n)|(?:\n)|(?:\r)",f.read())

f.close()

f2=open(trialDataFile)
trialDataList=re.split(r"(?:\r\n)|(?:\n)|(?:\r)",f2.read())

f2.close()
#nonHeadersString=''.join(experimentData[1:len(experimentData)])#old code, possibly useful later
#grabs the trial headers
trialDataHeadersA=[]
sentenceLocatedIn=0
newSentenceApproaching=False
pattern=re.compile(r"(?:^#\s*Col\.\s*)(\d?\d?)(?::)(?:\s*)(.*)")
for trialHeadA in trialDataList:
    match=pattern.match(trialHeadA)
    if match:
        if isSelfPaced:
            print match.group(2)
            if (int(match.group(1))==12 and match.group(2)=="Sentence (or sentence MD5)."):
                #need to get sentence, and number of chunks in said sentence(for now just word count?)
                #perhaps track the number of lines I've gone through, comparing it to the word count.
                #Once they are equal, check for new one?
                #Possibly keep an array of locations where the sentences end?
                newSentenceApproaching=True
                print newSentenceApproaching
                #need to put this elsewhere
        if ("\t"+match.group(2)) not in trialDataHeadersA and int(match.group(1)) >len(trialDataHeadersA):
            tstring=("\t"+match.group(2)).lstrip('')
            trialDataHeadersA.append(tstring)
        elif int(match.group(1)) < len(trialDataHeadersA) and (match.group(2) not in trialDataHeadersA[int(match.group(1))-1]) and ("\t"+match.group(2)) not in trialDataHeadersA:
            trialDataHeadersA[int(match.group(1))-1]+=("/"+match.group(2)).lstrip('')
#trialDataHeadersA=re.split(r"(?:^#\s*Col\.\s*\d?\d?:)(.*)",f2.read())
trialString=''.join(trialDataHeadersA)
commaCount=trialString.count('\t')
#print commaCount
#get worker ID\
workerid=''
#workerid[0]='ID not Found'
#workerid='ID not found'
fullcount=-1
#idPattern=re.compile(r"^\#PARTICIPANT\sID:\s(\w*)$")


#print idPattern
#idPattern=re.compile(r"^PARTICIPANT\sID:\s(\d*)$")
idPattern = re.compile(r"workerid,(\w*)")

for workerLines in trialDataList:
    fullcount+=1
    match=idPattern.search(workerLines)
    #print workerLines
    #print match
    if match:
        workerid=match.group(1)
    if len(workerLines)>0 and workerLines[0]!="#" and not match:
            workerLinesList=workerLines.split(',')
            while trialDataList[fullcount].count(',') < commaCount-1:
                trialDataList[fullcount]+=',NULL'
            trialDataList[fullcount]+=","+workerid
            #if workerLinesList[7]=="workerid":
            #    workerid[workercount]=workerLinesList[8]
            #    workerid=workerLinesList[8]
#retrieve headers from original files
headersString=experimentData[0]+trialString+"\tQuestion"+"\tJudgment"+"\tNULL"+"\tTime taken to answer."+"\t Worker ID"
#read number of tabs in experimentfile, to add form data without having odd number of columns
tabcount=experimentData[1].count('\t')
#open output
newoutput=open(outputFileName,'w')
#write headers to newoutput
newoutput.write(headersString+'\n')
#check item number(4th in each row from trial data) with row number of originalExperiment
formNumber=0
screeningPattern=re.compile(r"^.*,.*,Form,(\d),.*$")
for trialLine in trialDataList:
    if len(trialLine)>0 and trialLine[0]!="#":
        match=screeningPattern.match(trialLine)
        idMatch=idPattern.match(trialLine)
        if match:
            #need to acquire number of forms, this should always trigger before the else section does, but this is iffy
            if formNumber==0:
                formNumber=int(match.group(1))
            formGatherA=trialLine.split(',')
            t=-1
            while t<tabcount:
                t=t+1
                newoutput.write("NULL\t")
            newoutput.write(trialLine.replace(",","\t")+"\t""\n")
            #if itemNum and itemNum>0:
            #print "formfound"
        elif idMatch:
            pass
        else:
            if formNumber==0:
                formNumber=4
            #print trialLine
            itemNum=int(trialLine.split(',')[3])-formNumber
            if itemNum ==1:
                newoutput.write(experimentData[itemNum]+"\t"+trialLine.replace(",", "\t")+"\t""\n")
            elif itemNum and itemNum>=0:
                #take row number item num from experimentData
                #add workerid based on experiment type
                #print experimentData[itemNum]+trialLine
                #print experimentData[itemNum]
                #print trialLine
                #print itemNum
                newoutput.write(experimentData[itemNum]+"\t"+trialLine.replace(",", "\t")+"\t""\n")
            else:
                #plus 1 if exp1 or exp2, plus 2 if exp3 for liz
                newoutput.write(experimentData[itemNum+1]+"\t"+trialLine.replace(",", "\t")+"\t""\n")
newoutput.close()
