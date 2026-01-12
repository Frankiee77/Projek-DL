result, continuation_token = reviews(
    'com.levelinfinite.sgameGlobal',
    lang='id',
    country='id',
    sort=Sort.NEWEST,
    count=10000
)

df = pd.DataFrame(result)
df.to_csv("ulasan_hok.csv", index=False)
print("Total data mentah:", len(df))
