import csv

def format(input):
    # Encoding
    encodings = ['utf-8', 'utf-16', 'latin1']
    
    for encoding in encodings:
        try:
            with open(input+'.txt', 'r', encoding=encoding) as infile:
                lines = infile.readlines()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("Failed to read the file with known encodings.")
    
    with open(input+'_formatted.csv', 'w', newline='', encoding='utf-8') as outfile:
        csv_writer = csv.writer(outfile)
        
        header = ["occurence", "track_id"]
        csv_writer.writerow(header)

        for line in lines:
            # Split line yang dibatasi tab
            parts = line.split('\t')
            # Strip quotes dan whitespace
            index = parts[0].strip()
            track_id = parts[1].strip().strip('"')
            # Tulis ke csv
            csv_writer.writerow([index, track_id])

format('output/total_listen_id')