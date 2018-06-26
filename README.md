## ibexconvert

### How to get your own psycholinguistic experiment up!
Assuming you've got the proper format on your spreadsheet (if not, refer to https://github.com/prosodylab/prosodylab-experimenter/blob/master/instructions.Rmd)
The only addition to your spreadsheet is a column titled "Controller." Put the value "QAJ" if you'd like an audio experiment and "AJ" if you'd like an audio-less experiment.

## Setup

#### Run convert.py on your spreadsheet from the command line

``` {r, engine='bash', count_lines}
python convert.py originalExperimentFile.txt dataFileName.js 
```

#### SCP the JavaScript file to the server

``` {r, engine='bash', count_lines}
scp dataFileName.js experiment@prosodylab.cs.mcgill.ca:~/public_html/
```

#### SSH into the Prosody Lab web server (must have an account)

``` {r, engine='bash', count_lines}
ssh experiment@prosodylab.cs.mcgill.ca
```

#### Run the script titled setup.sh (done remotely on prosody server)

``` {r, engine='bash', count_lines}
sh setup.sh experimentName dataFileName.js
```

#### Further configuration can be done, i.e. SCP-ing audio files for audio experiments. For example, navigate to the file containing the audio files and:
``` {r, engine='bash', count_lines}
scp *.wav experiment@prosodylab.cs.mcgill.ca:~/public_html/experimentName/chunk_includes
```

#### Go to...
`http://prosodylab.cs.mcgill.ca/~experiment/experimentName/www/experiment.html`


## Results

#### Results can be accessed by... (remote)

``` {r, engine='bash', count_lines}
scp experiment@prosodylab.cs.mcgill.ca:~/public_html/experimentName/results/results.txt ./expresults.txt
```

#### To process results,
``` {r, engine='bash', count_lines}
python combinePlus.py originalExperimentFile.txt expresults.txt processedresults.txt
```


