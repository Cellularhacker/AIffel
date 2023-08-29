# Q. 직접 만들어보세요.

def FibonaChicken(n, m=0, prev=0, prev_2=0):
	# WARN: 최초의 n은 사람의 명 수이지만, 우리가 구해야 하는 것은 그 사람 명 수 미만의 피보나치 수열의 누적 이기 때문에, break 지점을 만들어야 합니다.
		# MARK: 여기서는 피보나치 수열의 순서를 매기기 위해 m을 사용하겠습니다.

	number = 0

	if (n <= 0):
		number = 0
		return number
	elif (n <= 2):
		number = 1
		return number
	elif (n == 3):
		# MARK: 성능향상을 위해서 굳이 이렇게 하였습니다. 습관이네요...
		number = 2
		return number
	else:
		# MARK: 3명을 초과하는 경우의 수 부터는 직전 수열의 값과 더하여 범위내에 해당되는지 비교하기 위해 재귀호출에 들어갑니다.
		# MARK: 직전 값이 특별히 제공되지 않은 경우, 다음 수열의 값에 도달하지 않았다고 보고, 3명이 먹을(n=3일 때) 값인 2를 디폴트로 둡니다.
		if (prev == 0 or 4 <= n <= 5):
			prev = 2
			prev_2 = 1
		
		# MARK: 하나의 함수로 구현할 때, n이라는 단어가 헷갈리지 않게 하기 위해서 m으로 썼습니다.
		# MARK: 여기까지 if ~ elif ~ else 문을 통과했는데, m이 0인 상태라면 디폴트로 0인 경우 밖에 없습니다. 즉, 피보나치 수열의 4번째의 값을 구해야하는 상황인 것입니다. 따라서 m은 4로 지정합니다.
		if (m == 0):
			m = 4
		
		number = prev + prev_2
		
		
		# MARK: 그리고나서, m번째 (n명 아닌 것이 가장 중요합니다. 아예 별개 입니다. 따로 놀아야 합니다. 따로 따로 따로)
		# MARK: m 번째, 첫번째로 else에서는 4 번째 피보나치 수열의 값, 1+2의 값인 3과 직전 값인 2를 더하여 나온 값인
		# MARK: 5. 이 5를 n 명에서 뺍니다.
		remain_people = n - (number + prev)
		
		if (remain_people > 0):
			prev_2 = prev
			prev = number
			
			print("[DEBUG] 이 다음으로 구하는 피보나치 수는 수열에서 몇 번째?: `{0}`".format(m+1))
			print("	방금 구한 수와 수열에서의 숫자는?: `{0}` -> `{1}`".format(m, prev))
			print("	이 직전에 구한 것은..?: `{0}` -> `{1}`".format(m-1, prev_2))	
			
			return FibonaChicken(n, m=m+1, prev=number, prev_2=prev)
		else:
			return prev

		
	return 0
