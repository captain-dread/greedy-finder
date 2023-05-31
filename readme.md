# Using Greedy Finder

In order to use Greedy Finder, you will need to log your puzzle pirates messages. (Options -> Chat). After, you can select the log file you are generating and load it into Greedy Finder. Some notes: 
- You need to wait for the "The victors plundered" message to appear in order to get the greedy hits.
- You **don't** need to reload the log file every time, just click on "Find Greedy Hits" to get the latest greedy hits.
- This is completely withing the game's TOS. You can read more about it [here](https://yppedia.puzzlepirates.com/Official:Third_Party_Software).

### MacOS/Unix
Under `/dist` folder, there is a `greedy-finder` executable file. You can run it directly which would be the same as running the script, but without the need to install python3 or the libraries it uses.

### Running Script Directly (MacOS/Unix/Windows)

If you don't want to run the executable file, you can run the python script directly. In order to do so, you will need to have Python and certain Python libraries installed on your machine. 

#### Installing Python
If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/). Make sure you download the latest version of Python 3.

Verify that you have Python installed by typing the following in your terminal:

```bash
python3 --version
```

#### Installing Python Libraries
You can install PySimpleGUI using Python's package installer, pip. In your terminal, type:

```bash
pip3 install PySimpleGUI
```

#### Running the Script
Once you have Python and the required libraries installed, you can run the script by typing the following in your terminal:

```bash
python3 greedy-finder.py
```

