from Entities.Generic.Controller import Controller
from Entities.Activities.Hunting.HuntingView import HuntingView
from Entities.Activities.Hunting.HuntingModel import Hunting
from Entities.Activities.Combat.CombatController import CombatController

class HuntingController(Controller):
	
	def __init__(self):
		self.huntingView = HuntingView()
		self.hunting = Hunting()

	def start(self, player):
		while True:
			playerInput = -1
			try:
				self.huntingView.displayStart()

				playerInput = int(input("Enter an action.\n"))
				print("\n")

				self.clearScreen()

				if(playerInput == 0 ):
					self.huntingView.displayEnd()
					break

				elif(playerInput == 10):
					self.clearScreen()

				elif(playerInput == 1):
					if(self.hunting.chanceToFindAnimal()):
						combatController = CombatController()
						combatController.start(player)
					else:
						self.huntingView.displayNoAnimalFound()


					

				else:
					print("This is not a valid action\n")

			except ValueError:
				print("Please enter a number.\n")
			except:
				print("Error occurred.\n")
				raise

		return player



