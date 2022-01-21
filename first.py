company_data = ['book','pencil','pen','note book','sharpener','ruber']
item = input('what item do you want to check for in the bag?')

for i in range(1):
    if item in company_data:
        print('Item is in company data')
        break
    else:
        print("data is not available")
