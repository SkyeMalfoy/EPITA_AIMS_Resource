
import math
import random
import json

data = open("iris.data", "r")
matrix = []
for line in data:
    line = line.strip()
    print(line)
    data_line = line.split(",")[:4]
    print(data_line)
    float_vector = []
    if len(data_line) > 3:
        for element in data_line:
            float_vector.append(float(element))
        print(float_vector)
        matrix.append(float_vector)
print(matrix)

def euclidian(V1, V2):
    if len(V1) != len(V2):
        return -1
    #print(V1)
    #print(V2)
    sum = 0
    #print(range(len(V1)))
    for inc in range(len(V1)):
        #print(inc,V1[inc],V2[inc], sum)
        sum = sum + ((V1[inc]-V2[inc])*(V1[inc]-V2[inc]))
    return math.sqrt(sum)
result = euclidian(matrix[0],matrix[1])
print(result)


k = 4

length = len(matrix[0])


centroids = []



for i in range(k):
    point = []
    for j in range(length):
        point.append(((i+1)*(j+1))/5)
    centroids.append(point)

print (centroids)
print (len(centroids))

centroids = []

for i in range(k):
    point = matrix[random.randint(0,len(matrix)-1)]
    centroids.append(point)


print (centroids)
print (len(centroids))


clusters = []

for n_cluster in range(k):
    clusters.append([])

for point in matrix:
    best_distance = -1
    best_inc = -1
    for inc in range(len(centroids)):
        estimated_distance = euclidian(centroids[inc],point)
        #if best_distance == -1:
        if inc == 0:
            best_distance = estimated_distance
            best_inc = inc
        else:
            if best_distance > estimated_distance:
                best_distance = estimated_distance
                best_inc = inc
    clusters[best_inc].append(point)
        
                
#print(json.dumps(clusters, indent=2))
print(json.dumps(clusters))


def centroid(l_cluster, l_length):
    # initialize the centroid
    returned_centroid = [0.0] * l_length
    for l_point in l_cluster:
        # we perform the sum
        for l_inc in range(l_length):
            returned_centroid[l_inc] = returned_centroid[l_inc] + l_point[l_inc]
    # we perform the mean
    for l_inc in range(l_length):
        returned_centroid[l_inc] = round(returned_centroid[l_inc] / len(l_cluster), 2)
    return returned_centroid

def new_centroids(l_clusters, l_length):
    returned_centroids = []
    for l_cluster in l_clusters:
        returned_centroids.append(centroid(l_cluster,l_length))
    return returned_centroids

#print ("Old centroids:", centroids)
#centroids = new_centroids(clusters,length)
#print ("New centroids:", centroids)

def populate_cluster(l_centroids, l_matrix, l_k):
    returned_clusters = []

    for n_cluster in range(l_k):
        returned_clusters.append([])

    for point in l_matrix:
        best_distance = -1
        best_inc = -1
        for inc in range(len(l_centroids)):
            estimated_distance = euclidian(l_centroids[inc],point)
            #if best_distance == -1:
            if inc == 0:
                best_distance = estimated_distance
                best_inc = inc
            else:
                if best_distance > estimated_distance:
                    best_distance = estimated_distance
                    best_inc = inc
        returned_clusters[best_inc].append(point)
    return returned_clusters

#clusters = populate_cluster(centroids, matrix, k)
#print(clusters)
#print ("Old centroids:", centroids)
#centroids = new_centroids(clusters,length)
#print ("New centroids:", centroids)

loops = 20
limit_distance = 0.01

for loop in range(loops):
    clusters = populate_cluster(centroids, matrix, k)
    old_centroids = centroids
    centroids = new_centroids(clusters,length)
    print ("New centroids:", loop, centroids)
    distance = 0
    for l_inc in range(len(centroids)):
        distance = distance + euclidian(old_centroids[l_inc],centroids[l_inc])
    distance = distance / len(centroids)
    print("Distance", distance)
    if distance < limit_distance:
        break


