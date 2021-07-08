sea = ('cod', 'herring', 'marlin')
fresh = ('asp', 'carp', 'ide' 'trout')

function_merge(sea, fresh)
object = list.new
	
while not (sea.empty and fresh.empty):
	if sea.top_iteam > fresh.top_item:
		fish = sea.remove_top_item
			
	else:
		fish = fresh.remove_top_item
	result.append(fish)
		
print (object)

