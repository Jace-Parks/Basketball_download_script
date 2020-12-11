from selenium import webdriver # Using Chrome to access web
from selenium.webdriver.common.by import By  #define By
from selenium.webdriver.common.action_chains import ActionChains
import time

alf = ['a/','b/','c/','d/','e/','f/','g/','h/','i/','j/','k/','l/','m/','n/','o/','p/','q/','r/','s/','t/','u/','v/','w/','x/','y/','z/'] #alphabet
driver = webdriver.Firefox() #Open the website
action = ActionChains(driver)

#location for a player and their name
def getPlayerData(playerstart, playernamebuff, runitback):
    driver.get(playerstart)
    time.sleep(3)

    eletable = driver.find_element_by_xpath("//div[@id='all_totals']")

    driver.execute_script("arguments[0].scrollIntoView();", eletable)
    time.sleep(3)

    pathfl = "//div[@id='all_totals']/div[1]/div/ul/li[@class='hasmore']"
    drop = driver.find_element_by_xpath(pathfl)


    print(drop.text)

    #element
    move = action.move_to_element(drop)
    move.perform()

    time.sleep(3)

    getcsv = driver.find_element_by_xpath("//div[@id='all_totals']/div[1]/div/ul/li[@class='hasmore drophover']/div/ul/li[4]/button")

    getcsv.click()

    wantedtxt = driver.find_element_by_xpath("//div[@id='all_totals']/div[@class='table_outer_container']/div/div/pre").text

    finalname = playernamebuff + '.txt'
    finalfile = 'Players/' + finalname

    f = open(finalfile , 'w')
    f.write(wantedtxt)
    f.close()

    with open(finalfile, 'r') as fin:
        data = fin.read().splitlines(True)
    with open(finalfile, 'w') as fout:
        fout.writelines(data[4:])

    driver.get(runitback)

#def getLetter():

def start():
    start = "https://www.basketball-reference.com/players/"

#    for x in alf:
    newstart = start + alf[0] #goes to basketball website "a"
    driver.get(newstart)

        #get number of players
    thisstr = driver.find_element_by_xpath("//div[@id='all_players']/div[@class='section_heading']/h2").text
    strnum = thisstr.split(" ")
    numplayer = int(strnum[0])

    print(numplayer)

        #for loop for players begins"
    for x in range(numplayer):
        driver.get(newstart)

        index = input("number: ")
        pathstr = "//table[@id=\"players\"]/tbody/tr[@data-row=\"" + index + "\"]/th/a"
        playerelement = driver.find_element_by_xpath(pathstr)
        playerlink = driver.find_element_by_xpath(pathstr).get_attribute('href')   # get_attribute("href")   #"//table[@id=\"players\"]/tbody/tr[@data-row=\"0\"]/th/a"
        driver.execute_script("arguments[0].scrollIntoView();", playerelement)
        playernamebuff = driver.find_element_by_xpath(pathstr).text   # get_attribute("href")   #"//table[@id=\"players\"]/tbody/tr[@data-row=\"0\"]/th/a"
        time.sleep(3)

        playername = playernamebuff.replace(" ", "_")

        print(playername)

        getPlayerData(playerlink,playername,newstart)


start()




#driver.find_element_by_xpath("//li[@class='hasmore']/div/ul/li[4]/button").click()  #//button[@text='Get table as CSV (for Excel)']
#button.click()


#csvbut = driver.find_element_by_xpath("//li[@class='hasmore']/div/ul/li[4]/button")  #//button[@text='Get table as CSV (for Excel)']
#csvbut.click()

#print()
#print(driver.find_element_by_xpath("//li[@class='hasmore']/div/ul/li[3]")).getdriver.find_element_by_xpath("//li[@class='hasmore']")
#.get_text()
#print(button)

#print(newstart)

#for x in alf:
#    newstart = start + alf
#    driver.get(newstart)
#    x = x + 1
#driver.quit()
