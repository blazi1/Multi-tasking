import expyriment
import os


#expyriment.control.set_develop_mode(True)
exp = expyriment.design.Experiment(name="Multitasking")
expyriment.control.initialize(exp)

STIM_DIR = 'Stimuli_folder/'

block_one = expyriment.design.Block(name="Primerno tudi za moske")

trial_one = expyriment.design.Trial()
#stim1 = expyriment.stimuli.TextLine(text="Ena ena1")
#pngname = os.path(STIM_DIR)
stim1 = expyriment.stimuli.Picture(os.getcwd() + '/Stimuli/' + 's2u.png')
stim1.preload()
trial_one.add_stimulus(stim1)
stim2 = expyriment.stimuli.Picture(os.getcwd() + '/Stimuli/' + 's2d.png')
stim2.preload()
trial_one.add_stimulus(stim2)
stim3 = expyriment.stimuli.Picture(os.getcwd() + '/Stimuli/' + 's3u.png')
stim3.preload()
trial_one.add_stimulus(stim3)

trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.TextLine(text="Ena dve")
stim.preload()
trial_two.add_stimulus(stim)


block_one.add_trial(trial_one)
block_one.add_trial(trial_two)
exp.add_block(block_one)



block_two = expyriment.design.Block(name="Primerno tudi za moske")

trial_one = expyriment.design.Trial()
stim = expyriment.stimuli.Picture(os.getcwd() + '/Stimuli/' + 's3d.png')
stim.preload()
trial_one.add_stimulus(stim)

trial_two = expyriment.design.Trial()
stim = expyriment.stimuli.Picture(os.getcwd() + '/Stimuli/' + 'd2u.png')
stim.preload()
trial_two.add_stimulus(stim)

block_two.add_trial(trial_one)
block_two.add_trial(trial_two)
exp.add_block(block_two)



expyriment.control.start()
exp.data_variable_names = ["Block", "Trial", "Key", "RT"]

for block in exp.blocks:
	for trial in block.trials:
		for stimulus in trial.stimuli:
			stimulus.present()
			#trial.stimuli[0].present()
			#exp.clock.wait(1000)
			key, rt = exp.keyboard.wait([expyriment.misc.constants.K_LEFT,
                                     expyriment.misc.constants.K_RIGHT], duration=4000)
			#if rt == None ALI ČE JE ODGOVOR NAPAČEN:
			    #5 sekund (5000 ms) opomnika pravilnega odgovora 
			    #500 ms pavze
			exp.data.add([block.name, trial.id, key, rt])



expyriment.control.end(goodbye_text="Thank you for participating in our experiment.")