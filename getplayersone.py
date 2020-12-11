from selenium import webdriver # Using Chrome to access web
from selenium.webdriver.common.by import By  #define By
from selenium.webdriver.common.action_chains import ActionChains
import time

alf = ['a/','b/','c/','d/','e/','f/','g/','h/','i/','j/','k/','l/','m/','n/','o/','p/','q/','r/','s/','t/','u/','v/','w/','x/','y/','z/'] #alphabet
driver = webdriver.Firefox() #Open the website
action = ActionChains(driver)

def start():
    time.sleep(30)
    start = "https://www.basketball-reference.com/players/"
    count = 0
    for x in alf:
        time.sleep(6)
        newstart = start + alf[count] #goes to basketball website "a"
        count = count + 1
        driver.get(newstart)

        #get number of players
        thisstr = driver.find_element_by_xpath("//div[@id='all_players']/div[@class='section_heading']/h2").text
        strnum = thisstr.split(" ")
        numplayer = int(strnum[0])

        #print(numplayer)
        driver.get(newstart)
        #for loop for players begins"
        buffcount = 0
        for i in range(numplayer):

            index = str(buffcount)

            theadcheck = "//table[@id=\"players\"]/tbody/tr[@data-row=\"" + index + "\"]"
            pathstrnorm = "//table[@id=\"players\"]/tbody/tr[@data-row=\"" + index + "\"]/th/a"
            pathstrstrg = "//table[@id=\"players\"]/tbody/tr[@data-row=\"" + index + "\"]/th/strong/a"

            try:
                maybethead = driver.find_element_by_xpath(theadcheck)
            except:
                pass

            if(maybethead.get_attribute("class") == "thead"):
                pass
            else:
                try:
                    driver.find_element_by_xpath(pathstrnorm)
                    playerelement = driver.find_element_by_xpath(pathstrnorm)
                    pathstr = pathstrnorm
                except:
                    playerelement = driver.find_element_by_xpath(pathstrstrg)
                    pathstr = pathstrstrg

                try:
                    playerlink = driver.find_element_by_xpath(pathstr).get_attribute('href')   # get_attribute("href")   #"//table[@id=\"players\"]/tbody/tr[@data-row=\"0\"]/th/a"
                except:
                    driver.execute_script("arguments[0].scrollIntoView();", playerelement)
                    time.sleep(2)

                playernamebuff = driver.find_element_by_xpath(pathstr).text   # get_attribute("href")   #"//table[@id=\"players\"]/tbody/tr[@data-row=\"0\"]/th/a"


                playername = playernamebuff.replace(" ", "_")

                print(playername)

                driver.get(playerlink)

                try:
                    eletable = driver.find_element_by_xpath("//div[@id='all_totals']")
                except:
                    driver.execute_script("arguments[0].scrollIntoView();", eletable)



        #pathfl = "//div[@id='all_totals']/div/div/ul/li[@class='hasmore']"
        #drop = driver.find_element_by_xpath(pathfl)

        #print(drop.text)

        #element
        #move = action.move_to_element(drop)
        #move.perform()

                while(True):
                    try:
                        getcsv = driver.find_element_by_xpath("//div[@id='all_totals']/div[1]/div/ul/li[@class='hasmore drophover']/div/ul/li[4]/button")
                        getcsv.click()
                        wantedtxt = driver.find_element_by_xpath("//div[@id='all_totals']/div[@class='table_outer_container']/div/div/pre").text
                        if(getcsv.click() == None):
                            break
                    except:
                        driver.execute_script("arguments[0].scrollIntoView();", eletable)
                        try:
                            wantedtxt = driver.find_element_by_xpath("//div[@id='all_totals']/div[@class='table_outer_container']/div/div/pre").text
                            break
                        except:
                            pass

                finalname = playername + '.txt'
                finalfile = 'Players/' + finalname

                f = open(finalfile , 'w')
                f.write(wantedtxt)
                f.close()

                with open(finalfile, 'r') as fin:
                    data = fin.read().splitlines(True)
                with open(finalfile, 'w') as fout:
                    fout.writelines(data[4:])

            buffcount = buffcount + 1
            driver.get(newstart)
            time.sleep(3)



#location for a player and their name




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
