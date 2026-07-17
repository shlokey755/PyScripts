import matplotlib.pyplot as plt
import numpy as np
data = {'angry birds':179000,'teen titans':209000,'marvel comics':414000,
        'crazy taxi':311000,'swiggy ginni':455000,'maths formula':278000}
courses=list(data.keys())
values=list(data.values())
fig=plt.figure(figsize=(10,5))
plt.bar(courses,values,color='orange',width=0.5)
plt.xlabel("app name")
plt.ylabel("total app downloads")
plt.title("total app downloads")
plt.show()


