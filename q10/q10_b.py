import os
import re
from q10_a import func

def finding_words():
    filenames = os.listdir()
    pattern = re.compile(r'^[a-zA-Z]\.txt$')
    filtered_names = [filename for filename in filenames if pattern.match(filename)]
    for file in filtered_names:
        file_path = os.path.join(os.getcwd(), file)
        func(file_path, "sorted_"+file)
finding_words()
