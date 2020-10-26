"""Query Wikidata for Belgian politicians"""

import argparse
from datetime import datetime as dt

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?magasin ?magasinLabel ?magasinAddress WHERE {
        ?magasin wdt: P31 wd:Q293431.
        ?magasin wdt: 131 wd: 239 .
        ?magasin wdt: P625 ?magasinAddress.
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    }
    ORDER BY ?magasinLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Magasins trouvés\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n magasins (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    if name_filter:
        rows = [row for row in rows if name_filter in row['magasinLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            magasinLabel = dt.strptime(row['magasinLabel']['value'], date_format)
        except ValueError:
            magasinlabel = "????"
        try:
            magasinAddress = dt.strptime(row['magasinAddress']['value'], date_format)
          
        except ValueError: 
            magasinAddress = "????"
        print(f"{row['magasinLabel']['value']}")

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)
