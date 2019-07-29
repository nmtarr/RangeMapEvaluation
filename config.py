#NOTE! this is overwritten by some notebooks, so update everywhere, if adding lines.
sp_id = 'bwewax0'
summary_name = 'wormie'
gbif_req_id = 'GBIFr16'
gbif_filter_id = 'GBIFf4'
ebird_req_id = None
ebird_filter_id = None
evaluation = 'eval_gbif1'
workDir = '/Users/nmtarr/Documents/RANGES/'
codeDir = '/Users/nmtarr/Code/GAP-range-evaluation/'
inDir = workDir + 'Inputs/'
outDir = workDir + 'Outputs/'
default_coordUncertainty = 500
SRID_dict = {'WGS84': 4326, 'AlbersNAD83': 102008} # Used in file names for output.
spdb = outDir + sp_id + gbif_req_id + gbif_filter_id + '.sqlite'