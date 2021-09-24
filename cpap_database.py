import json


def data_read_in():
    sample = open('sample_data.txt', 'r')
    sample_data = sample.read()
    sample.close()
    return sample_data


def data_split(data):
    split = data.split("\n")
    N = 5
    patient_group = [split[i:i+N] for i in range(0, len(split), N)]
    patient_group = patient_group[0:-2]  # Deleting 'END' array item
    return patient_group


def data_manipulation(patient_group):
    for x in range(len(patient_group)):
        patient_group[x][1] = float(patient_group[x][1])
        # Changing hours of sleep to float

        seal = patient_group[x][2].split(',')  # Formatting mask leakage data
        seal.remove('Seal')
        for y in range(len(seal)):
            seal[y] = float(seal[y])
        patient_group[x][2] = seal

        event = patient_group[x][3].split(',')  # Formatting events data
        event.remove('Events')
        for y in range(len(event)):
            event[y] = int(event[y])
        patient_group[x][3] = event

        O2 = patient_group[x][4].split(',')  # Formatting O2 data
        O2.remove('O2')
        for y in range(len(O2)):
            O2[y] = int(O2[y])
        patient_group[x][4] = O2

    return patient_group


def data_calculations(patient_data):
    for i in range(len(patient_data)):
        seal_tot = 0
        for x in range(len(patient_data[i][2])):  # Seal avg calculations
            seal_tot += patient_data[i][2][x]
        seal_avg = seal_tot / len(patient_data[i][2])
        seal_avg = round(seal_avg, 1)
        patient_data[i].append(seal_avg)

        event_tot = 0
        for x in range(len(patient_data[i][3])):  # Event avg calculations
            event_tot += patient_data[i][3][x]
        event_avg = event_tot / len(patient_data[i][3])
        event_avg = round(event_avg, 1)
        patient_data[i].append(event_avg)

    return patient_data


def diagnoses(calcs):
    for i in range(len(calcs)):
        if calcs[i][6] > 5:
            if all(x >= 93 for x in calcs[i][4]):
                calcs[i].append('apnea')
            else:
                calcs[i].append('hypoxia apnea')
        else:
            if all(x >= 93 for x in calcs[i][4]):
                calcs[i].append('normal sleep')
            else:
                calcs[i].append('hypoxia')
    return calcs


def dictionaries(full_info):
    dict_list = []
    for i in range(len(full_info)):
        name = []
        name = full_info[i][0].split(' ')
        dict_list.append({'First Name': name[0],
                          'Last Name': name[1],
                          'Hours': full_info[i][1],
                          'Seal': full_info[i][2],
                          'Events': full_info[i][3],
                          'O2': full_info[i][4],
                          'Seal Average': full_info[i][5],
                          'Diagnosis': full_info[i][7]
                          })
    return dict_list


def output_json(dictionary_list):
    for i in range(len(dictionary_list)):
        out_file = open("{}-{}.json".format(dictionary_list[i]['First Name'],
                                            dictionary_list[i]['Last Name']),
                        'w')
        json.dump(dictionary_list[i], out_file)
        out_file.close()


if __name__ == '__main__':
    data = data_read_in()
    patients = data_split(data)
    type_convert = data_manipulation(patients)
    calc = data_calculations(type_convert)
    diagnosed = diagnoses(calc)
    dict_list = dictionaries(diagnosed)
    output_json(dict_list)
