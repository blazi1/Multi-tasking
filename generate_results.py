#After all the subject have completed the experiment, a file with their results is created. 


import os, csv

def get_data():
    results = dict() 
    """ sex, 
        age, 
        average response time for the first two blocks (congruent vs. incongruent), 
        average reponse time for the third block while repeating (congruent vs. incongruent), 
        average response time for the third block while switching (congruent vs. incongruent),
        error rate for the first two blocks (congruent vs. incongruent),
        error rate for the third block while repeating (congruent vs. incongruent),
        error rate for the third block while switching (congruent vs. incongruent)"""
    subjects = []

    average_response_first_two_blocks_cong = 0
    average_response_switch = 0
    average_response_repeat_cong = 0
    average_response_repeat_incong = 0

    path = os.getcwd() + '/data/'
    for filename in os.listdir(path):
        if filename.endswith('.xpd'):
            with open(os.path.join(path, filename)) as f:
                number_first_two_blocks_cong = 0
                number_first_two_blocks_incong = 0
                number_response_switch_cong = 0
                number_response_switch_incong = 0
                number_response_repeat_cong = 0
                number_response_repeat_incong = 0

                counter_first_two_blocks_cong = 0
                counter_first_two_blocks_incong = 0
                counter_response_switch_cong = 0
                counter_response_switch_incong = 0
                counter_response_repeat_cong = 0
                counter_response_repeat_incong = 0

                previous_response = ""
                previous_trial = ""
                for line in f:
                    if not (line.startswith("#") or line.startswith("subject_id")): 
                        reader = csv.reader(line.splitlines())
                        this_line = next(reader)
                        if this_line[0] not in results:
                            results[this_line[0]] = [this_line[3], this_line[4], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                            subjects.append(this_line[0])
                        if this_line[7] == "CORRECT":
                            if this_line[1] == "3":
                                if this_line[9] == "False":
                                    if this_line[8] == "False": 
                                        counter_response_repeat_incong += 1  #response_repeat_incong
                                    else:
                                        counter_response_switch_incong += 1 #response_switch_incong
                                else:
                                    if this_line[8] == "False":
                                        counter_response_repeat_cong += 1 #response_repeat_cong 
                                    else:
                                        counter_response_switch_cong += 1 #response_switch_cong
                            else:
                                if this_line[9] == "False":
                                    counter_first_two_blocks_incong += 1 #first_two_blocks_incong
                                else:
                                    counter_first_two_blocks_cong += 1 #first_two_blocks_cong
                        if this_line[1] == previous_trial and previous_response == "CORRECT" and this_line[7] == "CORRECT":
                            if this_line[1] == "3":
                                if len(this_line) >= 9 and this_line[8] == "False":
                                    if this_line[9] == "True":
                                        results[this_line[0]][4] += int(this_line[6])
                                        number_response_repeat_cong += 1 
                                    else:
                                        results[this_line[0]][5] += int(this_line[6])
                                        number_response_repeat_incong += 1
                                elif len(this_line) >= 9 and this_line[8] == "True":
                                    if this_line[9] == "True":
                                        results[this_line[0]][6] += int(this_line[6])  
                                        number_response_switch_cong += 1 
                                    else:
                                        results[this_line[0]][7] += int(this_line[6])
                                        number_response_switch_incong += 1
                            else:
                                if this_line[9] == "True":
                                    results[this_line[0]][2] += int(this_line[6])
                                    number_first_two_blocks_cong += 1
                                else:
                                    results[this_line[0]][3] += int(this_line[6])
                                    number_first_two_blocks_incong += 1
                        elif this_line[7] == "WRONG":
                            if this_line[1] == "3":
                                if this_line[9] == "False":
                                    if this_line[8] == "False": 
                                        results[this_line[0]][8] += 1  #wrong_response_repeat_incong
                                        counter_response_repeat_incong += 1
                                    else:
                                        results[this_line[0]][9] += 1 #wrong_response_switch_incong
                                        counter_response_switch_incong += 1
                                else:
                                    if this_line[8] == "False":
                                        results[this_line[0]][10] += 1 #wrong_response_repeat_cong
                                        counter_response_repeat_cong += 1 
                                    else:
                                        results[this_line[0]][11] += 1 #wrong_response_switch_cong
                                        counter_response_switch_cong += 1
                            else:
                                if this_line[9] == "False":
                                    results[this_line[0]][12] += 1 #wrong_first_two_blocks_incong
                                    counter_first_two_blocks_incong += 1
                                else:
                                    results[this_line[0]][13] += 1 #wrong_first_two_blocks_cong
                                    counter_first_two_blocks_cong += 1
                        previous_response = this_line[7]
                        previous_trial = this_line[1]
                if number_first_two_blocks_cong != 0:
                    results[subjects[-1]][2] //= number_first_two_blocks_cong
                if number_first_two_blocks_incong != 0:
                    results[subjects[-1]][3] //= number_first_two_blocks_incong
                if number_response_repeat_cong != 0:
                    results[subjects[-1]][4] //= number_response_repeat_cong
                if number_response_repeat_incong != 0:
                    results[subjects[-1]][5] //= number_response_repeat_incong
                if number_response_switch_cong != 0:
                    results[subjects[-1]][6] //= number_response_switch_cong
                if number_response_switch_incong != 0:
                    results[subjects[-1]][7] //= number_response_switch_incong 
                    print(number_response_switch_incong)
                if number_response_repeat_incong != 0:
                    results[subjects[-1]][8] /= counter_response_repeat_incong
                if number_response_switch_incong != 0:
                    results[subjects[-1]][9] /= counter_response_switch_incong
                if number_response_repeat_cong != 0:
                    results[subjects[-1]][10] /= counter_response_repeat_cong
                if number_response_switch_cong != 0:
                    results[subjects[-1]][11] /= counter_response_switch_cong
                if number_first_two_blocks_incong != 0:
                    results[subjects[-1]][12] /= counter_first_two_blocks_incong
                if number_first_two_blocks_cong != 0:
                    results[subjects[-1]][13] /= counter_first_two_blocks_cong

    return results

