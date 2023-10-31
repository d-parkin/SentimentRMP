import pandas as pd

def mergeColumns(csv1, csv2):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)

    merged_df = df1.merge(df2[['ID', 'Department']], left_on='InstructorID', right_on='ID', how='left')

    # Drop the 'ID' column, as it's no longer needed
    merged_df = merged_df.drop('ID_y', axis=1)

    df_list = merged_df.columns.tolist()
    df_list.insert(2, 'Department')
    merged_df = merged_df[df_list]

    merged_df = merged_df.to_csv('FinalTableWithDepartment.csv', index=False)

finalMapping = r"C:\Users\parki\Downloads\SentimentRMP\FinalTableRatings+Sentiment+Mapping.csv"
instructor = r"C:\Users\parki\Downloads\SentimentRMP\SentimentRMP\instructor.CSV"
# mergeColumns(finalMapping, instructor)

def addCollege(csv):
    df = pd.read_csv(csv)
    df['College'] = ''

    for index, row in df.iterrows():
        if row['Department'] in ['Art', 'Dance', 'Design', 'Film and Electronic Arts', 'Music or "Theatre Arts', 'Theater', 'Film', 'Music']:
             df.at[index, 'College'] = 'College of the Arts'
        if row['Department'] in ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management and Human Resource Management', 'Marketing']:
             df.at[index, 'College'] = 'College of Business'
        if row['Department'] in ['Advanced Studies in Education and Counseling', 'Educational Leadership', 'Liberal Studies', 'Single Subject Teacher Education', 'Teacher Education']:
             df.at[index, 'College'] = 'College of Education'
        if row['Department'] in ['Biomedical Engineering', 'Chemical Engineering', 'Civil Engineering and Construction Engineering Management', 'Computer Engineering & Computer Science', 'Teacher Education']:
             df.at[index, 'College'] = 'College of Engineering'

    df_list = df.columns.tolist()
    df_list.insert(3, 'College')
    df = df[df_list]

    df = df.to_csv('FinalTablewithDepartmentCollege.csv', index=False)
        
addCollege(r"C:\Users\parki\Downloads\SentimentRMP\FinalTableWithDepartment.csv")

