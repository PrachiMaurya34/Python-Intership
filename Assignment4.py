import os                             #importing os for handling file path
def read_data(files):                  #create function read data to read the files
    data = []
    for file in files:
        try:
            with open(file, 'r') as f:
                data.extend(f.readlines())
        except FileNotFoundError:              #when file is not in the system it will show filenotfound error
            print(f"Error: {file} not found.")
    return data
def process_data(data):                    #create process data fuction to calculated total feedback and rating
    entries = []
    total_rating = 0
    count = 0
    for entry in data:
        try:
            name, rest = entry.split(": ")
            rating, comment = rest.split(" - ")
            rating = int(rating)
            entries.append((name, rating, comment.strip()))
            total_rating += rating
            count += 1
        except ValueError:                          #show value error when their is mistake in the entries value
            print(f"Error processing entry: {entry.strip()}")       
    average_rating = total_rating / count if count else 0
    return entries, average_rating, count
def summary(feedback_entries, average_rating, total_entries, output_file):# create summary fuction for to write all data in a file
    with open(output_file, 'w') as f:
        f.write(f"Total Feedback Entries: {total_entries}\n")
        f.write(f"Average Rating: {average_rating:.2f}\n")
        f.write("\nFeedbacks:\n")
        for entry in feedback_entries:
            f.write(f"{entry[0]}: {entry[1]} - {entry[2]}\n")
def main():                               # for displaying the feedback total entries and rating average
    current_directory = os.path.dirname(os.path.abspath(__file__))
    files = [
        os.path.join(current_directory, 'feedback1.txt'),
        os.path.join(current_directory, 'feedback2.txt'),
        os.path.join(current_directory, 'feedback3.txt')
    ]
    data = read_data(files)
    entries, average_rating, total_entries = process_data(data)   
    summary_file = os.path.join(current_directory, 'feedback_summary.txt')
    summary(entries, average_rating, total_entries, summary_file)
    with open(summary_file, 'r') as f:
        print(f.read())
if __name__ == "__main__":
    main()
# Output
# PS C:\Users\piyu\OneDrive\Desktop\python> & "C:/Program Files/Python312/python.exe" c:/Users/piyu/OneDrive/Desktop/python/Assignment_4.py/Assignment4.py
# Total Feedback Entries: 6
# Average Rating: 3.33

# Feedbacks:
# Alice: 5 - Great service!
# Bob: 4 - Good, but could improve.
# Charlie: 3 - Average experience.
# David: 2 - Not satisfied.
# Eve: 5 - Excellent!
# Frank: 1 - Very poor service.
