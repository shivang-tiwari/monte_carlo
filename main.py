#########################################################################
import numpy as np
import matplotlib.pyplot as plt
#########################################################################
ITER = 100000
prob = [0.6,0.1,0.3]
#########################################################################

class monte_carlo:
	def __init__(self):
		self.teams = []
		self.nrr = dict()
		self.points = dict()
	
	def add_team(self,name):
		self.teams.append(name)
		self.nrr[name] = 0
		self.points[name] = 0
	
	def add_match_result(self,team1, team2, outcome, run_rate):
		if outcome == team1:
			self.points[team1] += 2
			self.nrr[team1] += run_rate
			self.nrr[team2] -= run_rate
			
		elif outcome == "DRAW":
			self.points[team1] += 1
			self.points[team2] += 1
		else:
			self.points[team2] += 2
			self.nrr[team2] += run_difference / balls
			self.nrr[team1] -= run_difference / balls

	def simulate(self,matches):
		
		average_points = dict()
		
		for team in self.teams:
			average_points[team] = 0
			
		for _ in range(ITER):
			
			table = dict()
			
			for team in self.teams:
				table[team] = 0
			
			for t1,t2,ground in matches:
				if ground == t1:
					table[t1] += 2 * prob[0] + 1 * prob[1]
					table[t2] += 2 * prob[0] + 1 * prob[1]
				else:
					table[t2] += 2 * prob[0] + 1 * prob[1]
					table[t1] += 2 * prob[0] + 1 * prob[1]
			
			for team in self.teams:
				average_points[team] += self.points[team] + table[team]
		
		for team in self.teams:
			average_points[team] = round(average_points[team] / ITER,3)
		
		return average_points
				
			
			

if __name__ == "__main__":
	test = monte_carlo()
	test.add_team("GT")
	test.add_team("CSK")
	
	test.add_match_result("GT","CSK","GT",10,5)
	
	print(test.simulate([["GT","CSK","GT"]]))
