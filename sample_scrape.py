import requests
from bs4 import BeautifulSoup
from csv import writer

# This function will be used to retain just one space between strings in each column
def retain_one_space(values):
    new_values = ""
    prev_char_is_space = False
    for char in values:
        if char == " ":
            if not prev_char_is_space:
                new_values += char
            prev_char_is_space = True
        else:
            new_values += char
            prev_char_is_space = False
    return new_values

# We write a loop to extract multiple pages from the URL and export in a csv
for j in range(1,5):
    source = requests.get(f"https://www.kijiji.ca/b-cars-trucks/manitoba/honda-civic/2015__2023/page-{j}/k0c174l9006a68")
    soup = BeautifulSoup(source.content, 'html.parser') # get the content of the ulr above
    lists = soup.find_all('div', class_="info-container") # find all "div" with the class info-container

    with open('civicMAN.csv', 'a', encoding='utf8', newline='') as f:  # open my created csv file to append the extracted data
        theWriter = writer(f) # signifying the variable "thewriter" to write into f(civivMan.csv)
        header = ['price', 'Title', 'Location', 'OdoType'] # create header for the first row in the extracted data
        theWriter.writerow(header) # use writerow function to first row( which the header list above)

        # we write a for loop to extract the content of each row from our data
        for list in lists:
            price = list.find('div', class_="price").text.replace('\n', '').strip()
            new_price= retain_one_space(price)

            title = list.find('div', class_="title").text.replace('\n', '').strip()
            new_title= retain_one_space(title)

            location = list.find('div', class_="location").text.replace('\n', '').strip()
            new_location= retain_one_space(location)

            OdoType = list.find('div', class_="details").text.replace('\n', '').strip()
            new_OdoType= retain_one_space(OdoType)

           # We append each row at a time into a list object "info" and write into the file f
            info=[new_price, new_title, new_location, new_OdoType]
            theWriter.writerow(info)



    #discription = list.find('div', class_="description")

#print(len(lists))
