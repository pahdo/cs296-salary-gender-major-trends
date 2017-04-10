import pandas as pd

# df = pd.read_csv("bslike.csv")
# df_new = df[['Fall', 'College', 'Major Name', 'Total', 'Male', 'Female']].copy()
# df_major = df_new.groupby(['Fall', 'College', 'Major Name'])
# df_res = df_major[["Total", "Male", "Female"]].aggregate(pd.np.sum)
# df_res.to_csv("bsmajors.csv")
df = pd.read_csv("bsmajors.csv")