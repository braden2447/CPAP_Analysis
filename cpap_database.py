def data_read_in():
    sample = open('sample_data.txt', 'r')
    sample_data = sample.read()
    sample.close()
    return sample_data


def data_manipulation(data):
    split = data.split("\n")
    N = 5
    patient_grouping = [split[i:i+N] for i in range(0, len(split), N)]
    patient_grouping
    return patient_grouping


if __name__ == '__main__':
    data = data_read_in()
    patients = data_manipulation(data)
