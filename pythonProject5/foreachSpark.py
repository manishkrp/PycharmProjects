# This pyspark program using python prints only
# those elements who qualify for "foreach()" condition
from pyspark import SparkContext
sc = SparkContext("local","foreach")
words = sc.serialize(
    [
        "Colony",
        "Mohalla",
        "Basti",
        "Village"
        "Mansion"
        "Duplex"
        "Bunglow"

    ]
)
def f(p): print(p)
fore= words.foreach(f)