from ast import literal_evaldef extract_grid_site(line):    """Support funtion for get_grid_sites."""        line = line.rstrip()    site_key = line.split("=")[0].strip()    aas = literal_eval(line.split("=")[1].strip())        for aa in aas:        aa[0] = int(aa[0])            return (site_key, aas)def get_grid_sites(grid_result_file, ncav):    """Extracts the binding sites from the file predicted in the grid analysis."""        isresult = 0    sites_dict = {}    for line in open(grid_result_file, "r"):        line = line.rstrip()                if line == "[RESULTS.RESIDUES]":            isresult = 1            continue        if isresult == 0:            continue        if line == "[RESULTS.FREQUENCY.KAA.RESIDUES]" or not ncav:            break                        site_key, aas = extract_grid_site(line)        sites_dict[site_key] = aas        ncav -= 1            return(sites_dict)