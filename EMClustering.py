import math

def get_prob(mu,sd,x):
    return math.exp(-1*(x-mu)*(x-mu)/(2*sd*sd))/(math.sqrt(2*math.pi*sd*sd))

#clusters_prev = [[0,0],[0,0]]
# count probability of each datapoint using current clustering values

def EM_Clustering(dps,clusters,epsilon=1e-6):
    while True:
        dps_probs = []
        for dp in dps:
            probs = []
            for i in range(len(clusters)):
                probs.append(get_prob(clusters[i][0],clusters[i][1],dp))
            dps_probs.append(probs)

        #print(dps_probs)

        # normalize the probabilities
        # Using two-cluster scenario as example, p1_n = p1 / (p1 + p2), p2_n = p2 / (p1 + p2) 
        dps_probs_n = []

        for item in dps_probs:
            prob_sum = sum(item)
            probs = []
            for prob in item:
                probs.append(prob/prob_sum)

            dps_probs_n.append(probs)

        #print(dps_probs_n)

        #update the clusters (i.e., the u and v values) based on the probabilities of x belonging to each cluster

        clusters_prev = []

        for i in range(len(clusters)):
            mu_num = 0
            den = 0 
            for j in range(len(dps)):
                mu_num += dps[j]*dps_probs_n[j][i]
                den += dps_probs_n[j][i]
            
            mu = mu_num/den
            
            v = 0
            for j in range(len(dps)):
                v += (dps[j]-mu)*(dps[j]-mu)/den
            
            sd = math.sqrt(v)

            #clusters_prev[i] = clusters[i]
            clusters_prev.append([clusters[i][0],clusters[i][1]])
            clusters[i] = [sd,mu]

        print(clusters)        

        # **Check for Convergence**
        if all(abs(clusters[i][0] - clusters_prev[i][0]) < epsilon and
                abs(clusters[i][1] - clusters_prev[i][1]) < epsilon for i in range(len(clusters))):
            break
        

dps = [15, 6, 3, 2, 10, 16, 3, 5, 11, 10]

clusters = [[2, 7], [12, 2]]
epsilon = 1e-6

EM_Clustering(dps,clusters)
print("hello")