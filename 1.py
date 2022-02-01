with open('input.txt', 'r') as input:
    with open('output.txt', 'w') as output:
        output_str = ''
        for line in input:
            if sum([abs(float(i)) for i in line.split()]) > 750:
                output_str += '2\n'
            else:
                output_str += '1\n'
        output.write(output_str)

    
