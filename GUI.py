import PySimpleGUI as sg
from QueryHandling.QueryProcess import processQuery
from tester import load_json
from indexer import load_index
from Matching_functions import build_vectors, query_vector, getmatches

if __name__=='__main__':
    index = load_index('indexfiles/index.json')
    Vectors = build_vectors(index)

    #Vectors = load_json('indexfiles/Vectors.json')
    layout = [[sg.Text("Enter your Query")],
              [sg.InputText(key = 'query',size=(44,5))],
              [sg.Button('GO')],
              [sg.Listbox(values=[], size=(43, 10), key='res', enable_events=True)],
              ]


    window = sg.Window("Search Engine", layout, margins=(200, 100))


    while True:
        event, values = window.read()


        if event == sg.WIN_CLOSED:
            break
        elif event == "GO":
            query=values['query']
            query = processQuery(query)
            query_terms = query.split()
            queryVector = query_vector(query_terms, index)
            val = getmatches(queryVector, Vectors)
            results = [str(x[1])+'   '+str(x[0]) for x in val]
            window['res'].update(results)
    window.close()