def data_read_in():
    sample = open('sample_data.txt', 'r')
    sample_data = sample.read()
    sample.close()
    return sample_data


def data_manipulation(data):
    split = data.split("\n")
    N = 5
    patient_group = [split[i:i+N] for i in range(0, len(split), N)]
    patient_group = patient_group[0:-2] # Deleting 'END' array item
    for x in range(len(patient_group)):
        patient_group[x][1] = float(patient_group[x][1]) # Changing hours of sleep to float

        seal = patient_group[x][2].split(',') # Formatting mask leakage data
        seal.remove('Seal')
        for y in range(len(seal)):
            seal[y] = float(seal[y])
        patient_group[x][2] = seal

        event = patient_group[x][3].split(',') # Formatting events data
        event.remove('Events')
        for y in range(len(event)):
            event[y] = int(event[y])
        patient_group[x][3] = event

        O2 = patient_group[x][4].split(',') # Formatting O2 data
        O2.remove('O2')
        for y in range(len(O2)):
            O2[y] = int(O2[y])
        patient_group[x][4] = O2

    return patient_group


def data_calculations(data):
    for i in range(len(data)):
        s_total = 0
        e_total = 0
        seals = data[i][2].split(',')
        seals.remove('Seal')
        for x in range(len(seals)):
            seals[x] = float(seals[x])
            s_total += seals[x]
        seal_avg = s_total/len(seals)
        seal_avg = round(seal_avg, 1)
        data[i].append(seal_avg)

        events = data[i][3].split(',')
        events.remove('Events')
        for y in range(len(events)):
            events[y] = float(events[y])
            e_total += events[y]
        events_avg = e_total/len(events)
        events_avg = round(events_avg, 1)
        data[i].append(events_avg)
    return data


'''def diagnoses(data):
    for i in range(len(data)):
        if len(data[i]) == 5:'''
    

if __name__ == '__main__':
    data = data_read_in()
    patients = data_manipulation(data)
    print(patients)
    
