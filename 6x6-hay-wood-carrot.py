def start(x = get_pos_x(), y = get_pos_y()):
	
	def checkToPlant():
		x = get_pos_x()
		y = get_pos_y()
		if ((x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1)):
			if (can_harvest()):
				harvest()
				plant(Entities.Tree)
			if (get_water() <=  75 and num_items(Items.Water)):
				use_item(Items.Water)
		else:
			if (x >= get_world_size() / 2):
				if (get_ground_type() != Grounds.Soil):
					harvest()
					till()
				harvest()
				plant(Entities.Carrot)
			else:
				harvest()

	while(True):
		
		# Move Up
		while(get_pos_y() != get_world_size()-1):
			checkToPlant()
			move(North)
			
		# Move Right
		checkToPlant()
		move(East)
		
		# Move Down
		while(get_pos_y() != 0):
			checkToPlant()
			move(South)
	
		# Move Right
		checkToPlant()
		move(East)
