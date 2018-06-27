## Before you begin

The next steps assume you have the proper format on your spreadsheet (if not, refer to https://github.com/prosodylab/prosodylab-experimenter/blob/master/instructions.Rmd).

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

#### You should also upload an instruction file, otherwise the default will be used
``` {r, engine='bash', count_lines}
scp instruc.html experiment@prosodylab.cs.mcgill.ca:~/public_html/experimentName/chunk_includes
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
python combine.py originalExperimentFile.txt expresults.txt processedresults.txt
```

## Debugging tips

#### Server side python issues
If server.cgi is where the issue is arising, add a sys.stderr.write() statement, and you can see the output of this statement at /var/log/apache2/prosodylab.error.log

### JavaScript issues
If any javascript file is the issue, use console.log and check the console on your browser.

### Server issues
Be /very/ careful about permissions, this is the issue for server problems a good deal of the time.
Also try to check paths very carefully with print statements, as this is another silly issue that can occur very easily.
Otherwise, in case of more serious server mistakes, check with the CS server administrators.




