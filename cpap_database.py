def data_read_in():
    sample = open('sample_data.txt', 'r')
    sample_data = sample.read()
    sample.close()
    return sample_data


def data_manipulation(data):
    split = data.split("\n")
    N = 5
    patient_grouping = [split[i:i+N] for i in range(0, len(split), N)]
    return patient_grouping


def data_calculations(data):
    for i in range(len(data)):
        if len(data[i]) == 5:
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


if __name__ == '__main__':
    data = data_read_in()
    patients = data_manipulation(data)
    averages = data_calculations(patients)
    print(averages)
