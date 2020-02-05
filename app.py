import fileinput
import sys

def process(source, destination, a_calling_no, b_calling_no):
    cron_no = 1

    with open(destination, "a+") as f:
        for line in fileinput.input(source):
            pipe_position = [n for n,x in enumerate(line) if x=='|']

            cron_no_start_position = pipe_position[1] + 1
            a_calling_no_position = pipe_position[2] + 1
            b_calling_no_position = pipe_position[4] + 1

            cron_no_str = prepare_value(cron_no_start_position, pipe_position[2] - 1, cron_no)
            a_calling_no = prepare_value(a_calling_no_position, pipe_position[3] - 1, a_calling_no)
            b_calling_no = prepare_value(b_calling_no_position, pipe_position[5] - 1, b_calling_no)

            row = line[:cron_no_start_position] + cron_no_str + line[cron_no_start_position + cron_no_str.__len__():]   
            row = row[:a_calling_no_position] + a_calling_no + row[a_calling_no_position + a_calling_no.__len__():]   
            row = row[:b_calling_no_position] + b_calling_no + row[b_calling_no_position + b_calling_no.__len__():]   

            f.writelines(row)
            cron_no += 1

    fileinput.close()

def prepare_value(start_position, end_position, value):
    value = str(value)
    length = end_position - start_position - 1
    return value.ljust(length, ' ')

def main(args):
    process(*args)

if __name__ == '__main__':
    main(sys.argv[1:])
