import train_naivebayes
import math

if __name__=="__main__":

	# get the gaussian distributions for each feature
	barack_gaussian_arr, mitt_gaussian_arr, p_barack, p_mitt = train_naivebayes.train("train_data.csv")

	total = 0 # total number tested
	correct = 0 # total number we got correct

	with open("testing_data.csv") as test_corpus:
		for line in test_corpus:
			total+=1
			feature_vector = line.strip().split(",")
			
			# for testing only 
			answer = feature_vector[-1]
			feature_vector = feature_vector[:-1]


			feature_vector = map(float, feature_vector)
			total_barack_probability = 1
			total_mitt_probability = 1

			# naive assumption comes into play here. multiply 
			# all of the probabilities and take the classification with the highest total probability
			for i in range(len(feature_vector)):
				barack_probability = barack_gaussian_arr[i].pdf(feature_vector[i])
				if barack_probability > 0:
					total_barack_probability += math.log(barack_probability) + math.log(p_barack)

				mitt_probability = mitt_gaussian_arr[i].pdf(feature_vector[i])
				if mitt_probability > 0:
					total_mitt_probability += math.log(mitt_probability) + math.log(p_mitt)


			# classification!
			if total_barack_probability > total_mitt_probability:
				print "Predicted: Barack Obama"
				if answer == "Barack Obama":
					correct += 1
			else:
				print "Predicted: Mitt Romney"
				if answer == "Mitt Romney":
					correct += 1

	print correct/float(total)






