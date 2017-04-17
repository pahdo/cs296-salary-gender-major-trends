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
        if not income_list or not major_list:
            continue
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
    old_cols = ['Fall', 'College', 'Major Name', 'Total', 'Male', 'Female', 'P75th']
    new_cols = ['Year', 'College', 'Major', 'Total', 'Male', 'Female', 'Salary75']
    years = [2005, 2015]
    for year in years:
        generate_conbined_csv(dumbdict, year, 'temp{}.csv'.format(year))
        select_cols('temp{}.csv'.format(year), 'uiuc_major_salary{}.csv'.format(year), old_cols, new_cols)


def squeezedata():
    df = pd.read_csv("uiuc_major_salary.csv")
    df2005 = df[df['Year'] == 2005]
    df2015 = df[df['Year'] == 2015]
    df2005 = df2005[df2005['Major'].isin(list(df2015['Major']))]
    df2015 = df2015[df2015['Major'].isin(list(df2005['Major']))]
    df_new = []
    df_new_cols = ['College', 'Major', 'Total2005', 'Male2005', 'Female2005',
    'Salary75', 'Total2015', 'Male2015', 'Female2015']
    for index, row_2005 in df2005.iterrows():
        row_2015 = df2015[df2015['Major'] == row_2005['Major']]
        new_col = [row_2005['College'], row_2005['Major'], row_2005['Total'],
        row_2005['Male'], row_2005['Female'], row_2005['Salary75'], row_2015['Total'].values[0],
        row_2015['Male'].values[0], row_2015['Female'].values[0]]
        df_new.append(new_col)
    df = pd.DataFrame.from_records(df_new, columns=df_new_cols)
    df.to_csv("uiuc_together.csv", index=False)


if __name__ == '__main__':
    dumbdict = {'Agr & Environmental Cmc & Educ': 'ENVIRONMENTAL ENGINEERING',
                'Animal Sciences': 'ANIMAL SCIENCES',
                'Crop Sciences': 'PLANT SCIENCE AND AGRONOMY',
                'Food Science & Human Nutrition': 'FOOD SCIENCE',
                'Human Development & Family St': 'FAMILY AND CONSUMER SCIENCES',
                'Intl, Resource, Consumer Econ': 'AGRICULTURAL ECONOMICS',
                'Natural Resrcs & Environ Sci': 'ENVIRONMENTAL SCIENCE',
                'Technical Systems Management': 'MANAGEMENT INFORMATION SYSTEMS AND STATISTICS',
                'Accountancy': 'ACCOUNTING',
                'Finance': 'FINANCE',
                'Marketing': 'MARKETING AND MARKETING RESEARCH',
                'Elementary Education': 'ELEMENTARY EDUCATION',
                'Special Education': 'SPECIAL NEEDS EDUCATION',
                'Aerospace Engineering': 'AEROSPACE ENGINEERING',
                'Bioengineering' : 'BIOMEDICAL ENGINEERING',
                'Civil Engineering': 'CIVIL ENGINEERING', 'Computer Engineering': 'COMPUTER ENGINEERING', 'Computer Science': 'COMPUTER SCIENCE', 'Electrical Engineering': 'ELECTRICAL ENGINEERING',
'Engineering Mechanics': 'ENGINEERING MECHANICS PHYSICS AND SCIENCE', 'Engineering Physics': 'ENGINEERING MECHANICS PHYSICS AND SCIENCE', 'General Engineering': 'GENERAL ENGINEERING', 'Industrial Engineering': 'ENGINEERING AND INDUSTRIAL MANAGEMENT', 'Materials Science & Engr': 'MATERIALS ENGINEERING AND MATERIALS SCIENCE', 'Mechanical Engineering': 'MECHANICAL ENGINEERING', 'Nuclear, Plasma, Radiolgc Engr': 'NUCLEAR, INDUSTRIAL RADIOLOGY, AND BIOLOGICAL TECHNOLOGIES', 'Architectural Studies': 'ARCHITECTURE', 'Industrial Design': 'STUDIO ARTS', 'Music Education': 'ART AND MUSIC EDUCATION', 'Advertising': 'ADVERTISING AND PUBLIC RELATIONS', 'Journalism': 'JOURNALISM', 'Actuarial Science': 'ACTUARIAL SCIENCE', 'Biochemistry': 'BIOCHEMICAL SCIENCES', 'Chemical Engineering': 'CHEMICAL ENGINEERING', 'Chemistry': 'CHEMISTRY', 'Communication': 'COMMUNICATIONS', 'Earth, Soc, Env Sustainability': 'GEOLOGY AND EARTH SCIENCE', 'Economics': 'ECONOMICS', 'English': 'ENGLISH LANGUAGE AND LITERATURE', 'Global Studies': 'INTERNATIONAL RELATIONS', 'History': 'HISTORY', 'Integrative Biology': 'BIOLOGY', 'Math & Computer Science': 'MATHEMATICS AND COMPUTER SCIENCE', 'Mathematics': 'MATHEMATICS', 'Molecular and Cellular Biology': 'MOLECULAR BIOLOGY', 'Physics': 'PHYSICS', 'Political Science': 'POLITICAL SCIENCE AND GOVERNMENT', 'Psychology': 'PSYCHOLOGY', 'Sociology': 'SOCIOLOGY', 'Statistics': 'STATISTICS AND DECISION SCIENCE', 'Statistics & Computer Science': 'MANAGEMENT INFORMATION SYSTEMS AND STATISTICS', 'Community Health': 'COMMUNITY AND PUBLIC HEALTH', 'Interdisciplinary Health Sci': 'GENERAL MEDICAL AND HEALTH SERVICES', 'Kinesiology': 'TREATMENT THERAPY PROFESSIONS', 'Recreation, Sport, and Tourism': 'PHYSICAL FITNESS PARKS RECREATION AND LEISURE', 'Speech & Hearing Science': 'COMMUNICATION DISORDERS SCIENCES AND SERVICES', 'Social Work': 'SOCIAL WORK'}
    # clean(dumbdict)
    df = pd.read_csv("uiuc_together.csv")
    df['TotalIncr'] = df['Total2015'] - df['Total2005']
    df['MaleIncr'] = df['Male2015'] - df['Male2005']
    df['FemaleIncr'] = df['Female2015'] - df['Female2005']

    df['TotalIncrPer'] = df['TotalIncr'] / df['Total2005']
    df['MaleIncrPer'] = df['MaleIncr'] / df['Male2005']
    df['FemaleIncrPer'] = df['FemaleIncr'] / df['Female2005']
    #Horray we don't have NANs

    df = df.sort_values('Salary75', ascending = False)

    df.to_csv("uiuc_pretty.csv", index= False)
