import argparse
from pathlib import Path
import pandas as pd
from evaluate import evaluate

RELATIONS = {
    "CountryBordersWithCountry",
    "RiverBasinsCountry",
    "PersonLanguage",
    "PersonProfession",
    "PersonInstrument"
}

def your_solution(relation: str, input_csv: Path):
    '''
    Implement your solution here. Please add comments wherever possible!!
    
    Read the csv file, get the subject_entity and relations to form your own prompt. Use the object_entity column for corresponding labels. For a given subject_entity and relation pair, multiple labels are possible!!
    
    return: dataframe with columns names as ['SubjectEntity', 'Relation', 'ObjectEntity'], where 'ObjectEntity' are the generations using your solution.
    '''
    
    output_df = pd.DataFrame(columns=['SubjectEntity', 'Relation', 'ObjectEntity'])
    
    return output_df 


def main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "--input_dir",
        type=str,
        default="./dataset/test/",
    )
    
    parser.add_argument(
        "--output_dir",
        type=str,
        default="./baseline/",
        help="output directory to store the baseline output",
    )
    
    args = parser.parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    print(args)
    
    for relation in RELATIONS:
        input_csv = input_dir / f"{relation}.csv"
        output_df = your_solution(relation, input_csv)
        output_df.to_csv(output_dir / f"{relation}.csv", index=False)
    
    ### call the evaluate function to check your scores!
    input_dir = output_dir ### the outputs saved by your solution becomes the input directory for the evaluate function
    ground_truth_dir = Path("./test/")
    results_dir = Path("./results/") ### change based on your needs
    evaluate(input_dir, ground_truth_dir, results_dir)
    
if __name__ == '__main__':
    main()