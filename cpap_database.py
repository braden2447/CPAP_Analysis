def data_read_in():
    sample = open('sample_data.txt', 'r')
    sample_data = sample.read()
    sample.close
    return sample_data


if __name__ == '__main__':
    data = data_read_in()
    print(data)
