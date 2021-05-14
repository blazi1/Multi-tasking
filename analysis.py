#After each subject complets the experiment, a file with their results is created. 

import os, csv

results = dict() # sex, age, average response time for the first two blocks, average response time for the third block while switching, average reponse time for the third block while repeating
subjects = []

average_response_first_two_blocks = 0
average_response_switch = 0
average_response_repeat = 0

path = os.getcwd() + '/data/'
for filename in os.listdir(path):
    if filename.endswith('.xpd'):
        with open(os.path.join(path, filename)) as f:
            number_first_two_blocks = 0
            number_response_switch = 0
            number_response_repeat = 0
            previous_response = ""
            previous_trial = ""
            for line in f:
                if not (line.startswith("#") or line.startswith("subject_id")): 
                    reader = csv.reader(line.splitlines())
                    this_line = next(reader)
                    if this_line[0] not in results:
                        results[this_line[0]] = [this_line[3], this_line[4], 0, 0, 0]
                        subjects.append(this_line[0])
                    if this_line[1] == previous_trial and previous_response == "CORRECT" and this_line[7] == "CORRECT":
                        if this_line[1] == "3":
                            print(this_line)
                            if len(this_line) >= 9 and this_line[8] == "True":
                                results[this_line[0]][3] += int(this_line[6])
                                number_response_switch += 1 
                            elif len(this_line) >= 9 and this_line[8] == "False":
                                results[this_line[0]][4] += int(this_line[6])  
                                number_response_repeat += 1 
                        else:
                            results[this_line[0]][2] += int(this_line[6])
                            number_first_two_blocks += 1
                    previous_response = this_line[7]
                    previous_trial = this_line[1]
            if number_first_two_blocks != 0:
                results[subjects[-1]][2] /= number_first_two_blocks
            if number_response_switch != 0:
                results[subjects[-1]][3] /= number_response_switch
            if number_response_repeat != 0:
                results[subjects[-1]][4] /= number_response_repeat
print(results)

