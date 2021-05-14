import expyriment
import os
from random import choice

#waiting times 
INTERTRIAL_INTERVAL = 800
WRONG_NO_ANSWER_WAIT = 5000
PAUSE = 500

#some of the text used
beginning_text = "We are measuring multitasking. Your task will be to classify figures." 
beginning_text_continue = "If they appear under the label 'Shape', you have to press the LEFT arrow key if it is a diamond and the RIGHT arrow key if it is a square. If the figure appears above 'Filling', you will have to press the LEFT arrow key if it contains two dots and the RIGHT arrow key if it contains three dots. \nPlease press any key to continue if you have understood the instructions. \nIf at any time you will want to end the experiment, you can press ESCAPE."
info_text = "First, we would like to know something about you."
response = "Your response was incorrect or not received."

#First, the order is generated
ordering_train = []
ordering_real = []
ordering = []

def determine_order(stimuli_for_ordering, trials_number):
    ordered = []
    for k in range(trials_number):
        ordered.append(choice(stimuli_for_ordering))
    return ordered

ordering_train.append(determine_order(["d2u","d3u","s2u","s3u"], 40))
ordering_train.append(determine_order(["d2d","d3d","s2d","s3d"], 40))
ordering_train.append(determine_order(["d2u","d3u","s2u","s3u","d2d","d3d","s2d","s3d"], 40))
ordering.append(ordering_train)
ordering_real.append(determine_order(["d2u","d3u","s2u","s3u"], 64))
ordering_real.append(determine_order(["d2d","d3d","s2d","s3d"], 64))
ordering_real.append(determine_order(["d2u","d3u","s2u","s3u","d2d","d3d","s2d","s3d"], 64))
ordering.append(ordering_real)


#function for adding stimuli
def adding_stimuli(ordering_list, trial1, trial2, trial3):
	for training_block in ordering_list:
	    for one_trial in training_block:
	        stim = expyriment.stimuli.Picture(os.getcwd() + '/Stimuli/' + one_trial + '.png')
	        stim.preload()
	        if training_block == ordering_list[0]:
	    	    trial1.add_stimulus(stim)
	        if training_block == ordering_list[1]:
	    	    trial2.add_stimulus(stim)
	        if training_block == ordering_list[2]:
	    	    trial3.add_stimulus(stim)
	return trial1, trial2, trial3


#Starting the experiment 
"""We should add that the words "Block", "Trial", and "Stimulus" mean different things here 
compared to the use in the paper we are recreating. Here, we have two blocks of three trials, 
first block with 40 stimuli and second block with 64 stimuli each time. In the paper, 
blocks are our trials and trials are our stimuli.
In the data file we use the terminology provided in the paper, because the first block (in our parlance) doesn't figure in the data at all, 
so we can consider as blocks the three trials and as trials the 64 * 3 stimuli. """
exp = expyriment.design.Experiment(name="Multitasking")
expyriment.control.initialize(exp)

expyriment.stimuli.TextScreen("Welcome to our multitasking experiment.", heading_size = 40, text = beginning_text + beginning_text_continue).present()
exp.keyboard.wait()

expyriment.stimuli.TextScreen(info_text, heading_size = 40, text =  "If your biological gender is male press M, if it is female press F").present()
sex, x = exp.keyboard.wait_char(["m", "f"])

expyriment.stimuli.TextScreen(info_text, heading_size = 40, text =  "Please press any key to continue, enter your age and then press ENTER.").present()
exp.keyboard.wait()
age = expyriment.io.TextInput("").get()


#First block (training)
block_one = expyriment.design.Block(name="Training")

trial_one = expyriment.design.Trial()
trial_two = expyriment.design.Trial()
trial_three = expyriment.design.Trial()

result = adding_stimuli(ordering[0], trial_one, trial_two, trial_three)
block_one.add_trial(result[0])
block_one.add_trial(result[1])
block_one.add_trial(result[2])

exp.add_block(block_one)

#Second block (training)
block_two = expyriment.design.Block(name="Experiment")

trial_one = expyriment.design.Trial()
trial_two = expyriment.design.Trial()
trial_three = expyriment.design.Trial()

result = adding_stimuli(ordering[1], trial_one, trial_two, trial_three)
block_two.add_trial(result[0])
block_two.add_trial(result[1])
block_two.add_trial(result[2])

exp.add_block(block_two)


expyriment.control.start()
exp.data_variable_names = ["Block", "Trial", "Sex", "Age", "Key", "RT", "Response", "Task Switch or not"]

#function that determines whas is the correct response
def determine_correct(current_stimulus):
	correct_determined = ""
	if (current_stimulus[0] == 'd' and current_stimulus[2] == 'u') or (current_stimulus[2] == 'd' and current_stimulus[1] == '2'):
	    correct_determined = "LEFT"
	elif (current_stimulus[0] == 's' and current_stimulus[2] == 'u') or (current_stimulus[2] == 'd' and current_stimulus[1] == '3'):
	    correct_determined = "RIGHT"
	return correct_determined

#function that returns the instructions according to the trial (just shapes, just content, both)
def greet(number_of_trial):
	task_first = ""
	task_second = ""
	if number_of_trial == 0:
	    task_first = "Here is your first task."
	    task_second = "You have to press the LEFT arrow key if you see a diamond and the RIGHT arrow key if you see a square. Now press any key to continue."
	if number_of_trial == 1:
	    task_first = "We continue with your second task."
	    task_second = "You have to press the LEFT arrow key if you see a diamond and the RIGHT arrow key if you see a square. Now press any key to continue."
	if number_of_trial == 2:
		task_first = "Third part consists in the real multitasking task."
		task_second = "Here, figures will appear under 'Shape' and above 'Filling' interchangeably. If the figure appears under 'Shape', you have to press the LEFT arrow key if you see a diamond and the RIGHT arrow key if you see a square. If it appears above 'Filling', you have to press the LEFT arrow key if you see two dots and the RIGHT arrow key if you see three. Now press any key to continue."
	return task_first, task_second


#the main function that executes the experiment
current_stimulus = "  x"
pressed_key = ""
counter_trials = 0
counter_stimuli = 0
correct_answer = ""
right_or_wrong = ""
previous_stimulus = "  x"
task_switch = False
for block in exp.blocks:
	for trial in block.trials:
		number_of_correct_responses = 0
		first, second = greet(counter_trials)
		expyriment.stimuli.TextScreen(first, heading_size = 40, text = second).present()
		exp.keyboard.wait()
		for stimulus in trial.stimuli:
			stimulus.present()
			key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT], duration=4000)
			if key == 1073741904:
				pressed_key = "LEFT" 
			elif key == 1073741903:
				pressed_key = "RIGHT" 
			if block == exp.blocks[0]: #training block
				current_stimulus = ordering[0][counter_trials][counter_stimuli]
				correct_answer = determine_correct(current_stimulus)
			elif block == exp.blocks[1]: #real block
			    previous_stimulus = current_stimulus
			    current_stimulus = ordering[1][counter_trials][counter_stimuli]
			    correct_answer = determine_correct(current_stimulus)
			    if previous_stimulus[2] != current_stimulus[2] and counter_stimuli != 0:
			        task_switch = True
			    else: 
			        task_switch = False
			if correct_answer == pressed_key: #answer is correct
				exp.clock.wait(INTERTRIAL_INTERVAL)
				right_or_wrong = "CORRECT"
				number_of_correct_responses += 1
			else: #answer is wrong
				if current_stimulus[2] == 'u':
					reminder = "When the stimulus appears under 'Shape': if it is a diamond press LEFT, if it is a square press RIGHT."
				elif current_stimulus[2] == 'd':
					reminder = "When the stimulus appears above 'Filling': if it contains two dots press LEFT, if it contains three press RIGHT." 
				if correct_answer == "LEFT":
					expyriment.stimuli.TextScreen(response, text_size = 40, text= reminder + "\nThe correct response was LEFT").present()
				else:
					expyriment.stimuli.TextScreen(response, text_size = 40, text= reminder +"\nThe correct response was RIGHT").present()
				exp.clock.wait(WRONG_NO_ANSWER_WAIT)
				expyriment.stimuli.BlankScreen().present()
				exp.clock.wait(PAUSE)
				right_or_wrong = "WRONG"
			if block == exp.blocks[1]: #in block 2 we add data
			    exp.data.add([trial.id+1, counter_stimuli+1, sex, age, pressed_key, rt, right_or_wrong, task_switch])
			counter_stimuli += 1
		counter_stimuli = 0
		counter_trials += 1
	counter_trials = 0


expyriment.control.end(goodbye_text="This is the end of the experiment. Thank you for participating.")