import json

def merge_json_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    merged_data = data1 + data2

    with open(output_file, 'w') as outfile:
        json.dump(merged_data, outfile, indent=4)

merge_json_files('file1.json', 'file2.json', 'merged.json')
