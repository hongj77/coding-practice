import scipy.stats


def train(fileName):
	''' Continuous case of naive bayes classifier assuming gaussian distribution '''

	# this is for use later to find P(barack) and P(mitt) on training data
	count_barack = 0
	count_mitt = 0

	# parse data
	train_data = []
	with open(fileName) as handle:
		for line in handle:
			data_list = line.strip().replace("\r",",").split(",")
			if data_list[-1] == "Mitt Romney": count_mitt+=1
			if data_list[-1] == "Barack Obama": count_barack+=1
	 		train_data.append(data_list)

	totalLines = len(train_data)

	# dimension of feature vector
	dim = len(train_data[0])-1 # minus 1 is because last column is not a feature

	# for each of the 14 features, we estimate the mean for each feature
	barack_mean_arr = []
	mitt_mean_arr = []

	# look at each feature one by one and calculate mean
	for col in range(dim):
		barack_sum = 0 
		barack_N = 0

		mitt_sum = 0
		mitt_N = 0

		for row in range(len(train_data)):
			if row == 0: continue # not actual values

			# training mean separately for romney and obama
			if train_data[row][-1] == "Mitt Romney": 
				mitt_sum += float(train_data[row][col])
				mitt_N += 1

			if train_data[row][-1] == "Barack Obama":
				barack_sum += float(train_data[row][col])
				barack_N += 1

		barack_mean_arr.append(barack_sum/float(barack_N))
		mitt_mean_arr.append(mitt_sum/float(mitt_N))


	# for each of the 14 features, we estimate the std dev
	barack_dev_arr = []
	mitt_dev_arr = []

	# calculate std dev of each feature
	for col in range(dim):
		barack_sum = 0 
		barack_N = 0

		mitt_sum = 0
		mitt_N = 0

		for row in range(len(train_data)):
			if row == 0: continue
			val = float(train_data[row][col])

			if train_data[row][-1] == "Mitt Romney": 
				mitt_sum += (val - float(mitt_mean_arr[col]))**2
				mitt_N += 1

			if train_data[row][-1] == "Barack Obama":
				barack_sum += (val - float(barack_mean_arr[col]))**2
				barack_N += 1

		barack_dev_arr.append(barack_sum/float(barack_N))
		mitt_dev_arr.append(mitt_sum/float(mitt_N))


	# make a guassian distribution for each feature
	barack_gaussian_arr = []
	mitt_gaussian_arr = []

	for i in range(dim):
		barack_distribution = scipy.stats.norm(barack_mean_arr[i], barack_dev_arr[i])
		barack_gaussian_arr.append(barack_distribution)

		mitt_distribution = scipy.stats.norm(mitt_mean_arr[i], mitt_dev_arr[i])
		mitt_gaussian_arr.append(mitt_distribution)

	return barack_gaussian_arr, mitt_gaussian_arr, count_barack/float(totalLines), count_mitt/float(totalLines)
