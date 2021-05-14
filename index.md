## Are women better than men at multi-tasking?

Recreating the experiment presented in Stoet et al. (2013).

# The project

The project consisted in replicating the paper (Stoet et al.) which tried to verify the common belief that women are better at multi-tasking than men. To check this, they designed two experiments. In the first one, computer-based task switching paradigm was used, and in the second one, paper-and-pencil multi-tasking tests were used.

According to Stoet et al. (2013), multi-tasking can be defined in two ways: as performing several tasks sequentially/interchangeably or as performing several tasks simultaneously. It is the first sense that is used in the part of the paper by Stoet et al. (2013) that we reproduced. Here, multi-tasking ammounted to task-switching.

We have only reproduce Experiment 1, because Experiment 2 wasn’t computer-based at all; it aimed to create a "real-life" multi-tasking situation and used standardized neuro-cognitive tests.

## The Experiment

The main concept of the experiment is responding to the location and the form of stimuli: 
1. *differentiating between diamonds and squares* (if the stimuli appears bellow "Shape") by pressing the LEFT arrow key for a diamond and the RIGHT arrow key for a square
2. *differentiating between the number (2 or 3) of dots inside the figure* (if the stimuli appears above "Filling") by pressing the LEFT arrow key for two dots and the RIGHT arrow key for three dots. 

First, the experiment is divided in two parts: training and the real experiment (where the actual data are collected). Each part consists of three blocks of trials (40 each for training and 64 each in the real experiment). In the first block, subjects only differentiate between diamonds and squares and in the second block they only differentiate between the number of dots in the figures (2 or 3). It is only in the third block that the real experiment starts: figures randomly (and intechangeably) appear either bellow "Shape" or above "Filling" which determines whether the subject has to focus on shapes or dots and press the key accordingly.

## Running the experiment

To run the experiment, make sure you have downloaded the whole folder, including the folder `Stimuli` and the files `multi_tasking_code.py`, `generate_results.py`, and `data_analysis.py`. First, several subjects have to take part in the experiment to provide data. This is done by running the file `multi_tasking_code.py`. Using the terminal, this means first moving to the folder where all the mentioned (downloaded) files are and then executing:
```
python multi_tasking_code.py
```
Once that the data has been provided, we can analyse it by running:
```
python data_analysis.py
```
This will generate two figures. 
`generate_results.py` is just an auxiliary file that is used by the file `data_analysis.py`, so we don't have to run it.

## My implementation

My implementation of the experiment has four parts. 

1. The first part is the folder `Stimuli` with images of stimuli used. I've had some problems with stimuli, so I had to manually generate them and they are therefore in a separate folder that has to be included. 

2. The main part is of course the file `multi_tasking_code.py`, where the experiment itself takes place. 
   - First, the file generates the order of stimuli, then prepares two blocks of three trials, each with 40 stimuli for the training part and 64 each for the actual
   experimental part. As mentioned earlier, only in the second block data are collected. We should add that the words "Block", "Trial", and "Stimulus" mean different things here compared to the use in the paper we are recreating. Here, we have two blocks of three trials, first block with 40 stimuli and second block with 64 stimuli for each of the three trials that constitute it. It is only in this second block that the actual experiment begins (data start getting collected). In the paper, "blocks" are our trials and "trials" are our stimuli. In the `generate_results.py` file, we use the terminology provided in the paper, because the first block (in our parlance) doesn't figure in the data at all, so we can consider as blocks the three trials and as trials the 64 * 3 stimuli.
   -  `multi_tasking_code.py` creates a folder called `data` and its sister file `events`. For each subject (or rather: for each try), a file is created in the `data` folder and one in the `events` folder. In the latter, all the events (such as that a certain stimuli image was presented, that a key was pressed etc.) are described, but the former is more important.  For each stimulus that the subject classifies, a line is written in the `data` folder describing the subject number, the block and the trial numbers, the subject's gender and age, which key was pressed (as mentioned above, subjects have to press the LEFT arrow key when they see a diamond under the label 'Shape', for example), their reaction time, whether their response was correct, whether the stimulus switched from under the label 'Shape' to above the label 'Filling' or the other way arond, and whether it is congruent or not (meaning if it requires the same response in both tasks, for example a dimaond with two dots requires a LEFT arrow key press whether it appears under 'Shape' or above 'Filling')
Thus, a line of the following type is generated: 
```
Subject_id Block, Trial, Sex, Age, Key, Response Time (ms), Response, Task Switch or not, Congruent or not
   4,       3,      1,    f,   22, LEFT,    1016,           CORRECT,        False,              True
```
3. The third part is the file `generate_results.py` which is responsible for (surprise, surprise) generating the results by taking all the lines from the files of particular subjects (/tries) and averaging the response times for different conditions and also calculating error rates, so that the result is a dictionary with 14 values for each subject: sex, age and then the possible conditions: six for response times and six for error rates: two for "pure" blocks where the task isn't changing (one for congruent and the other for incongruent cases), two for mixed trials where the task repeats itself (one for congruent and the other for incongruent cases), and two for mixed trials where the task changes (one for congruent and the other for incongruent cases).

4. The last part is the file `data_analysis.py` which first takes runs `generate_results.py` and gets a dictionary of individual subjects. Then it divides the results into those by men and women (since that is the purpose of the experiment) and averages them. Also, it converts the response times into seconds (from miliseconds) and the error rates into percentages (from decimals). Then it plots two graphs, one with response rates for each condition (and comparing men and women) and the other with error rates (also for each condition and comparing men and women). Here, we provide these graphs (although the data are illustrative since we only used one female and one male subject) in our repository: 
<img src="https://user-images.githubusercontent.com/53874416/118336321-b7f09180-b511-11eb-9aad-ec06e13acfe8.png" width="450" height="350"> <img src="https://user-images.githubusercontent.com/53874416/118336180-7233c900-b511-11eb-9680-4e34c014c0dd.png" width="450" height="350"> 


### Other remarks

Because of my philosophical and linguistic background this was my first time programming a project in Python, so the class was a new experience to me. It was interesting not to just get some programming skills, but also to learn how to use GitHub which is something I will probably need in the future, too. 
What I missed in the class was especially a bit more thourough introduction to basic programming concepts. I am aware, however, that we didn't have a lot of time and that it is almost impossible to make the class work since the students' skills are so different.
