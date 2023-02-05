from datetime import datetime as dt
import pytz

# kld_tz = pytz.timezone("Europe/Kyiv")

post = "{}\n{}".format(
    dt.now(tz=pytz.UTC).strftime('%Y-%m-%d %H:%M:%S %Z%z'),
    "Очень важный документ"
)

print(post)

doc = open("post.txt", "w+", encoding="utf-8")
doc.write(post)
doc.close()
