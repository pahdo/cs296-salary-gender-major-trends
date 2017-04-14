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
    clean(dumbdict)
