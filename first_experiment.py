import expyriment
import os
from random import choice, shuffle


beginning_text = "We are measuring multitasking. Your task will be to classify figures." 
beginning_text_continue = "If they appear under the label 'Shape', you will have to press the LEFT arrow key if it is a diamond and the RIGHT arrow key if it is a square. If the figure appears above 'Filling', you will have to press the LEFT arrow key if it contains two dots and the RIGHT arrow key if it contains three dots. \nPlease press any key to continue if you have understood the instructions. \nIf at any time you will want to end the experiment, you can press ESCAPE."
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

intertrial_interval = 800
wrong_no_answer_wait = 5000
pause = 500 

#The order of blocks was identical for all par- ticipants. 

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


exp = expyriment.design.Experiment(name="Multitasking")
expyriment.control.initialize(exp)


expyriment.stimuli.TextScreen("Welcome to our multitasking experiment.", heading_size = 40, text = beginning_text + beginning_text_continue).present()
exp.keyboard.wait()

expyriment.stimuli.TextScreen(info_text, heading_size = 40, text =  "If your biological gender is male press M, if it is female press F").present()
sex, x = exp.keyboard.wait_char(["m", "f"])

expyriment.stimuli.TextScreen(info_text, heading_size = 40, text =  "Please press any key to continue, enter your age and then press ENTER.").present()
exp.keyboard.wait()
age = expyriment.io.TextInput("").get()


#First
block_one = expyriment.design.Block(name="Training")

trial_one = expyriment.design.Trial()
trial_two = expyriment.design.Trial()
trial_three = expyriment.design.Trial()

result = adding_stimuli(ordering[0], trial_one, trial_two, trial_three)
block_one.add_trial(result[0])
block_one.add_trial(result[1])
block_one.add_trial(result[2])

exp.add_block(block_one)

#Second
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
exp.data_variable_names = ["Block", "Trial", "Sex", "Age", "Key", "RT", "Response"]

def determine_correct(current_stimulus):
	correct_determined = ""
	if (current_stimulus[0] == 'd' and current_stimulus[2] == 'u') or (current_stimulus[2] == 'd' and current_stimulus[1] == '2'):
	    correct_determined = "LEFT"
	elif (current_stimulus[0] == 's' and current_stimulus[2] == 'u') or (current_stimulus[2] == 'd' and current_stimulus[1] == '3'):
	    correct_determined = "RIGHT"
	return correct_determined

current = ""
press = ""
counter_blocks = -1
counter_trials = -1
counter_stimuli = -1
correct = ""
correctness = ""
counter = 0
for block in exp.blocks:
	counter_blocks += 1
	for trial in block.trials:
		if counter == 0:
			expyriment.stimuli.TextScreen("Welcome to our multitasking experiment.", heading_size = 40, text = "You will have to press the LEFT arrow key if it is a diamond and the RIGHT arrow key if it is a square").present()
			exp.keyboard.wait()
		if counter == 1:
			expyriment.stimuli.TextScreen("Welcome to our multitasking experiment.", heading_size = 40, text = "You will have to press the LEFT arrow key if it contains two dots and the RIGHT arrow key if it contains three dots).present()
			exp.keyboard.wait()
		if counter == 2:
			xpyriment.stimuli.TextScreen("Third part consists in the real multitasking task. Here, figures will appear under 'Shape' and above 'Filling' interchangeably", heading_size = 40, text = beginning_text_continue).present()
			exp.keyboard.wait()
		counter += 1
		counter_trials += 1
		for stimulus in trial.stimuli:
			counter_stimuli += 1
			stimulus.present()
			key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT], duration=4000)
			if key == 1073741904:
				press = "LEFT" 
			elif key == 1073741903:
				press = "RIGHT" 
			if block == exp.blocks[0]:
				current = ordering[0][counter_trials][counter_stimuli]
				correct = determine_correct(current)
			elif block == exp.blocks[1]:
				current = ordering[1][counter_trials][counter_stimuli]
				correct = determine_correct(current)
			if correct == press:
				exp.clock.wait(intertrial_interval)
				correctness = "CORRECT"
			else:
				if current[2] == 'u':
					reminder = "When the stimulus appears under 'Shape': if it is a diamond press LEFT, if it is a square press RIGHT."
				elif current[2] == 'd':
					reminder = "When the stimulus appears above 'Filling': if it contains two dots press LEFT, if it contains three press RIGHT." 
				if correct == "LEFT":
					expyriment.stimuli.TextScreen(response, text_size = 40, text= reminder + "\nThe correct response was LEFT").present()
				else:
					expyriment.stimuli.TextScreen(response, text_size = 40, text= reminder +"\nThe correct response was RIGHT").present()
				exp.clock.wait(wrong_no_answer_wait)
				expyriment.stimuli.BlankScreen().present()
				exp.clock.wait(pause)
				correctness = "WRONG"
			if block == exp.blocks[0]:
			    exp.data.add([block.name, trial.id, sex, age, press, rt, correctness])
		counter_stimuli = 0
	counter_trials = 0


expyriment.control.end(goodbye_text="Thank you for participating in our experiment.")