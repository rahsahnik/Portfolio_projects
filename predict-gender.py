import requests
from tkinter import * 
import tkinter as tk
import mysql.connector

# Country code is passed as an argument in the request URl.
# User can select the country names from the dropdown List.

OPTIONS = {"France":"FR", "Italy":"IT", "Spain":"ES", "Turkey":"TR", "Germany":"DE", "Poland":"PL", "United Kingdom":"GB", 
           "Russia":"RU", "Czech Republic":"CZ", "Portugal":"PT", "Netherlands":"NL", "Belgium":"BE", "Morocco":"MA",
           "Philippines":"PH", "United States":"US", "Romania":"RO", "Algeria":"DZ", "Nigeria":"NG", "Switzerland":"CH",
           "Hungary":"HU", "Thailand":"TH", "Sweden":"SE", "Indonesia":"ID", "India":"IN", "Ukraine":"UA", "Malaysia":"MY",
           "Tunisia":"TN", "Saudi Arabia":"SA", "Greece":"GR", "Ivory Coast":"CI", "Austria":"AT", "South Africa":"ZA",
           "South Korea":"KR", "China":"CN", "Serbia":"RS", "Japan":"JP", "Egypt":"EG", "Slovakia":"SK", "Senegal":"SN",
           "Denmark":"DK", "Finland":"FI", "Cameroon":"CM", "Iran":"IR", "Argentina":"AR", "Canada":"CA", "Singapore":"SG",
           "Pakistan":"PK", "Ghana":"GH", "Lebanon":"LB", "Ireland":"IE", "Angola":"AO", "Norway":"NO", "Belarus":"BY",
           "Brazil":"BR", "Mexico":"MX", "Colombia":"CO", "Kenya":"KE", "Chile":"CL", "Kuwait":"KW", "Albania":"AL",
           "Venezuela":"VE", "Reunion":"RE", "Bosnia and Herzegovina":"BA", "Israel":"IL", "Taiwan":"TW", "Slovenia":"SI",
           "Kazakhstan":"KZ", "Peru":"PE", "Azerbaijan":"AZ", "United Arab Emirates":"AE", "Cyprus":"CY", "Lithuania":"LT",
           "Dominican Republic":"DO", "Jordan":"JO", "Moldova":"MD", "Benin":"BJ", "Bulgaria":"BG", 
           "Democratic Republic of the Congo":"CD", "Croatia":"HR", "Latvia":"LV", "Hong Kong":"HK", "Mozambique":"MZ",
           "Australia":"AU", "Luxembourg":"LU", "Uganda":"UG", "Mali":"ML", "Burkina Faso":"BF", "Mauritius":"MU", "Oman":"OM",
           "Togo":"TG", "Qatar":"QA", "Macedonia":"MK", "Madagascar":"MG", "Vietnam":"VN", "Gabon":"GA", "Estonia":"EE", 
           "Iraq":"IQ", "Malta":"MT", "Bahrain":"BH", "Tanzania":"TZ", "Ecuador":"EC", "Georgia":"GE", "Armenia":"AM", 
           "Sudan":"SD", "Ethiopia":"ET", "Myanmar":"MM", "Montenegro":"ME", "Syria":"SY", "Uzbekistan":"UZ", 
           "Zimbabwe":"ZW", "Djibouti":"DJ", "Sri Lanka":"LK", "Bangladesh":"BD", "Saint Helena":"SH", "Botswana":"BW",
           "Cape Verde":"CV", "Bolivia":"BO", "Yemen":"YE", "Rwanda":"RW", "Iceland":"IS", "Libya":"LY", "Niger":"NE",
           "Andorra":"AD", "Gambia":"GM", "Republic of the Congo":"CG", "Zambia":"ZM", "Afghanistan":"AF", "Namibia":"NA", 
           "Mauritania":"MR", "Uruguay":"UY", "Costa Rica":"CR", "Kyrgyzstan":"KG", "Panama":"PA", "Nepal":"NP", 
           "Guinea":"GN", "Guadeloupe":"GP", "Equatorial Guinea":"GQ", "Martinique":"MQ", "Seychelles":"SC", "Cuba":"CU",
           "New Zealand":"NZ", "Guatemala":"GT", "Monaco":"MC", "Maldives":"MV", "Malawi":"MW", "El Salvador":"SV", 
           "French Guiana":"GF", "Sierra Leone":"SL", "Liberia":"LR", "Nicaragua":"NI", "Cambodia":"KH", "Tajikistan":"TJ", 
           "Puerto Rico":"PR", "Burundi":"BI", "Paraguay":"PY", "Comoros":"KM", "Lesotho":"LS", "Somalia":"SO",
           "Honduras":"HN", "Chad":"TD", "Gibraltar":"GI", "Brunei":"BN", "San Marino":"SM", "Jersey":"JE",
           "Swaziland":"SZ", "Turkmenistan":"TM", "New Caledonia":"NC", "Mongolia":"MN", "Liechtenstein":"LI",
           "Greenland":"GL", "Bhutan":"BT", "French Polynesia":"PF", "Sao Tome and Principe":"ST", "Mayotte":"YT",
           "Faroe Islands":"FO", "Jamaica":"JM", "Haiti":"HT", "Bahamas":"BS", "Guinea-Bissau":"GW", "Fiji":"FJ",
           "Guernsey":"GG", "Laos":"LA", "East Timor":"TL", "Trinidad and Tobago":"TT", "Antigua and Barbuda":"AG", 
           "Western Sahara":"EH", "Central African Republic":"CF", "Palau":"PW", "Isle of Man":"IM", "Aruba":"AW", 
           "Belize":"BZ", "American Samoa":"AS", "Anguilla":"AI", "Northern Mariana Islands":"MP", "Bermuda":"BM",
           "Eritrea":"ER", "Suriname":"SR", "British Virgin Islands":"VG", "U.S. Virgin Islands":"VI", "Guyana":"GY",
           "Barbados":"BB", "Marshall Islands":"MH", "Macao":"MO", "Papua New Guinea":"PG", "Cayman Islands":"KY", 
           "Kiribati":"KI", "Netherlands Antilles":"AN", "Cook Islands":"CK", "Guam":"GU", "Wallis and Futuna":"WF",
           "Palestine":"PS", "Turks and Caicos Islands":"TC", "Vanuatu":"VU", "Saint Lucia":"LC", "Tonga":"TO", 
           "Cocos Islands":"CC", "Samoa":"WS", "Grenada":"GD", "Vatican":"VA", "British Indian Ocean Territory":"IO",
           "Micronesia":"FM", "Niue":"NU", "Saint Barthelemy":"BL", "Saint Kitts and Nevis":"KN", "Saint Pierre and Miquelon":"PM",
           "Falkland Islands":"FK", "Antarctica":"AQ", "Pitcairn":"PN", "Saint Martin":"MF", "Tuvalu":"TV", 
           "Saint Vincent and the Grenadines":"VC", "Dominica":"DM", "Solomon Islands":"SB", "Tokelau":"TK", "Norfolk Island":"NF", 
           "Christmas Island":"CX", "Nauru":"NR", "Svalbard and Jan Mayen":"SJ", 
           "Montserrat":"MS", "North Korea":"KP", "South Georgia And Sandwich Isl.":"GS", "Bouvet Island":"BV"
}

gender_url="https://api.genderize.io/"             # API URL to be used to determine the Gender of Person
gname=input("Enter name to determine gender : ")       


# Defining/Designing the UI to select the country, which would be then sent along with the request

master = Tk()

master['bg']='#f080ff'
master.geometry("350x300")
master.title("COUNTRIES")
l = Label(master, text = "Select Country and Press OK ",bg="#ffa64d")
l.pack(side=TOP,padx=10, pady=10)
variable = StringVar(master)
variable.set("INDIA")    # default value displayed
w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    global gcountry
    gcountry=OPTIONS[variable.get()] #variable.get() returns the key (i.e. country name) , but we need the country code so use key as index to fetch country ID

    result=Label(master,text="You selected Country : "+ variable.get() + "\nPlease Press EXIT to view Gender")
    result.pack()
button = Button(master, text="OK", command=ok, bg="#1aff1a")
button.pack(side=TOP,padx=10, pady=10)

# The below commented code has some issues, if anyone can help me out in fixing this. Thanks
#gender_response=requests.get(gender_url+"?name="+gname+"&country_id="+gcountry).json() # sending request

# def result():
     
#     result=Label(master,text="Gender of "+str(gname).upper() + " is "+ str(gender_response['gender']).upper() + " in " +variable.get() +" \nwith PROBABILITY of : "+ percentage +" %")
#     result.pack()
    
# button = Button(master, text="Result", command=result, bg="#1aff1a")
# button.pack(side=TOP,padx=10, pady=10)

button_exit=Button(master,text="EXIT", command=master.destroy,bg="#ff1a75")
button.pack(side=TOP,padx=10, pady=10)
button_exit.pack()
mainloop()

gender_response=requests.get(gender_url+"?name="+gname+"&country_id="+gcountry).json()

percentage=str(gender_response['probability']*100)
malefemale=str(gender_response['gender'])

print(f"Gender of {gname} is {gender_response['gender']} "+ "in " +variable.get() +" with PROBABILITY of :"+ percentage +" %")

#Stroing the data to SQL Database

try: 
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",               # use username as per your Mysql  settings 
      password="",            # use password as per your Mysql settings             
      database="gender_api"  
    )

    mycursor = mydb.cursor()
    mycursor.execute('''create table if not exists gender (
                            Name varchar(20),
                            Gender Varchar(10),
                            Country varchar(20),
                            Probability varchar(5)        );''')
    
    sql = "INSERT INTO gender VALUES (%s,%s,%s,%s)" 
    val=(gname,malefemale,variable.get(),percentage)
    mycursor.execute(sql,val)
    mydb.commit()
    
    print(mycursor.rowcount, "Record inserted Successfully to Database ")
    mycursor.close()
    mydb.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Gender table {}".format(error))

finally:
    if mydb.is_connected():
        mydb.close()
        print("MySQL connection is closed")
