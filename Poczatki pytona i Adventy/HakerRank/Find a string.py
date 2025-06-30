def count_substring(string, sub_string):
    count = 0
    for i in range(count, len(string)):
        print(len(string))
            if string != sub_string:
            count += 1
        #print(str(i))
        #print(len(string))

    return i


if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'

    count = count_substring(string, sub_string)
    print(count)