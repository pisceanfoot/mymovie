def itemValue(item):
	if not isinstance(item, list):
		return item
		
	if len(item) == 1:
			return item[0]
	elif len(item) > 1:
		return ','.join(item)

	return None

def  getNotEmpryList(item):
	if not isinstance(item, list):
		return item

	if len(item) == 0:
		return item

	newItem = []
	for i in item:
		if(i and i.strip()):
			newItem.append(i)

	return newItem