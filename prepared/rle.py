def rle_to_txt(rle_filename):
    # Generate the output filename by replacing the extension
    txt_filename = rle_filename.replace(".rle", ".txt")

    with open(rle_filename, "r") as rle_file:
        rle_lines = []
        for line in rle_file:
            if not line.startswith("#") and not line.startswith("x ="):
                rle_lines.append(line.strip())

    txt_lines = []
    max_length = 0
    for rle_line in rle_lines:
        txt_line = ""
        count = ""
        for char in rle_line:
            if char.isdigit():
                count += char
            elif char in "bo$!":
                if count == "":
                    count = "1"
                if char == "b":
                    txt_line += "0 " * int(count)
                elif char == "o":
                    txt_line += "1 " * int(count)
                elif char == "$":
                    txt_lines.append(txt_line)
                    max_length = max(max_length, len(txt_line))
                    txt_line = ""
                elif char == "!":
                    break
                count = ""
        txt_lines.append(txt_line)  # Append the last line

    # Pad shorter lines with dead cells
    txt_lines = [line.ljust(max_length, '0') for line in txt_lines]

    with open(txt_filename, "w") as txt_file:
        txt_file.write('\n'.join(txt_lines))

if __name__ == '__main__':
    rle_to_txt("../1beacon.rle")
