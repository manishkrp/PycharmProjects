from pyspark import SparkContext
sc = SparkContext("Local","Map App")
words = sc.parallelize(
    [
        "Trisha",
        "Anand",
        "Waqar",
        "George",
        "Simon",
        "Unnati"
    ]
)
wordMap = words.map(lambda f: (x,1))
word_coll = wordMap.collect()
print("The collected words:" %s %(word_coll))