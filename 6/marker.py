input1_datastream = open('input.txt').read()
test = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

def find_marker_in_datastream(datastream):
    marker_pos = 1
    dif_char_needed = 14 # Set to 4 for part 1
    processed_datastream = []
    for char in datastream:
        processed_datastream.append(char)
        if len(set(processed_datastream)) == dif_char_needed:
            return marker_pos
        elif(len(processed_datastream) >= dif_char_needed):
            processed_datastream.pop(0)
        marker_pos+=1
    

for test_datastream in test:
    print(test_datastream)
    print(find_marker_in_datastream(test_datastream))

print("Full Input Data")
print(input1_datastream)
print(find_marker_in_datastream(input1_datastream))