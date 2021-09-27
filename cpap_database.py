import json


def data_read_in(filename):
    """Read in patient data from CPAP sample file

    A CPAP machine, or continuous positive airway pressure machine,
    is a device used to treat sleep apnea.  Sleep apnea is a condition
    in which blocked airways cause patients to wake up from sleep
    multiple time throughout the night.  More info on CPAP machines and
    sleep apnea can be found at:
    https://www.webmd.com/sleep-disorders/sleep-apnea/features/cpap-machine#1

    :returns: string containing all CPAP info from input file
    """
    sample = open(filename, 'r')
    sample_data = sample.read()
    sample.close()
    return sample_data


def data_split(data):
    """Split input text string into patient list items

    The input data is split by line return characters first to sort the data
    back into its respective line entries, then every group of five lines is
    grouped together in one nested list item to represent the data and info
    from one patient.

    :param data: string containing all patient CPAP info

    :returns: list of lists containing grouped patient data
    """
    split = data.split("\n")
    N = 5
    patient_group = [split[i:i+N] for i in range(0, len(split), N)]
    patient_group = patient_group[0:-1]  # Deleting 'END' list item
    return patient_group


def data_manipulation(patient_group):
    """Manipulate patient list data to become more operable

    The input list of patient data is modified to delete strings from lists
    of numerical data to later perform iterative operations on those lists.

    :param patient_group: list of lists containing grouped patient data

    :returns: list of lists with explicitly string or numerical data
    """
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
    """Calculate mask seal leakage average and nightly event average

    The input data is analyzed to calculate the mask seal leakage average
    throughout the night as well as the nightly "event" average.  A sleep
    apnea event is characterized by a sudden state of wakefulness during
    the night due to lack of airflow while asleep.

    :param patient_data: list of patient data manipulated for calculations

    :returns: list containing patient data with appended seal leakage average
              and nightly event average
    """
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
    """Diagnose patients based off O2 values and event averages

    The calculated patient data is considered to diagnose each patient
    with either normal sleep, apnea, hypoxia, or hypoxia apnea.  Normal
    sleep is defined as having all hourly O2 values above 93 and having
    less than or equal to 5 average events per night.  Apnea is defined by
    all hourly O2 values above 93 but more than 5 average events per night.
    Hypoxia is defined as any O2 values below 93 but less than or equal to
    5 average events per night.  Hypoxia apnea is defined by any O2 value
    below 93 and more than 5 average events per night.

    :param calcs: list of patient data containing appended calculated averages

    :returns: list of patient data containing appended patient sleep diagnosis
    """
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
    """Organize patient info into dictionaries

    Each set of patient data is taken and more clearly organized
    into a list of dictionaries that make the data more readable
    and easier to navigate.

    :param full_info: list of patient data containing all given and
                      calculated information

    :returns: list of dictionaries of all patient data
    """
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
    """Output patient data to individual json files

    Each patient's dictionary of full information is compiled and
    output to an individual json file with their given first and
    last name.

    :param dictionary_list: list of dictionaries of full patient data

    :returns: json files of patient info to local disk
    """
    for i in range(len(dictionary_list)):
        out_file = open("{}-{}.json".format(dictionary_list[i]['First Name'],
                                            dictionary_list[i]['Last Name']),
                        'w')
        json.dump(dictionary_list[i], out_file)
        out_file.close()


if __name__ == '__main__':
    data = data_read_in("sample_data.txt")
    patients = data_split(data)
    type_convert = data_manipulation(patients)
    calc = data_calculations(type_convert)
    diagnosed = diagnoses(calc)
    dict_list = dictionaries(diagnosed)
    output_json(dict_list)
