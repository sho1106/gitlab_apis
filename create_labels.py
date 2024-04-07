import pandas as pd
import gitlab


def loadCSV(filename):
    return pd.read_csv(filename)

def connect():
    return gitlab.Gitlab.from_config()

def get_group(gl, group_name):
    return gl.groups.get(group_name)

def add_label(gl_api, label_info):
    try:
        gl_api.labels.create()

if __name__ == '__main__':
    

    filename = "test.csv"
    labels = loadCSV(filename)
    print(labels)
    
    
    