import random

import time

print('Hello in game "City State"!')

while True:
    country_and_capitals = {
        'Poland': 'Warsaw',
        'Germany': 'Berlin',
        'France': 'Paris',
        'Russia': 'Moscow',
        'Czech Republic': 'Prague',
        'Norway': 'Oslo',
        'Sweden': 'Sztokholm',
        'Afghanistan': 'Kabul',
        'Albania': 'Tirana',
        'Algeria': 'Algiers',
        'Andorra': 'Andorra la Vella',
        'Angola': 'Luanda',
        'Antigua and Barbuda': 'Saint John',
        'Argentina': 'Buenos Aires',
        'Armenia': 'Yerevan',
        'Australia': 'Canberra',
        'Austria': 'Vienna',
        'Azerbaijan': 'Baku',
        'Bahamas': 'Nassau',
        'Bahrain': 'Manama',
        'Bangladesh': 'Dhaka',
        'Barbados': 'Bridgetown',
        'Belarus': 'Minsk',
        'Belgium': 'Brussels',
        'Belize': 'Belmopan',
        'Benin': 'Porto Novo',
        'Bhutan': 'Bhutan',
        'Bolivia': 'La Paz' or 'Sucre',
        'Bosnia and Herzegovina': '	Sarajevo',
        'Botswana': 'Gaborone',
        'Brazil': 'Brasilia',
        'Brunei': 'Bandar Seri Begawan',
        'Bulgaria': 'Sofia',
        'Burkina Faso': 'Ouagadougou',
        'Burundi': 'Gitega',
        'Cambodia': 'Phnom Penh',
        'Cameroon': 'Yaounde',
        'Canada': 'Ottawa',
        'Cape Verde': 'Praia',
        'Central African Republic': 'Bangui',
        'Chad': "N'Djamena",
        'Chile': 'Santiago',
        'China': 'Beijing',
        'Colombia': 'Bogota',
        'Comoros': 'Moroni',
        'Democratic Republic of the Congo': 'Kinshasa',
        'Republic of the Congo': 'Republic of the',
        'Costa Rica': 'San Jose',
        "Côte d'Ivoire (Ivory Coast)": 'Yamoussoukro',
        'Croatia': 'Zagreb',
        'Cuba': 'Havana',
        'Cuprus': 'Nicosia',
        'Denmark': 'Copenhagen',
        'Djibouti': 'Djibouti',
        'Dominica': 'Roseau',
        'Dominican Republic': '	Santo Domingo',
        'East Timor': 'Dili',
        'Ecuador': 'Quito',
        'Egypt': 'Cairo',
        'El Salvador': 'San Salvador',
        'England': 'London',
        'Equatorial Guinea': 'Malabo',
        'Eritrea': 'Asmara',
        'Estonia': 'Tallinn',
        'Eswatini (Swaziland)': 'Mbabana',
        'Ethiopia': 'Addis Ababa',
        'Federated States of Micronesia': 'Palikir',
        'Fiji': 'Suva',
        'Finland': 'Helsinki',
        'Gabon': 'Libreville',
        'Gambia': 'Banjul',
        'Georgia': 'Tbilisi',
        'Ghana': 'Accra',
        'Greece': 'Athens',
        'Grenada': "Saint George's",
        'Guatemala': 'Guatemala City',
        'Guinea': 'Conakry',
        'Guinea-Bissau': 'Bissay',
        'Guyana': 'Georgetown',
        'Haiti': 'Port au Prince',
        'Honduras': 'Tegucigalpa',
        'Hungary': 'Budapest',
        'Iceland': 'Reykjavik',
        'India': 'New Delhi',
        'Indonesia': 'Jakarta',
        'Iran': 'Tehran',
        'Iraq': 'Baghdad',
        'Ireland': 'Dublin',
        'Israel': 'Jerusalem',
        'Italy': 'Rome',
        'Jamaica': 'Kingston',
        'Japan': 'Tokyo',
        'Jordan': 'Amman',
        'Kazakhstan': 'Astana',
        'Kenya': 'Nairobi',
        'Kiribati': 'Tarawa Atoll',
        'Kosovo': 'Pristina',
        'Kuwait': 'Kuwait City',
        'Kyrgyzstan': 'Bishkek',
        'Laos': 'Vientiane',
        'Latvia': 'Riga',
        'Lebanon': 'Beirut',
        'Lesotho': 'Maseru',
        'Liberia': 'Monrovia',
        'Libya': 'Tripoli',
        'Liechtenstein': 'Vaduz',
        'Lithuania': 'Vilnius',
        'Luxembourg': 'Luxembourg',
        'Madagascar': 'Antananarivo',
        'Malawi': 'Lilongwe',
        'Malaysia': 'Kuala Lumpur',
        'Maldives': 'Male',
        'Mali': 'Bamako',
        'Malta': 'Valletta',
        'Marshall Islands': 'Majuro',
        'Mauritania': 'Nouakchott',
        'Mauritius': 'Port Louis',
        'Mexico': 'Mexico City',
        'Moldova': 'Chisinau',
        'Monaco': 'Monaco',
        'Mongolia': 'Ulaanbaatar',
        'Montenegro': 'Podgorica',
        'Morocco': 'Rabat',
        'Mozambique': 'Maputo',
        'Myanmar (Burma)': 'Nay Pyi Taw',
        'Namibia': 'Windhoek',
        'Nauru': 'Yaren',
        'Nepal': '	Kathmandu',
        'Netherlands': 'Amsterdam',
        'New Zealand': 'Wellington',
        'Nicaragua': 'Managua',
        'Niger': 'Niamey',
        'Nigeria': 'Abuja',
        'North Korea': 'Pyongyang',
        'North Macedonia (Macedonia)': 'Skopje',
        'Northern Ireland': 'Belfast',
        'Oman': 'Muscat',
        'Pakistan': 'Islamabad',
        'Palau': 'Melekeok',
        'Palestine': 'Jerusalem',
        'Panama': 'Panama City',
        'Papua New Guinea': 'Port Moresby',
        'Paraguay': 'Asuncion',
        'Peru': 'Lima',
        'Philippines': 'Manila',
        'Portugal': 'Lisbon',
        'Qatar': 'Doha',
        'Romania': 'Bucharest',
        'Rwanda': 'Kigali',
        'Saint Kitts and Nevis': 'Basseterre',
        'Saint Lucia': 'Castries',
        'Saint Vincent and the Grenadines': 'Kingstown',
        'Samoa': 'Apia',
        'San Marino': 'San Marino',
        'Sao Tome and Principe': 'Sao Tome',
        'Saudi Arabia': 'Riyadh',
        'Scotland': 'Edinburgh',
        'Senegal': 'Dakar',
        'Serbia': 'Belgrade',
        'Seychelles': 'Victoria',
        'Sierra Leone': 'Freetown',
        'Singapore': 'Singapore',
        'Slovakia': 'Slovakia',
        'Slovenia': 'Ljubljana',
        'Solomon Islands': 'Honiara',
        'Somalia': 'Mogadishu',
        'South Africa': 'Pretoria' or 'Bloemfontein' or 'Cape Town',
        'South Korea': 'Seoul',
        'South Sudan': 'Juba',
        'Spain': 'Madrid',
        'Sri Lanka': 'Sri Jayawardenapura Kotte',
        'Sudan': 'Khartoum',
        'Suriname': 'Paramaribo',
        'Switzerland': 'Berm',
        'Syria': 'Damascus',
        'Taiwan': 'Taipei',
        'Tajikistan': 'Dushanbe',
        'Tanzania': 'Dodoma',
        'Thailand': 'Bangkok',
        'Togo': 'Lome',
        'Tonga': "Nuku'alofa",
        'Trinidad and Tobago': 'Port of Spain',
        'Tunisia': 'Tunis',
        'Türkiye (Turkey)': 'Ankara',
        'Turkmenistan': 'Ashgabat',
        'Tuvalu': 'Funafuti',
        'Uganda': 'Kampala',
        'Ukraine': 'Kyiv' or 'Kiev',
        'United Arab Emirates': 'Abu Dhabi',
        'United States': 'Washington',
        'Uruguay': 'Montevideo',
        'Uzbekistan': 'Tashkent',
        'Vanuatu': 'Port Vila',
        'Vatican City': 'Vatican City',
        'Venezuela': 'Caracas',
        'Vietnam': 'Hanoi',
        'Wales': 'Cardiff',
        'Yemen': "Sana'a",
        'Zambia': 'Lusaka',
        'Zimbabwe': 'Harare'
    }

    country_dictionary_keys = random.choice(list(country_and_capitals.keys()))

    game_question = input(f'What is the capital {country_dictionary_keys}?\n')
    if country_and_capitals[country_dictionary_keys] == game_question:
        print('Yes! You win!')
        while True:
            end = input('You play agan?\n')
            if end == 'Yes':
                break
            elif end == 'yes':
                break
            elif end == 'No':
                print('Thank you for playing!')
                time.sleep(2)
                exit()
            elif end == 'no':
                print('Thank you for playing!')
                time.sleep(2)
                exit()
            else:
                continue
    else:
        print(f'No! It is about {country_and_capitals[country_dictionary_keys]}')
        while True:
            end = input('You play agan?\n')
            if end == 'Yes':
                break
            elif end == 'yes':
                break
            elif end == 'No':
                print('Thank you for playing!')
                time.sleep(2)
                exit()
            elif end == 'no':
                print('Thank you for playing!')
                time.sleep(2)
                exit()
            else:
                continue
