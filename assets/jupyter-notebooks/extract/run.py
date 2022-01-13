import os
def change_jupyter_to_html(file):
    os.system(f'jupyter nbconvert --to html {file}')

def get_body(str):
    if "<body" in str or "body>" in str: 
        return True
    else:
        return False

def extract_body_from_html(html_file):
    with open(html_file,'r') as  f:
        lines = f.readlines()
        index_lines = [x for x in lines if get_body(x)]
        if len(index_lines) == 2:
            start_index = lines.index(index_lines[0])
            last_index = lines.index(index_lines[1])
            body_lines = lines[start_index:last_index+1]
        else:
            print('error')
            body_lines = []

    header = [  "---\n",\
                "layout: notebook-html\n",\
                "---\n"]

    with open(html_file, 'w') as f:
        if body_lines:
            f.writelines(header)
            f.writelines(body_lines)

cur_dir = os.path.dirname(os.path.abspath(__file__))
file_list = os.listdir(cur_dir)
print(file_list)
for file in file_list:
    if ".ipynb" in file:
        file = f'{cur_dir}/{file}'
        change_jupyter_to_html(file)
        html_file = file.replace('.ipynb','.html')
        extract_body_from_html(html_file)
