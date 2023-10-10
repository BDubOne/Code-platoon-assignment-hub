
def bottle_song(bottles):
	fridge_capacity = bottles
	full_fridge = ""

	while bottles > 2:
		full_fridge = full_fridge + f"{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around, {bottles - 1} bottles of beer on the wall.  "

		bottles = bottles - 1
	
	
	
	running_out = f"""{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around, {bottles - 1} bottle of beer on the wall.  """
		
	TIME_TO_SHOP = f"""1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, {fridge_capacity} bottles of beer on the wall."""

	# write your code here!
	return full_fridge + running_out + TIME_TO_SHOP

print(bottle_song(15))

####kldjsfalkfdajalskdfjdfls