import pandas as pd


def get_major_names():
    df_majors = pd.read_csv("uiuc_demographics_undergrad.csv")
    df_income = pd.read_csv("income_majors_undergrad.csv")
    print "Majors"
    print df_majors['Major Name'].unique()
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print df_income['Major'].unique()


def generate_conbined_csv(map_major_income, year, name):
    df_majors = pd.read_csv("uiuc_demographics_undergrad.csv")
    df_income = pd.read_csv("income_majors_undergrad.csv")
    df_major_year = df_majors[df_majors['Fall'] == year]
    income_names = df_income.columns.tolist()
    major_names = df_major_year.columns.tolist()
    names_new = major_names + income_names
    df_new = []
    for key, value in map_major_income.iteritems():
        income_list = df_income[df_income['Major'] == value].values.tolist()
        major_list = df_major_year[df_major_year['Major Name'] == key].values.tolist()
        major_list = major_list[0] + income_list[0]
        df_new.append(major_list)
    df = pd.DataFrame.from_records(df_new, columns=names_new)
    df.to_csv(name, index=False)


def select_cols(name, new_name, old_cols, new_cols):
    df = pd.read_csv(name)
    df = df[old_cols]
    df.columns = [new_cols]
    df.to_csv(new_name, index=False)


def clean(map_major_income):
    old_cols = ['Fall', 'College', 'Major Name', 'Total', 'Male', 'Female', 'Rank', 'P75th']
    new_cols = ['Year', 'College', 'Major', 'Total', 'Male', 'Female', 'Rank', 'Salary75']
    years = [2005, 2015]
    for year in years:
        generate_conbined_csv(dumbdict, year, 'temp{}.csv'.format(year))
        select_cols('temp{}.csv'.format(year), 'uiuc_major_salary', old_cols, new_cols)


if __name__ == '__main__':
    dumbdict = {'Animal Sciences': 'MECHANICAL ENGINEERING', 'Technical Systems Management':
        'INDUSTRIAL AND MANUFACTURING ENGINEERING', 'Early Childhood Education': 'OPERATIONS LOGISTICS AND E-COMMERCE'}
    clean(dumbdict)
