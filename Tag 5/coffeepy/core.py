
gpcr183 = "GPCR183.fasta"
aac = pd.read_csv("amino_acid_properties.csv")
hydrophobicity = aac.pop("hydropathy index (Kyte-Doolittle method)")
onelcode = aac.pop("1-letter code")

with open(gpcr183) as gpcr:
    whole_seq = "" 
    for line in gpcr:
        if not line.startswith(">"):
            whole_seq += line.replace("\n", "")

def listcreator(data):
    lis = list()
    for i in range(0, len(data)):
        lis.append(data[i])
        i += 1
    return lis

list_hyd = listcreator(hydrophobicity)
one_letterc = listcreator(onelcode)

def convert(lis1, lis2):
    dict = {}
    for i in range(0, len(lis1)):
        dict.update({lis1[i]: lis2[i]})
        i += 1
    return dict

mapping_dict = convert(one_letterc, list_hyd)

def matcher(seq, hyd):
    matches = list()
    for item in seq:
        matches.append(hyd.get(item))
    return matches

hyd_seq_list = matcher(whole_seq, mapping_dict)

def slidingwindow(beginning, end):
    sliding_window = hyd_seq_list[beginning : end]
    add = 0
    for element in sliding_window:
        add += element
    data = [go.Bar(y=hyd_seq_list[beginning : end])]
    fig = go.Figure(data=data)
    fig.update_layout(template="plotly_dark", title="Sliding window:" + 
                      str(beginning) + "-" + 
                      str(end) + " " +
                     "average hydropathy" + 
                      "=" + 
                      str(add / len(sliding_window)))
    fig.update_xaxes(title_text="Amino acid position")
    fig.update_yaxes(title_text="Hydrophaty")
    fig.show()
    
slidingwindow(10, 20)
slidingwindow(30, 300)
slidingwindow(0, 360)

def find_peaks(list_of_intensities):
    peaks = []
    for pos, current_peak in enumerate(list_of_intensities[:-1]):
        if pos == 0:
            continue
        if list_of_intensities[pos - 1] < current_peak > list_of_intensities[pos + 1]:
            peaks.append(current_peak)
    return peaks
